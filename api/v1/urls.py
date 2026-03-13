from django.urls import path, include

urlpatterns = [
    path('users/', include('api.v1.views.user_urls')), 
]
