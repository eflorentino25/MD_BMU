from django.shortcuts import render

# Create your views here.


def tv_main(request):
    return render(request, "tv/tv_maker.html",context={})