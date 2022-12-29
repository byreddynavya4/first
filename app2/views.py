from django.shortcuts import render

def first1(request):
    d={'name':'Navya Byreddy'}
    
    return render(request,'first1.html',d)

