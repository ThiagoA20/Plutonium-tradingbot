from .views import home_page, price, doc, faq, affiliate, login_page, resetpassword, register, dashboard, logout_page
from django.urls import path

app_name = 'tb_app'

urlpatterns = [
    path('', home_page, name='home'),
    path('price/', price, name='prices'),
    path('doc/', doc, name="doc"),
    path('faq/', faq, name="faq"),
    path('affiliate/', affiliate, name="affiliate"),
    path('login/', login_page, name="login"),
    path('logout/', logout_page, name='logout'),
    path('register/', register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('login/resetpass/', resetpassword, name='reset_password')
]