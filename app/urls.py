from django.urls import path
from .views import RegisterView
from .views import EditView
from .views import ListView
from .views import MyDetailView
from .views import MyDeleteView
from .views import MyLoginView
from .views import MyLogoutView


urlpatterns = [
    path('', ListView.as_view(), name='list'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('edit/<int:pk>', EditView.as_view(), name='edit'),
    path('detail/<int:pk>', MyDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', MyDeleteView.as_view(), name='delete'),
]
