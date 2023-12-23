
from django.contrib import admin
from django.urls import path
from ais import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login,name='login'),
    path('login',views.login,name='login'),
    path('go for login',views.go_for_login,name="go_for_logins"),
    ############### ADMIN #############
    path('admin_page',views.admin_page),
    path("all_ais_details",views.all_ais_details),
    path('approved_ais',views.approved_ais),
    path('approved_ais_1',views.approved_ais_1),
    path('add',views.add_product),
    path('ped_page',views.ped_page),
    path('ped_approve/<product_part_number>',views.ped_approve),
    path('ped_reject/<product_part_number>',views.ped_reject),
    path('reject_status',views.reject_satus),
    path('reject_status_1',views.reject_status_1),
    path('update/<product_part_number>',views.update),
    path('delete/<id>',views.delete),
    path("search_Admin",views.search_Admin),
    
    ############### PRODUCTION #############
    path('production_page',views.production_page),
    path('production_approve/<product_part_number>',views.production_approve),
    path('reject_production/<product_part_number>',views.reject_production),
    path('all_ais_1',views.ais_status_1),
   
      ############### HOD #############
    path('hod_page',views.hod_page,name='hod_page'),
    path('hod_approve/<product_part_number>',views.hod_approve),
    path("hod_reject/<product_part_number>",views.hod_reject),
    path("all_ais_details_hod",views.all_ais_details_hod),
    path("approved_ais_hod",views.approved_ais_hod),
    path("reject_status_hod",views.reject_status_hod),
    path("search_hod",views.search_hod),
    path("update_hod/<product_part_number>",views.update_hod),
    path("delete_hod/<id>",views.delete_hod),
    ############### QUALITY #############
     path('quality_page',views.quality_page),
    path('quality_approve/<product_part_number>',views.quality_approve),
    path('quality_reject/<product_part_number>',views.quality_reject),
    path("all_ais_2",views.all_ais_2),
    path("approved_ais_2",views.approved_ais_2),
    path("reject_status_2",views.reject_status_2),
     ############### OPARATOR #############
     path("oparator_search",views.update_to_live),
     path('search',views.update_to_lives),
     path('controll_copy/<product_part_number>',views.controll_copy),
     ############### FORGOT PASSWORD #############
     path("forgot",views.forgot),
     path("check",views.check),
     path("reset/<id>",views.reset),
     ############## NEW USER ################
     path("type of user",views.user_type),
     path("Admin_new_user",views.Admin_new_user),
     path("production_new_user",views.production_new_user),
     path('quality_new_user',views.quality_new_user),
     path("hod_new_user",views.hod_new_user),
     path("operator_new_user",views.operator_new_user),
     ############### TRAIAL ############
     path("traial",views.traial),
     
]
