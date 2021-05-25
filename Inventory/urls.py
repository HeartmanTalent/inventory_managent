from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import path, include
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # auth
    path('signup/', permission_required('main.add_user')
         (views.SignUpView.as_view()), name='signup'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path("logout/", login_required(auth_views.LogoutView.as_view()), name="logout"),

    # store urls
    path('store/index', permission_required('main.view_store')
         (views.Index.as_view()), name='store_index'),
    path('store/create/', permission_required('main.add_store')
         (views.StoreCreateView.as_view()), name='create_store'),
    path('store/update/<int:pk>',
         permission_required('main.change_store')(views.StoreUpdateView.as_view()), name='update_store'),
    path('store/read/<int:pk>', permission_required('main.view_store')
         (views.StoreReadView.as_view()), name='read_store'),
    path('store/delete/<int:pk>',
         permission_required('main.delete_store')(views.StoreDeleteView.as_view()), name='delete_store'),
    path('stores/', views.stores, name='stores'),

    # oulet urls
    path('outlet/index', permission_required('main.view_outlet')
         (views.OutletIndex.as_view()), name='outlet_index'),
    path('outlet/create/', permission_required('main.add_outlet')
         (views.OutletCreateView.as_view()), name='create_outlet'),
    path('outlet/update/<int:pk>',
         permission_required('main.change_outlet')(views.OutletUpdateView.as_view()), name='update_outlet'),
    path('outlet/read/<int:pk>', permission_required('main.view_outlet')
         (views.OutletReadView.as_view()), name='read_outlet'),
    path('outlet/delete/<int:pk>',
         permission_required('main.delete_outlet')(views.OutletDeleteView.as_view()), name='delete_outlet'),
    path('outlets/', views.outlets, name='outlets'),

    # users urls
    path('user/index', permission_required('main.view_user')
         (views.UserIndex.as_view()), name='user_index'),
    path('user/update/<int:pk>',
         permission_required('main.change_user')(views.UserUpdateView.as_view()), name='update_user'),
    path('user/read/<int:pk>', permission_required('main.view_user')
         (views.UserReadView.as_view()), name='read_user'),
    path('user/delete/<int:pk>',
         permission_required('main.delete_user')(views.UserDeleteView.as_view()), name='delete_user'),
    path('user/', views.users, name='users'),

    # item urls
    path('item/index', permission_required('main.view_item')
         (views.ItemIndex.as_view()), name='item_index'),
    path('item/create/', permission_required('main.add_item')
         (views.ItemCreateView.as_view()), name='create_item'),
    path('item/update/<int:pk>',
         permission_required('main.change_item')(views.ItemUpdateView.as_view()), name='update_item'),
    path('item/read/<int:pk>', permission_required('main.view_item')
         (views.ItemReadView.as_view()), name='read_item'),
    path('item/delete/<int:pk>',
         permission_required('main.delete_item')(views.ItemDeleteView.as_view()), name='delete_item'),
    path('items/', views.items, name='items'),

    # supplier urls
    path('supplier/index', permission_required('main.view_supplier')
         (views.SupplierIndex.as_view()), name='supplier_index'),
    path('supplier/create/', permission_required('main.add_supplier')(views.SupplierCreateView.as_view()),
         name='create_supplier'),
    path('supplier/update/<int:pk>',
         permission_required('main.change_supplier')(views.SupplierUpdateView.as_view()), name='update_supplier'),
    path('supplier/read/<int:pk>',
         permission_required('main.view_supplier')(views.SupplierReadView.as_view()), name='read_supplier'),
    path('supplier/delete/<int:pk>',
         permission_required('main.delete_supplier')(views.SupplierDeleteView.as_view()), name='delete_supplier'),
    path('suppliers/', views.suppliers, name='suppliers'),

    # ops
    path('purchase/', views.purchase, name='purchase'),
    path('dispatch/', views.dispatch, name='dispatch'),
    path('analysis', views.chart, name='analysis'),

    # chart
    path('plot/', views.plot, name='plot'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
