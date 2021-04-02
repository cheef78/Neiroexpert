from django.shortcuts import render
from damage import damage

# Create your views here.

def main (request):
    return render(request, 'mainapp/index.html' )

def damage_neiro_calculate (request):
    # project_path = r'C:\Users\suslo\Google Диск\2,5 млрд\Neiroexpert\Neiroexpert_WEb\projekts'
    # project_number = 1
    # files_path = project_path + str('\\') + str(project_number)
    # result = damage (project_path, project_number)
    result = "Тут отражается результат выполнения расчетов сил, напряжений и повреждаемости по нейросетевым моделям"
    content = {
        'fuction_result':result 
    }
    return render(request, 'mainapp/ok_form.html', content )

def damage_metoda_calculate (request):
        # project_path = r'C:\Users\suslo\Google Диск\2,5 млрд\Neiroexpert\Neiroexpert_WEb\projekts'
    # project_number = 1
    # files_path = project_path + str('\\') + str(project_number)
    # result = damage (project_path, project_number)
    result = "Тут отражается результат выполнения расчетов сил, напряжений и повреждаемости по методике РЖД 2706р "
    content = {
        'fuction_result':result 
    }
    return render(request, 'mainapp/ok_form.html', content )