from django.urls import path
from . import views
app_name = 'Article'
urlpatterns = [
    path("",views.Display_view,name='home'),
    path("<slug:content>/",views.Detail_view,name="details"),
    path("Add-blog",views.create_view,name='add'),
    path("update/<int:index>/",views.update_view,name='update'),
    path("delete/<int:index>/",views.delete_view,name='delete'),
]
