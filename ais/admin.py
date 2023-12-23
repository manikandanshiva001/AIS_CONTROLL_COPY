from django.contrib import admin
from ais.models import ais,admin_login,production_Approve,production_login,quality_login,PED_Approve,QUALITY_Approve,hod_login,oparator_login,Hod_Approve
from ais.models import PED_Reject,QUALITY_Reject,Hod_Reject,production_Reject
# Register your models here.
class aisAdmin(admin.ModelAdmin):
    list=["product_name","product_part_number",'ais',"ApprovedByProduction",'ApprovedByQUA','ApprovedByHod',"reject"]
class admin_loginAdmin(admin.ModelAdmin):
    list=['user','password','mail']
class production_loginAdmin(admin.ModelAdmin):
    list=['user','password','mail']
class quality_loginAdmin(admin.ModelAdmin):
    list=['user','password','mail']
class PED_ApproveAdmin(admin.ModelAdmin):
    list=["product_part_number"]
class production_ApproveAdmin(admin.ModelAdmin):
    list=["product_part_number"]
class QUALITY_ApproveAdmin(admin.ModelAdmin):
    list=["product_part_number"]
class Hod_ApproveAdmin(admin.ModelAdmin):
    list=["product_part_number"]
class oparator_loginAdmin(admin.ModelAdmin):
    list=['user','password','mail']
class hod_loginAdmin(admin.ModelAdmin):
    list=['user','password','mail']

class PED_RejectAdmin(admin.ModelAdmin):
    list=["product_part_number"]
class production_RejectAdmin(admin.ModelAdmin):
    list=["product_part_number"]
class QUALITY_RejectAdmin(admin.ModelAdmin):
    list=["product_part_number"]
class Hod_RejectAdmin(admin.ModelAdmin):
    list=["product_part_number"]

admin.site.register(ais,aisAdmin)
admin.site.register(admin_login,admin_loginAdmin)
admin.site.register(production_login,production_loginAdmin)
admin.site.register(quality_login,quality_loginAdmin)
admin.site.register(PED_Approve,PED_ApproveAdmin)
admin.site.register(QUALITY_Approve,QUALITY_ApproveAdmin)
admin.site.register(hod_login,hod_loginAdmin)
admin.site.register(oparator_login,oparator_loginAdmin)
admin.site.register(Hod_Approve,Hod_ApproveAdmin)
admin.site.register(production_Approve,production_ApproveAdmin)
admin.site.register(production_Reject,production_RejectAdmin)
admin.site.register(PED_Reject,PED_RejectAdmin)
admin.site.register(QUALITY_Reject,QUALITY_RejectAdmin)
