from django.contrib import admin, auth
from django.urls import path,include
from django.views.generic import TemplateView
from Lab import views, models

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('tickets/', views.tickets_table),
    path('tickets/create/', views.create_ticket),
    path('tickets/edit/<int:id>/', views.edit_ticket),
    path('tickets/delete/<int:id>/', views.delete_ticket),
    path('planes/', views.planes_table),
    path('planes/create/', views.create_plane),
    path('planes/edit/<int:id>/', views.edit_plane),
    path('planes/delete/<int:id>/', views.delete_plane),
    #path('customers/', views.customers_table),
    path('customers/', views.CustomersClassTable.as_view()),
    path('customers/create/', views.create_customer),
    path('customers/edit/<int:id>/', views.edit_customer),
    path('customers/delete/<int:id>/', views.delete_customer),
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]