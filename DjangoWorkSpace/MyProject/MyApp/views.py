from django.shortcuts import render,redirect
from django.http import HttpResponse
from MyApp.models import Contact
from MyApp.models import About, MenuItem, Booking
from MyApp.models import Booking
from .forms import SignupForm

def index(request):
    return render(request, 'MyApp/index.html')


# Create your views here.
def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        en=Contact(name=name,email=email,message=message)
        en.save()
    return render(request,"MyApp/contact.html")

def about(request):
    return render(request, 'MyApp/about.html')

def menu(request):
    return render(request, 'MyApp/menu.html')

def book(request):
    if request.method == 'POST':
        nm = request.POST.get('nm')  # Name
        ph = request.POST.get('ph')   # Phone number
        em = request.POST.get('em')  # Email
        da = request.POST.get('da')  # Date
        gu = request.POST.get('gu')  # Number of guests

        if gu:
            gu = int(gu)
        en = Booking(nm=nm, em=em, ph=ph, da=da, gu=gu)
        en.save()

    return render(request, "MyApp/book.html")

def signup(request):
    if request.method=='GET':
        sform=SignupForm()
        return render(request,"MyApp/signup.html",{'sform':sform})
    if request.method=='POST':
        sform=SignupForm(request.POST)
        user=sform.save()
        user.set_password(user.password)
        sform=SignupForm()
        mydict={'msg':'Registration Success...','sform':sform}
        return render(request,"MyApp/signup.html",context=mydict)
