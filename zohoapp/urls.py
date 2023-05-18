from django.urls import path,include
from.import views
from .views import save_data

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('base', views.base, name='base'),
    path('logout', views.logout, name='logout'),
    path('view_profile', views.view_profile, name='view_profile'),
    path('edit_profile/<pk>', views.edit_profile, name='edit_profile'),
    path('itemview',views.itemview,name='itemview'),
    path('additem',views.additem,name='additem'),
    path('add',views.add,name='add'),
    path('add_account',views.add_account,name='add_account'),
    path('detail/<int:id>',views.detail,name='detail'),
    path('edititem/<int:id>',views.edititem,name='edititem'),
    path('edit_db/<int:id>',views.edit_db,name='edit_db'),
    path('Action/<int:id>',views.Action,name='Action'),
    path('cleer/<int:id>',views.cleer,name='cleer'),
    path('add_unit',views.add_unit,name='add_unit'),
    path('sales',views.add_sales,name='add_sales'),
    path('recurringhome',views.recurringhome,name='recurringhome'),
    path('add_expense',views.add_expense,name='add_expense'),
    path('recurringbase',views.recurringbase,name='recurringbase'),
    path('show_recurring/<int:expense_id>/', views.show_recurring, name='show_recurring'),
    path('expense_details', views.expense_details, name='expense_details'),
    path('vendor/',views.vendor,name='vendor'),
    path('add_vendor/',views.add_vendor,name='add_vendor'),
    path('edit_expense/<int:expense_id>/', views.edit_expense, name='edit_expense'),
    path('newexp/',views.newexp,name='newexp'),
    path('save-data/', save_data, name='save_data'),
    path('get-account-names/', views.get_account_names, name='get_account_names'),
    path('profileshow',views.profileshow,name='profileshow'),
    path('add_customer',views.add_customer,name='add_customer'),
    path('entr_custmr',views.entr_custmr,name='entr_custmr'),
    path('payment_term',views.payment_term,name='payment_term'),
    path('get_customer_names', views.get_customer_names, name='get_customer_names'),


]