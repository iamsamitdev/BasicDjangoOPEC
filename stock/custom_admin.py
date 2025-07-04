from django.contrib.admin import AdminSite
from django.urls import path


class CustomAdminSite(AdminSite):
    site_header = "ระบบจัดการสินค้า"
    site_title = "Inventory Admin"
    index_title = "ยินดีต้อนรับสู่ระบบจัดการสินค้า"

    def get_urls(self):
        urls = super().get_urls()
        # เพิ่ม custom URLs ได้ที่นี่
        return urls


# สร้าง instance ของ custom admin site
custom_admin_site = CustomAdminSite(name='custom_admin')
