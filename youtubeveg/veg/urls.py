from django.urls import path
from . import views

urlpatterns = [
    path('', views.receipes, name="reciepe"),
    path('update/<int:id>/', views.update_recipe, name="update_recipe"),
    path('delete/<int:id>/', views.delete_recipe, name="delete_recipe"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.register_view, name="register"),
]
