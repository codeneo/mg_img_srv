from django.urls import path, include

urlpatterns = [
    path('v1/', include(('accounts.api.v1.urls', 'accounts-api-v1'), namespace='v1')),
]