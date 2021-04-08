from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from projektapp.models import Projekt
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.template.loader import render_to_string
from django.http import JsonResponse
from projektapp.forms import ProjektCreateForm, ProjektEditForm 
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

@login_required
def projekt_load(request, pk):
    title = 'Проекты'
    projekt_item = get_object_or_404(Projekt, pk=pk)
    
    print (projekt_item, 'воть')
    content = {
              'title': title,
              'item': projekt_item,
              }
    return render(request, 'mainapp/index.html', content)  



def projekt_update(request, pk):
    title = 'проекты/редактирование'
    edit_category = get_object_or_404(Projekt, pk=pk)
    if request.method == 'POST':
        edit_form = ProjektEditForm(request.POST, request.FILES, instance=edit_category)
        if edit_form.is_valid():
            # edit_form.save()
            # title = 'Проекты'
            # projekt_items = Projekt.objects.filter(user=request.user).order_by('add_datetime')
            # content = {
            # 'title': title,
            # 'projekt_items': projekt_items,
            # }
            # return render(request, 'projektapp/projekt.html', content))
            edit_form.save()
            return HttpResponseRedirect(reverse('projekt:view'))
    else:
        edit_form = ProjektEditForm(instance=edit_category)

    content = {'title': title, 'update_form': edit_form}

    return render(request, 'projektapp/projekt_update.html', content)



@login_required
def projekt_remove(request, pk):
    projekt_record = get_object_or_404(Projekt, pk=pk)
    projekt_record.delete()
    title = 'Проекты'
    projekt_items = Projekt.objects.filter(user=request.user).order_by('add_datetime')
    content = {
    'title': title,
    'projekt_items': projekt_items,
    }
    return render(request, 'projektapp/projekt.html', content)

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

