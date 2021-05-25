from django.contrib import admin
from main.models import User, Till, Store, Item, Outlet,  Purchase, Dispatch, SuppliedBy, Invoice, Recipt,Supplier


models = [Till,User, Store, Item, Outlet,
          Purchase, Dispatch, SuppliedBy, Invoice, Recipt, Supplier]
admin.site.register(models)
    