from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from projektapp.models import Projekt
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.template.loader import render_to_string
from django.http import JsonResponse
from projektapp.forms import ProjektCreateForm
from authapp.models import ProjektUser

# @login_required
# def projekt_edit(request, pk, quantity):

#     if request.is_ajax():
#         quantity = int(quantity)
#         new_basket_item = Basket.objects.get(pk=int(pk))

#         if quantity > 0:
#             new_basket_item.quantity = quantity
#             new_basket_item.save()
#         else:
#             new_basket_item.delete()
#         basket_items = Basket.objects.filter(user=request.user).order_by('product__category')
        
#         content = {
#         'basket_items': basket_items,
#         }

#         result = render_to_string('basketapp/includes/inc_basket_list.html',content)
#         return JsonResponse({'result': result})


@login_required
def projekt(request):
    title = 'Проекты'
    projekt_items = Projekt.objects.filter(user=request.user).order_by('add_datetime')
    content = {
    'title': title,
    'projekt_items': projekt_items,
    }
    return render(request, 'projektapp/projekt.html', content)

# @login_required
# def projekt_remove(request, pk):
#     basket_record = get_object_or_404(Basket, pk=pk)
#     basket_record.delete()
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def projekt_create(request):
    title = 'проект/создание'
    print (request.user)
    if request.method == 'POST':
        projekt_create_form = ProjektCreateForm(request.POST, request.FILES,initial={'Username': request.user,} )
        if projekt_create_form.is_valid():
            projekt_create_form.save()
            return HttpResponseRedirect(reverse('projekt:view'))
          
    else:
        projekt_create_form = ProjektCreateForm(initial={'Username': request.user,})
    content = {'title': title, 'update_form': projekt_create_form}
    return render(request, 'projektapp/projekt_update.html', content)




# @login_required
# def projekt_add (request):
#     projekt = Projekt.objects.filter(user=request.user).first()
    
#     if 'login' in request.META.get('HTTP_REFERER'):
#         return HttpResponseRedirect(reverse('products:product', args=[pk]))
    
#     if not projekt:
#         projekt = Projekt(user=request.user)
#     basket.quantity += 1
#     basket.save()
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# def projekt_create (request):
#     project_path = r'C:/Users/suslo/Google Диск/2,5 млрд/Neiroexpert/Neiroexpert_WEb/projekts'
#     project_number = 3
#     damage = ForceNeiroCalc(project_path, project_number)
#     result = damage.damage()
#     pic_names = ('Mean_F_vertR_kN', 'Mean_F_vertL_kN', 'Mean_F_vert_kN', 'sigma_F_vertR_kN','sigma_F_vertL_kN','sigma_F_vert_kN','Mean_F_sideR_kN', 'Mean_F_sideL_kN', 'Mean_F_side_kN','sigma_F_sideR_kN','sigma_F_sideL_kN', 'sigma_F_side_kN', 'Mean_Hp_kN', 'sigma_Hp_kN','MeanP1NarkPa', 'RmsP1NarkPa', 'MeanP1VnrkPa', 'RmsP1VnrkPa','MeanP2NarkPa', 'RmsP2NarkPa', 'MeanP2VnrkPa', 'RmsP2VnrkPa', 'Mean_nar_krom_MPa', 'RMS_nar_krom_MPa', 'Mean_vntr_krom_MPa',  'RMS_vntr_krom_MPa','Mean_osev_MPa', 'RMS_osev_MPa', 'mean_F_shpal_vert_kN','sigma_F_shpal_vert_kN','mean_F_shpal_side_kN','sigma_F_shpal_side_kN','mean_F_ballast_kPa', 'sigma_F_ballast_kPa', 'mean_F_OPZP_kPa', 'sigma_F_OPZP_kPa', 'd_rail_MPa^Xrail', 'd_fast_kN^Xfast', 'd_tie_kN^Xtie', 'd_shkol_kN^Xshkol', 'd_prof_kPa^Xprof', 'd_plan_kN^Xplan', 'd_ball_kPa^Xball', 'd_opzp_kPa^Xopzp')
#     desc_names = ('Условные обозначения:', 'Mean - среднее значение', 'RMS, sigma - С.К.О.значения', 'R, L - правый левый рельс/сторона', 'F_vert - вертикальная сила, действующая от колеса на рельс,кН', 'F_side - боковая сила, действующая о колеса на рельс, кН',  'Hp - рамная сила, передающаяся на рельсошпальную решетку, кН', 'P1Nar/P1Vnr - контактное напряжение на поверхности катания рельса (наружная/внутренняя нить), kПa', 'P2Nar/P2Vnr - контактное напряжение на боковой грании рельса (наружная/внутренняя нить), kПa ','nar_krom/vntr_krom/osev - напряжения в рельсах, MПa (наружная кромка/внутренняя кромка/ось рельса)', 'F_shpal_vert/F_shpal_side - вертикальная/горизонтальная силы, действующие на шпалу, кН','F_ballast/F_OPZP - напряжения в балласте под шпалой/на основной площадке зем.полотна, кПа','Значения повреждаемостией от 1 цикла нагружения для расчета деградации:', 'd_rail_MPa/d_fast_kN/d_tie_kN/d_shkol_kN', 'рельсов/скреплений/шпал/ширины колеи', 'd_prof_kPa/d_plan_kN/d_ball_kPa/d_opzp_kPa', 'отступления по профилю/отступления в плане/загрязненность балласта/неисправности основной площадки')
     
#     pic_full_names = []
#     for pic in pic_names:
#         pic_full_name = "/projekts/" + str(project_number) + "/graf/" + pic + ".png"
#         pic_full_names.append(pic_full_name)
    
#     content = {
#         'fuction_result':result,
#         'pic_names':pic_full_names,
#         'project_number':project_number,
#         'desc_names':desc_names, 
#     }
#     return render(request, 'mainapp/ok_form.html', content )