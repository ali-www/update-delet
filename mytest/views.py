from django.http import request
from django.shortcuts import render,redirect,get_object_or_404
#from django.http import  HttpResponse
from .models import Po
from .form import Poform , FormSignup
from django.contrib.auth import login as auth_login
from datetime import datetime
from django.core.paginator import Paginator
# Create your views here.

def forms_html(request,f_h):
    F_d = Po.objects.get(pk=f_h)
    form = Poform(instance=F_d)
    if request.method == 'POST':
        form = Poform(request.POST,request.FILES,instance=F_d)
        if form.is_valid():
            form.save()
            return redirect('show' , f_h )
    
    context = {'form':form}
    return render(request,'home.html',context)
#=================================================================
def de_let(request,dl_d):
    de_let = Po.objects.get(pk=dl_d)
   

    if request.method == 'POST':
        de_let.delete()
      
        return redirect('asd' )
     

    return render(request,'de_let.html',{'de_let': de_let})    

#==================================================================== detials 
def show(req,id_show):
    show = get_object_or_404(Po,pk=id_show)
    return render(req,'show.html',{'show':show})


#///////////////////////////////////////////////////////////////// all thing post 
def asd(requset):
    
    if requset.method == 'GET':
        
        po = Po.objects.all()
        return render(requset,'asd.html',{'po':po}) 
      

  
#====================================================================
def home(requset):
    form = Poform()
    if requset.method == 'POST':
      form = Poform(requset.POST,requset.FILES)
      if form.is_valid():
            form.save()
            return redirect('asd')
    wkt =  datetime.now()       
            
    return render(requset,'home.html',{'form':form ,'wkt':wkt})

#==================================================================== side ==
def side(req): #========= try
    return render(req,'side.html')    


#===================================================================0   
def signup(requset):
    form = FormSignup()
    if requset.method == 'POST':
        form = FormSignup(requset.POST)
        if form.is_valid():
            user = form.save()
            auth_login(requset,user)
            return redirect('home')
           
        

    return render(requset,'signup.html',{'form':form})    