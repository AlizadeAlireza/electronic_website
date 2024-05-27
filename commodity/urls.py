from django.urls import path
from . import  views


# app_name = "commodity"
urlpatterns = [
    path('', views.HomePageView.as_view(), name='Home'),
#-------------post dtail
    path('laptop/<int:pk>', views.PostDetaiLaptoplView, name='post_detail_laptop'),
    path('mobile/<int:pk>', views.PostDetaiMobilelView.as_view(), name='post_detail_mobile'),
    path('desktop/<int:pk>', views.PostDetailDesktopView.as_view(), name='post_detail_desktop'),
    path('motherboard/<int:pk>', views.PostDetailMotherBoardView.as_view(), name='post_detail_motherboard'),
    path('accessories/<int:pk>', views.PostDetailAccessoriesView.as_view(), name='post_detail_accessories'),
#-------------mobile----------
    path('all_mobile' , views.AllMobileView.as_view(), name='all_mobile'),
    path('rog_phone' , views.RogPhoneView.as_view(), name='rog_phone'),
    path('zen_phone' , views.ZenfoneMobileView.as_view(), name='zen_phone'),
#--------------laptop-----------
    path('laptop_for_home' , views.LaptopHomeView.as_view(), name='laptop_for_home'),
    path('laptop_for_work' , views.LaptopWorkView.as_view(), name='laptop_for_work'),
    path('laptop_for_student' , views.LaptopStudentView.as_view(), name='laptop_for_student'),
    path('laptop_for_game' , views.LaptopGameView.as_view(), name='laptop_for_game'),
#-------------desktop------------
    path('monitor' , views.MonitorView.as_view(), name='monitor'),
    path('projector' , views.ProjectorsView.as_view(), name='projector'),
    path('Mini_pc' , views.MiniPCView.as_view(), name='mini_pc'),
#-----------------motherboatrd----------------------
    path('motherboard_intel' , views.MotherboardIntelView.as_view(), name='intel'),

#--------------Accessories--------------
    path('keyboards' , views.KeyboardsView.as_view(), name='keyboards'),
    path('mouse' , views.MouseView.as_view(), name='mouse'),
    path('powerbank' , views.PowerBankView.as_view(), name='powerbank'),
    path('hedset' , views.HedsetView.as_view(), name='hedset'),
    path('buy' , views.BuyView, name='buy'),

    path('cart', views.cart, name='cart'),

    path('delete-cart', views.delete_cart, name='delete-cart')

]