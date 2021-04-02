from django.shortcuts import render

# Create your views here.

def main (request):
    name = request.GET.get('name')
    print(name)
    click = request.GET.get('click')
    print(click)
    if name == 'calculation' and click == 'true':
        print('Command_read_OK')
    return render(request, 'mainapp/index.html' )

def damage_calculate (request):

    result = "Тут отражается результат выполнения функции"
    content = {
        'fuction_result':result
    }
    return render(request, 'mainapp/ok_form.html', content )



