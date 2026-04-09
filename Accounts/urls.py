from django.urls import path
from . import views
app_name = 'Accounts'
urlpatterns =[
    path('login/',views.login_view,name='logger'),
    path('Register/',views.register_view,name='Register'),
    path('logout/',views.logout_view,name='logout'),
]