from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('create/', views.ClientCreateView.as_view(), name='create_client'),
    path('update/<int:pk>', views.ClientUpdateView.as_view(), name='update_client'),
    path('read/<int:pk>', views.ClientDetailView.as_view(), name='read_client'),
    path('delete/<int:pk>', views.ClientDeleteView.as_view(), name='delete_client'),
    path('user/read/<int:pk>', views.UserDetailView.as_view(), name='read_user'),
]