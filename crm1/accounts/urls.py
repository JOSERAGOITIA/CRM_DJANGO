from os import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name="home"),
    path('register',views.registerPage,name='register'),
    path('login',views.loginPage,name='login'),
    path('logout',views.logoutUser,name='logout'),
    path('user/',views.userPage,name='user-page'),
    path('account/',views.accountSettings,name="account"),
    #('products/',views.products,name="products"),
    path('member/',views.member,name="member"),
    path('mentor/',views.mentor,name="mentor"),
    path('customer/<str:pk_test>/',views.customer,name="customer"),
    path('update_order/<str:pk_update>/',views.updateorder,name="update_order"),
    path('delate_order/<str:pk_delate>/',views.delateorder,name="delate_order"),
    path('creatnew_order/<str:pk_creatorder>/',views.creatnewordercu,name="creatnew_order"),
 
    
   



]
