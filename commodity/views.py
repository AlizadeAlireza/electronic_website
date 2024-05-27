from django.views import generic
from .models import *
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from . forms import  Order_Form
from django.db.models import Sum

class PostDetaiMobilelView(generic.DetailView):
    model = Mobile
    template_name = 'commodity/post_detail.html'
    context_object_name = 'context'


# def shoplist(request,myid):
#     detail = Product.objects.get(id=myid)
#     # offer = Product.objects.all().filter(last_price__isnull=False)
#     hot = News.objects.all().reverse().filter(season__contains='current_season').order_by('id')[:3]
#     all = Product.objects.all().order_by('-id')[:10]
#     product = Product.objects.all().order_by('-id')[:4]
#     if request.method != 'POST':
#         form = Order_Form()
#     else:
#         form = Order_Form(request.POST)
#         if form.is_valid():
#             new_form = form.save(commit=False)
#             new_form.owner = request.user
#             if Order.objects.filter(product_id=myid):
#                 return redirect('sport_news:shop-list',myid)    
#             new_form.save()
#             return redirect('sport_news:cart')
#     return render(request,'sport_news/shoplist.html',{'detail':detail,'form':form,'hot':hot,'all':all,'product':product})


# laptop


def delete_cart(request):
    query = OrderModel.objects.all()
    query.delete()
    return redirect('order.html')



@login_required
def cart(request):    
    
    orders = OrderModel.objects.filter(user=request.user).order_by('-id')
    total = OrderModel.objects.filter(user=request.user).aggregate(count=Sum('laptop__price'))
    # laptop = Laptop.objects.all().order_by('-id')[:4]
    return render(request,'commodity/order.html',{'orders':orders, 'total': total})


def PostDetaiLaptoplView(request,pk):
    context = Laptop.objects.get(id=pk)

    if request.method != 'POST':

        form = Order_Form()
    else:

        form = Order_Form(request.POST)

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            # if Laptop.objects.filter(id=pk):
            #     return redirect('commodity/post_detail.html',pk)  
            new_form.laptop = context
            new_form.save()
            # return redirect('sport_news:cart')
        
    return render(request,'commodity/post_detail.html',{'context':context,'form':form})


# class PostDetaiLaptoplView(generic.DetailView):
#     model = Laptop
#     template_name = 'commodity/post_detail.html'
#     context_object_name = 'context'
#
class PostDetailDesktopView(generic.DetailView):
    model = Desktop
    template_name = 'commodity/post_detail.html'
    context_object_name = 'context'
#
class PostDetailMotherBoardView(generic.DetailView):
    model = MotherBoards
    template_name = 'commodity/post_detail.html'
    context_object_name = 'context'

class PostDetailAccessoriesView(generic.DetailView):
    model = Accessories
    template_name = 'commodity/post_detail.html'
    context_object_name = 'context'




#----------------home----------------------
# class HomePageView(generic.ListView):
#     template_name = 'commodity/home_view.html'
#     context_object_name = 'home'
#
#     def get_queryset(self):
#         return Mobile.objects.order_by('-date_time_created')[:3]

class HomePageView(generic.TemplateView):
    template_name = 'commodity/home_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model1 = Mobile.objects.order_by('-date_time_created')[:3]
        model2 = Laptop.objects.order_by('-date_time_created')[:3]

        context['model1'] = model1
        context['model2'] = model2

        return context


#---------------------mobile---------------
class AllMobileView(generic.ListView):
    model = Mobile
    template_name = 'commodity/all_mobile.html'
    context_object_name = 'mobile_view'

    def get_queryset(self):
        return Mobile.objects.all()

class ZenfoneMobileView(generic.ListView):
    model = Mobile
    template_name = 'commodity/zenfone.html'
    context_object_name = 'zenfon_mobile'

    def get_queryset(self):
        return Mobile.objects.filter(model='Zenfone')

class RogPhoneView(generic.ListView):
    model = Mobile
    template_name = 'commodity/rog_phone.html'
    context_object_name = 'rog_phone'

    def get_queryset(slef):
        return Mobile.objects.filter(model='ROG Phone')

#--------------------laptop-----------------
class LaptopHomeView(generic.ListView):
    model = Laptop
    template_name = 'commodity/laptop_home.html'
    context_object_name = 'laptop_home'

    def get_queryset(self):
        return Laptop.objects.filter(model='Home')

class LaptopWorkView(generic.ListView):
    model = Laptop
    template_name = 'commodity/laptop_work.html'
    context_object_name = 'laptop_work'

    def get_queryset(self):
        return Laptop.objects.filter(model='Work')

class LaptopStudentView(generic.ListView):
    model = Laptop
    template_name = 'commodity/laptop_student.html'
    context_object_name = 'laptop_student'

    def get_queryset(self):
        return Laptop.objects.filter(model='Student')

class LaptopGameView(generic.ListView):
    model = Laptop
    template_name = 'commodity/laptop_game.html'
    context_object_name = 'laptop_game'

    def get_queryset(self):
        return Laptop.objects.filter(model='Game')

#--------------------desktop---------------

class MonitorView(generic.ListView):
    model = Desktop
    template_name = 'commodity/monitor.html'
    context_object_name = 'monitor_view'

    def get_queryset(self):
        return Desktop.objects.filter(model = 'Monitor')

class ProjectorsView(generic.ListView):
    model = Desktop
    template_name = 'commodity/projectors.html'
    context_object_name = 'projectors_view'

    def get_queryset(self):
        return Desktop.objects.filter(model = 'Projector')

class MiniPCView(generic.ListView):
    model = Desktop
    template_name = 'commodity/mini_pc.html'
    context_object_name = 'mini_pc'

    def get_queryset(self):
        return Desktop.objects.filter(model = 'Mini Pc')

class MotherboardIntelView(generic.ListView):
    model = MotherBoards
    template_name = 'commodity/motherboard_inteld.html'
    context_object_name = 'motherboard_inteldd'

    def get_queryset(self):
        return MotherBoards.objects.filter(model = 'intel')

#-----------------Accessories-----------------\

class KeyboardsView(generic.ListView):
    model = Accessories
    template_name = 'commodity/keyboards.html'
    context_object_name = 'keyboards_context'

    def get_queryset(self):
        return Accessories.objects.filter(model = 'Keyboard')

class MouseView(generic.ListView):
    model = Accessories
    template_name = 'commodity/Mouse.html'
    context_object_name = 'Mouse_context'

    def get_queryset(self):
        return Accessories.objects.filter(model = 'Mouse')

class HedsetView(generic.ListView):
    model = Accessories
    template_name = 'commodity/hedset.html'
    context_object_name = 'hedset_context'

    def get_queryset(self):
        return Accessories.objects.filter(model = 'Hedset')

class PowerBankView(generic.ListView):
    model = Accessories
    template_name = 'commodity/powerbank.html'
    context_object_name = 'powerbank_context'

    def get_queryset(self):
        return Accessories.objects.filter(model = 'Power Bank')


#-------------------Buy----------------
# @login_required
# class BuyView(generic.TemplateView):
#     template_name = 'commodity/buy.html'

@login_required
def BuyView(request):
    
    return render(request, 'commodity/buy.html', {})