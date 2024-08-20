from django.shortcuts import render, HttpResponse


modules = {'tv':'Criador de tabelas verdade' ,
           'exe':'Exercício de tabelas verdade',
            'venn':'Lógica com diagrama de Venn' }


# Create your views here.
def home(request):
    # return HttpResponse("hi") 
    return render(request, 'home/index.html', context= {
        "modules" : modules
    })