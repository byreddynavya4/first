from django.shortcuts import render

def first(request):
    d={'name':'Navya'}
    return render(request,'first.html',d)
