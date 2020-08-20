from django.shortcuts import render
from .models import dest

# Create your views here.
def home(request):

    dest1 =dest()
    dest1.name="Kolkata"
    dest1.price=100
    dest1.image="destination_1.jpg"
    dest1.desc="City of joy"
    dest1.flag=False

    dest2= dest()
    dest2.name = "Bihar"
    dest2.price = 120
    dest2.image = "destination_2.jpg"
    dest2.desc = "sasural"
    dest2.flag=True

    dest3 = dest()
    dest3.name = "Mumbai"
    dest3.image = "destination_3.jpg"
    dest3.price = 200
    dest3.desc = "City never sleep"
    dest3.flag = False

    dests =[dest1,dest2,dest3]
    return render(request,'index.html',{'dests': dests})