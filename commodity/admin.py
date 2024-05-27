from django.contrib import admin
from commodity.models import *


class CommodityAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'model')
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')

admin.site.register(Mobile , CommodityAdmin)
admin.site.register(Laptop , CommodityAdmin)
admin.site.register(MotherBoards , CommodityAdmin)
admin.site.register(Desktop , CommodityAdmin)
admin.site.register(Accessories , CommodityAdmin)
admin.site.register(ContactUs , ContactUsAdmin)
admin.site.register(OrderModel )
