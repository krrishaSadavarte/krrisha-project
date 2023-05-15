from .views  import *
from django.urls import path,include

urlpatterns = [
path('', index, name='index'),
path('about/',about,name='about'),
path('contact/',contact,name='contact'),
path('register/',register,name='register'),
path('registersubmit/',reg_submit,name='register_submit'),
path('otp/',otp,name='otp'),
path('login/',login,name='login'),
path('logout/',log_out,name='logout'),
path('add/',add,name='add'),
path('my_account/',my_account,name='my_account'),
path('dessert_drinks/',dessert_drinks,name='dessert_drinks'),
path('veg/',vegetarian,name='veg'),
path('search/',search,name='search'),
path('save_changes/',save_changes,name='save_changes'),
path('homepage/',homepage,name='homepage'),
path('homepage/paymenthandler/',paymenthandler,name='paymenthandler'),
path('payment/',payment,name='payment')



]   