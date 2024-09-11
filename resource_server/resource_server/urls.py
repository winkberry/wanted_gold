from django.contrib import admin
from django.urls import path, include  # include를 추가합니다

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('orders.urls')),  # orders 앱의 URL을 포함시킵니다
]
