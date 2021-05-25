from .models import User, Item, Store, Outlet, Purchase, DispatchedBy, Dispatch, SuppliedBy, DispatchedBy, Supplier, SuppliedBy
from .serializers import ItemSerializer
from datetime import timedelta
from itertools import chain
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.contrib.messages import constants


from bootstrap_modal_forms.generic import (
    BSModalLoginView,
    BSModalFormView,
    BSModalCreateView,
    BSModalUpdateView,
    BSModalReadView,
    BSModalDeleteView
)

from .forms import (
    StoreModelForm,
    OutletModelForm,
    UserModelForm,
    ItemModelForm,
    CustomUserCreationForm,
    CustomAuthenticationForm,
    DispatchForm,
    PurchaseForm,
    SupplierModelForm
)


class SignUpView(BSModalCreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_message = 'Success: Sign up succeeded. You can now Log in.'
    success_url = reverse_lazy('index')


class CustomLoginView(BSModalLoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'registration/login.html'
    success_message = 'Success: You were successfully logged in.'
    success_url = reverse_lazy('dashboard')


class ItemIndex(generic.ListView):
    model = Item
    context_object_name = 'items'
    template_name = 'items.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs


class ItemCreateView(BSModalCreateView):
    template_name = 'item/create_item.html'
    form_class = ItemModelForm
    success_message = 'Success: Item was created.'
    success_url = reverse_lazy('item_index')


class ItemUpdateView(BSModalUpdateView):
    model = Item
    template_name = 'item/update_item.html'
    form_class = ItemModelForm
    success_message = 'Success: Item was updated.'
    success_url = reverse_lazy('item_index')


class ItemReadView(BSModalReadView):
    model = Item
    template_name = 'item/read_item.html'


class ItemDeleteView(BSModalDeleteView):
    model = Item
    template_name = 'item/delete_item.html'
    success_message = 'Success: Item was deleted.'
    success_url = reverse_lazy('item_index')


@permission_required('main.view_item')
def items(request):
    data = dict()
    if request.method == 'GET':
        items = Item.objects.all()
        data['table'] = render_to_string(
            '_Items_table.html',
            {'items': items},
            request=request
        )
        return JsonResponse(data)


class UserIndex(generic.ListView):
    model = User
    context_object_name = 'users'
    template_name = 'users.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs


class UserUpdateView(BSModalUpdateView):
    model = User
    template_name = 'user/update_user.html'
    form_class = UserModelForm
    success_message = 'Success: User was updated.'
    success_url = reverse_lazy('user_index')


class UserReadView(BSModalReadView):
    model = User
    template_name = 'user/read_user.html'


class UserDeleteView(BSModalDeleteView):
    model = User
    template_name = 'user/delete_user.html'
    success_message = 'Success: User was deleted.'
    success_url = reverse_lazy('user_index')


@permission_required('main.view_user')
def users(request):
    data = dict()
    if request.method == 'GET':
        users = User.objects.all()
        data['table'] = render_to_string(
            '_users_table.html',
            {'users': users},
            request=request
        )
        return JsonResponse(data)


class Index(generic.ListView):
    model = Store
    context_object_name = 'stores'
    template_name = 'stores.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs


class StoreCreateView(BSModalCreateView):
    template_name = 'store/create_store.html'
    form_class = StoreModelForm
    success_message = 'Success: Store was created.'
    success_url = reverse_lazy('store_index')


class StoreUpdateView(BSModalUpdateView):
    model = Store
    template_name = 'store/update_store.html'
    form_class = StoreModelForm
    success_message = 'Success: Store was updated.'
    success_url = reverse_lazy('store_index')


class StoreReadView(BSModalReadView):
    model = Store
    template_name = 'store/read_store.html'


class StoreDeleteView(BSModalDeleteView):
    model = Store
    template_name = 'store/delete_store.html'
    success_message = 'Success: Store was deleted.'
    success_url = reverse_lazy('store_index')


@permission_required('main.view_store')
def stores(request):
    data = dict()
    if request.method == 'GET':
        stores = Store.objects.all()
        data['table'] = render_to_string(
            '_stores_table.html',
            {'stores': stores},
            request=request
        )
        return JsonResponse(data)


def index(request):
    return render(request, 'index.html')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'user': request.user})


