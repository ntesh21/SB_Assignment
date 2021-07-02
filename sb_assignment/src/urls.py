from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('data', views.list_data, name='data'),
    path('details/<int:id>', views.data_detail, name='details'),
    path('save/data/', views.save_db),
]


