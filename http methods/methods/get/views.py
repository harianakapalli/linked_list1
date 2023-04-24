from django.shortcuts import render

# Create your views here.
"""
def getmethod(request):
    
    firstname=request.GET.get("fname") if request.GET.get("fname") else "hari"
    lastname=request.GET.get("lname") if request.GET.get("lname") else "ravi"
    fullName=firstname+" "+lastname
    context={"fullName": fullName}
    return render(request,"get.html",context)
"""
def postmethod(request):
    number1=request.POST.get("num1") if request.POST.get("num1") else 0
    num1=int(number1)
    number2=request.POST.get("num2") if request.POST.get("num2") else 0
    num2=int(number2)
    product=num1*num2
    context={"product":product}
    return render(request,"get.html",context)
    