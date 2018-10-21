from django.urls import path, include
from .views import CreateAccountView, ListAccountView, Logout
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', CreateAccountView.as_view(), name='create-account'),
    path('login/', obtain_auth_token, name='login'),
    path('account/', ListAccountView.as_view(), name='list-account'),
    path('logout/', Logout.as_view(), name='logout'),
]