@login_required
def item_delete(request):
    if request.method == 'POST':
        id = request.POST['item_id']
        pk = int(id)
        item = Item.objects.filter(id=id)
        if item is not None:
            item.delete()
        return redirect('items')


class OutletIndex(generic.ListView):
    model = Outlet
    context_object_name = 'outlets'
    template_name = 'outlets.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs


class OutletCreateView(BSModalCreateView):
    template_name = 'outlet/create_outlet.html'
    form_class = OutletModelForm
    success_message = 'Success: Outlet was created.'
    success_url = reverse_lazy('outlet_index')


class OutletUpdateView(BSModalUpdateView):
    model = Outlet
    template_name = 'outlet/update_outlet.html'
    form_class = OutletModelForm
    success_message = 'Success: Outlet was updated.'
    success_url = reverse_lazy('outlet_index')


class OutletReadView(BSModalReadView):
    model = Outlet
    template_name = 'outlet/read_outlet.html'


class OutletDeleteView(BSModalDeleteView):
    model = Outlet
    template_name = 'outlet/delete_outlet.html'
    success_message = 'Success: Outlet was deleted.'
    success_url = reverse_lazy('outlet_index')


permission_required('main.view_outlet')


def outlets(request):
    data = dict()
    if request.method == 'GET':
        outlets = Outlet.objects.all()
        data['table'] = render_to_string(
            '_outlets_table.html',
            {'outlets': outlets},
            request=request
        )
        return JsonResponse(data)


@login_required
def purchase(request):
    if request.method == 'POST':
        try:
            purchase_form = PurchaseForm(request.POST)
            barcode = request.POST['barcode']
            outlet_id = request.POST['outlet']
            store_id = request.POST['store']
            quantity = request.POST['quantity']
            transaction_type = request.POST['transaction_type']
            item = Item.objects.get(barcode=barcode)
            store = Store.objects.get(id=store_id)
            outlet = Outlet.objects.get(id=outlet_id)
            old_quantity = item.quantity
            new_quantity = int(old_quantity) + int(quantity)
            money_value = item.unit_price*int(new_quantity)
            item.quantity = new_quantity
            item.save()
            transact = Purchase(
                user=request.user, store=store, money_value=money_value, quantity=quantity, item=item, initial_quatity=old_quantity, new_quatity=new_quantity, transaction_type=transaction_type)
            transact.save()
            if transaction_type == 'stock':
                supb = SuppliedBy(outlet=outlet, store=store)
                supb.transaction = transact
                supb.save()
            messages.add_message(
                request, messages.SUCCESS, 'Transaction successful')
            return redirect('purchase')
        except Item.DoesNotExist:
            messages.add_message(
                request, messages.ERROR, 'Item corresponding to barcode was not found')
            return render(request, 'purchase.html', {'purchase_form': purchase_form})
        except Outlet.DoesNotExist:
            messages.add_message(
                request, messages.ERROR, 'Selected Outlet was not found')
            return render(request, 'purchase.html', {'purchase_form': purchase_form})
        except Store.DoesNotExist:
            messages.add_message(
                request, messages.ERROR, 'Selected Store was not found')
            return render(request, 'purchase.html', {'purchase_form': purchase_form})
    else:
        purchase_form = PurchaseForm()
        return render(request, 'purchase.html', {'purchase_form': purchase_form})


