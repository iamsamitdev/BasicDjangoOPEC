from django.contrib import admin
from django.urls import path, include

# ปรับแต่งชื่อและข้อความ Admin site
admin.site.site_header = "ระบบจัดการสินค้า"
admin.site.site_title = "Inventory Admin"
admin.site.index_title = "ยินดีต้อนรับสู่ระบบจัดการสินค้า"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('stock.urls')),
]
