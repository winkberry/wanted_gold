from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('gold_auth.urls')),  # gold_auth 앱의 URL 추가
]