@login_required
def dispatch(request):
    if request.method == 'POST':
        try:
            dispatch_form = DispatchForm(request.POST)
            barcode = request.POST['barcode']
            outlet_id = request.POST['outlet']
            store_id = request.POST['store']
            quantity = request.POST['quantity']
            transaction_type = request.POST['transaction_type']
            item = Item.objects.get(barcode=barcode)
            store = Store.objects.get(id=store_id)
            outlet = Outlet.objects.get(id=outlet_id)
            old_quantity = item.quantity
            if int(old_quantity) < int(quantity):
                messages.add_message(
                    request, messages.ERROR, 'Transaction quantity should be less than quantity in stock')
                return render(request, 'dispatch.html', {'dispatch_form': dispatch_form})
            new_quantity = int(old_quantity)-int(quantity)
            money_value = item.unit_price*int(new_quantity)
            item.quantity = new_quantity
            item.save()
            transact = Dispatch(
                user=request.user, store=store, money_value=money_value, quantity=quantity, item=item, initial_quatity=old_quantity, new_quatity=new_quantity, transaction_type=transaction_type)
            transact.save()
            if transaction_type == 'stock':
                supb = DispatchedBy(outlet=outlet, store=store)
                supb.transaction = transact
                supb.save()
            messages.add_message(
                request, messages.SUCCESS, 'Transaction successful')
            return redirect('dispatch')
        except Item.DoesNotExist:
            messages.add_message(
                request, messages.ERROR, 'Item corresponding to barcode Not found')
            return render(request, 'dispatch.html', {'dispatch_form': dispatch_form})
        except Store.DoesNotExist:
            messages.add_message(
                request, messages.ERROR, 'Store selected not found')
            return render(request, 'dispatch.html', {'dispatch_form': dispatch_form})
        except Outlet.DoesNotExist:
            messages.add_message(
                request, messages.ERROR, 'Outlet selected not found')
            return render(request, 'dispatch.html', {'dispatch_form': dispatch_form})
    else:
        dispatch_form = DispatchForm()
        return render(request, 'dispatch.html', {'dispatch_form': dispatch_form})


class SupplierIndex(generic.ListView):
    model = Supplier
    context_object_name = 'suppliers'
    template_name = 'suppliers.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs


class SupplierCreateView(BSModalCreateView):
    template_name = 'supplier/create_supplier.html'
    form_class = SupplierModelForm
    success_message = 'Success: Supplier was created.'
    success_url = reverse_lazy('supplier_index')


class SupplierUpdateView(BSModalUpdateView):
    model = Supplier
    template_name = 'supplier/update_supplier.html'
    form_class = SupplierModelForm
    success_message = 'Success: Supplier was updated.'
    success_url = reverse_lazy('supplier_index')


class SupplierReadView(BSModalReadView):
    model = Supplier
    template_name = 'supplier/read_supplier.html'


class SupplierDeleteView(BSModalDeleteView):
    model = Supplier
    template_name = 'supplier/delete_supplier.html'
    success_message = 'Success: Supplier was deleted.'
    success_url = reverse_lazy('supplier_index')


@permission_required('main.view_supplier')
def suppliers(request):
    data = dict()
    if request.method == 'GET':
        suppliers = Supplier.objects.all()
        data['table'] = render_to_string(
            '_suppliers_table.html',
            {'suppliers': suppliers},
            request=request
        )
        return JsonResponse(data)


@permission_required('main.add_user')
def chart(request):
    if request.method == 'POST':
        period = int(request.POST['period'])
        type = request.POST['type']
        delta = timedelta(days=period)
        first = timezone.now() - delta
        print(type)
        if type == 'dispatch':
            transactions = Dispatch.objects.filter(date__gt=first)
            return render(request, 'chart.html', {'transactions': transactions})
        elif type == 'purchase':
            transactions = Purchase.objects.filter(date__gt=first)
            return render(request, 'chart.html', {'transactions': transactions})
        elif type == 'all':
            sup = Purchase.objects.filter(date__gt=first)
            dis = Dispatch.objects.filter(date__gt=first)
            transactions = list(chain(sup, dis))
            return render(request, 'chart.html', {'transactions': transactions})
        return redirect('analysis')
    elif request.method == 'GET':
        sup = Purchase.objects.all()
        dis = Dispatch.objects.all()
        transactions = list(chain(sup, dis))
        return render(request, 'chart.html', {'transactions': transactions})


@csrf_exempt
@login_required
def plot(request):
    try:
        snippet = Item.objects.all()
    except Item.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ItemSerializer(snippet, many=True)
        return JsonResponse(serializer.data, safe=False)
