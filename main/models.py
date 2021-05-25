from main.choices import groups, purchase, dispatch, gender_choices
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, UserManager
from django.utils.translation import ugettext as _
from django.utils import timezone


class Outlet(models.Model):  #
    date_modified = models.DateTimeField(_('Date and Time Modified'), null=False, blank=False, unique=False,
                                         auto_now=True)
    date_added = models.DateTimeField(
        _('Date and Time'), null=False, blank=False, unique=False, auto_now_add=True)

    address = models.CharField(
        _("Address"), max_length=500, null=True, blank=True)

    name = models.CharField(_('Name'), max_length=30, null=False, blank=False,
                            unique=True)
    description = models.CharField(_('Description'), max_length=100, null=False, blank=False,
                                   unique=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return '/outlet/%s' % self.title

    class Meta:
        ordering = ['-date_modified']
        verbose_name = _('Outlet')
        verbose_name_plural = _('Outlets')


class Till(models.Model):  #
    date_added = models.DateTimeField(
        _('Date and Time'), null=False, blank=False, unique=False, auto_now_add=True)

    till_number = models.CharField(
        _("Till Number"), max_length=500, null=True, blank=True)

    outlet = models.ForeignKey(
        Outlet, blank=False, null=True, unique=False, on_delete=models.CASCADE)

    description = models.CharField(_('Description'), max_length=100, null=False, blank=False,
                                   unique=True)

    def get_absolute_url(self):
        return '/till/%s' % self.title

    class Meta:
        ordering = ['-till_number']
        verbose_name = _('Till')
        verbose_name_plural = _('Tills')


class Store(models.Model):  #
    date_modified = models.DateTimeField(_('Date and Time Modified'), null=False, blank=False, unique=False,
                                         auto_now=True)
    date_added = models.DateTimeField(
        _('Date and Time'), null=False, blank=False, unique=False, auto_now_add=True)

    address = models.CharField(
        _("Address"), max_length=500, null=True, blank=True)

    name = models.CharField(_('Name'), max_length=30, null=False, blank=False,
                            unique=True)
    description = models.CharField(_('Description'), max_length=100, null=False, blank=False,
                                   unique=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return '/store/%s' % self.title

    class Meta:
        ordering = ['-date_modified']
        verbose_name = _('Store')
        verbose_name_plural = _('Stores')


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """creates and saves a new user"""
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create a super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class Supplier(models.Model):
    email = models.EmailField(_("email address"), max_length=255, unique=True)
    name = models.CharField(_("Name"), max_length=255, null=True)
    address = models.CharField(_("Address"), max_length=255)

    def __str__(self):
        return str(self.name)


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(_("email address"), max_length=255, unique=True)
    first_name = models.CharField(_("first name"), max_length=255, null=True)
    last_name = models.CharField(_("last name"), max_length=255)
    gender = models.CharField(
        _("gender"), max_length=1, choices=gender_choices)
    store = models.ForeignKey(
        Store, blank=False, null=True, unique=False, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(_("Date joined"), default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Item(models.Model):  #
    date_modified = models.DateTimeField(_('Date and Time Modified'), null=False, blank=False, unique=False,
                                         auto_now=True)
    date_added = models.DateTimeField(
        _('Date and Time'), null=False, blank=False, unique=False, auto_now_add=True)

    quantity = models.IntegerField(
        _('Quantity'), default=10, null=False, blank=False)
    re_order_level = models.IntegerField(
        _('Re-order Level'), default=5, null=False, blank=False)
    id = models.AutoField(null=False, blank=False, primary_key=True)

    title = models.CharField(_('Title'), max_length=30, null=False, blank=False,
                             unique=True)
    barcode = models.CharField(_('Barcode'), max_length=12, null=False, blank=False,
                               unique=True)
    description = models.CharField(_('Description'), max_length=100, null=False, blank=False,
                                   unique=False)
    supplier = models.ForeignKey(
        Supplier, blank=True, null=True, unique=False, on_delete=models.CASCADE)
    unit_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)

    def get_absolute_url(self):
        return '/items/%s' % self.title

    class Meta:
        ordering = ['-date_modified']
        verbose_name = _('Item')
        verbose_name_plural = _('Items')


class Dispatch(models.Model):
    date = models.DateTimeField(
        _('Date and Time'), null=False, blank=False, unique=False, auto_now_add=True)
    store = models.ForeignKey(
        Store, blank=False, null=True, unique=False, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, blank=False, null=True, unique=False, on_delete=models.CASCADE)
    item = models.ForeignKey(
        Item, blank=False, null=True, unique=False, on_delete=models.CASCADE)

    initial_quatity = models.IntegerField(
        _('Initial Quantity'), default=10, null=False, blank=False)

    quantity = models.IntegerField(
        _('Quantity'), default=10, null=False, blank=False)

    new_quatity = models.IntegerField(
        _('New Quantity'), default=10, null=False, blank=False)

    id = models.AutoField(null=False, blank=False, primary_key=True)
    transaction_type = models.CharField(
        _('Transaction Type'), default='add', max_length=30, unique=False, choices=dispatch)
    money_value = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['-date']
        verbose_name = _('Purchase')
        verbose_name_plural = _('Purchases')


class Purchase(models.Model):
    date = models.DateTimeField(
        _('Date and Time'), null=False, blank=False, unique=False, auto_now_add=True)
    store = models.ForeignKey(
        Store, blank=False, null=True, unique=False, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, blank=False, null=True, unique=False, on_delete=models.CASCADE)
    item = models.ForeignKey(
        Item, blank=False, null=True, unique=False, on_delete=models.CASCADE)

    initial_quatity = models.IntegerField(
        _('Initial Quantity'), default=10, null=False, blank=False)

    quantity = models.IntegerField(
        _('Quantity'), default=10, null=False, blank=False)

    new_quatity = models.IntegerField(
        _('New Quantity'), default=10, null=False, blank=False)

    id = models.AutoField(null=False, blank=False, primary_key=True)
    transaction_type = models.CharField(
        _('Transaction Type'), default='add', max_length=30, unique=False, choices=purchase)
    money_value = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['-date']
        verbose_name = _('Purchase')
        verbose_name_plural = _('Purchases')


class Recipt(models.Model):
    ref_number = models.CharField(
        max_length=6, null=False, blank=False, unique=True, primary_key=True)
    date_of_generated = models.DateTimeField(
        _('Date and Time '), null=False, blank=False, unique=False, auto_now_add=True)
    transaction = models.ForeignKey(
        Purchase, blank=False, null=True, unique=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.refNumber

    class Meta:
        ordering = ['date_of_generated']


class Invoice(models.Model):
    ref_number = models.CharField(
        max_length=5, null=False, blank=False, unique=True, primary_key=True)
    date_of_generated = models.DateTimeField(
        _('Date and Time '), null=False, blank=False, unique=False, auto_now_add=True)
    transaction = models.ForeignKey(
        Dispatch, blank=False, null=True, unique=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.refNumber

    class Meta:
        ordering = ['date_of_generated']


class SuppliedBy(models.Model):
    date_modified = models.DateTimeField(
        _("Date and Time"), null=False, blank=False, unique=False, auto_now=True)
    date_added = models.DateTimeField(
        _("Date and Time"), null=False, blank=False, unique=False, auto_now_add=True)
    id = models.AutoField(null=False, blank=False, primary_key=True)
    store = models.ForeignKey(
        Store, blank=False, null=True, unique=False, on_delete=models.CASCADE)
    outlet = models.ForeignKey(
        Outlet, blank=False, null=True, unique=False, on_delete=models.CASCADE)
    transaction = models.ForeignKey(
        Purchase, blank=False, null=True, unique=False, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-date_modified"]


class DispatchedBy(models.Model):
    date_modified = models.DateTimeField(
        _("Date and Time"), null=False, blank=False, unique=False, auto_now=True)
    date_added = models.DateTimeField(
        _("Date and Time"), null=False, blank=False, unique=False, auto_now_add=True)
    id = models.AutoField(null=False, blank=False, primary_key=True)
    store = models.ForeignKey(
        Store, blank=False, null=True, unique=False, on_delete=models.CASCADE)
    outlet = models.ForeignKey(
        Outlet, blank=False, null=True, unique=False, on_delete=models.CASCADE)
    transaction = models.ForeignKey(
        Dispatch, blank=False, null=True, unique=False, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-date_modified"]
