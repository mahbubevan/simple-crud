from django.urls import path
from . import views

app_name = 'restapi'

urlpatterns = [
    path('',views.index,name='index'),
    path('create/',views.create,name='create'),
    path('store/',views.store,name='store'),
    path('edit/<int:book_id>',views.edit,name='edit'),
    path('update/',views.update,name='update'),
    path('delete/<int:book_id>',views.delete,name='delete'),
]
