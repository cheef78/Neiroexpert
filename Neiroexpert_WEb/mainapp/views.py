from django.shortcuts import render

# Create your views here.

def main (request):
    return render(request, 'mainapp/index.html' )

def damage_calculate (request):
    result = "Тут отражается результат выполнения функции"
    content = {
        'fuction_result':result 
    }
    return render(request, 'mainapp/ok_form.html', content )