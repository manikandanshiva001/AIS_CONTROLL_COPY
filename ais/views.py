from django.shortcuts import render,redirect,HttpResponse
from ais.models import ais,admin_login,production_login,quality_login,PED_Approve,QUALITY_Approve,hod_login,oparator_login,Hod_Approve
from ais.forms import aisForm,admin_loginForm,pdiForm,production_loginForm,quality_loginForm,hod_loginForm,operator_loginForm
from ais.models import production_Approve,PED_Reject,production_Reject,QUALITY_Reject,Hod_Reject,pdi
from localStoragePy import localStoragePy
import datetime

localStorage = localStoragePy('AIS_Controller', 'json')


# Create your views here.
##################  PED APPROVE ################
def ped_page(request):
    a=ais.objects.all()
    list_one=ais.objects.all()
    list_two=ais.objects.filter(ApprovedByped=True)
    one_not_two = set(list_one).difference(list_two)
    return render(request,'ped_page.html',{'g':one_not_two})
def ped_approve(request,product_part_number):
    
    g = ais.objects.all()
    
    
    your_datetime = datetime.date.today()
    date=your_datetime
   
    a=ais.objects.filter(product_part_number=product_part_number).update(ApprovedByped = True, ApprovedBypedUser=localStorage.getItem("user_name"),
                                                                         ApprovedBypeddate=date)
    data = ais.objects.get(product_part_number=product_part_number)
    data2 = PED_Approve(product_part_number = data)
    data2.save()
    return redirect('/ped_page')

        
        #update to database
        #product_list = request.POST.getlist('boxes')
      
       # tem=0
        #for i in product_list:
       
    
             
   
    
def ped_reject(request,product_part_number):
    g = ais.objects.all()
    data = ais.objects.get(product_part_number=product_part_number)
    if request.method == 'POST':
        
        command=request.POST["command"]
        a=ais.objects.filter(product_part_number=product_part_number).update(RejectByPedcommand=command)
        data2 = PED_Reject(product_part_number = data,command=command)
        data2.save()
        
        #update to database
        product_list = request.POST.getlist('boxes')
      
        tem=0
        for i in product_list:
            a=ais.objects.filter(product_part_number=i).update(RejectByPed = True)
            tem=1
            if tem==1:
                return redirect('/ped_page')
             
    else:
        return render(request,'reject.html',{'data':data})


##########    PRODUCTION APROVE   ####################

def production_page(request):
    a=ais.objects.all()
    list_one=ais.objects.all()
    list_two=ais.objects.filter(ApprovedByped=True,ApprovedByProduction=False)
    one_not_two = set(list_one).difference(list_two)
    return render(request,'production_page.html',{'g':list_two})
def approved_ais_1(request):
    a=ais.objects.filter(ApprovedByHod=True)
    
    return render(request,'approved_ais_1.html',{'a':a})
def reject_status_1(request):
    list_one=ais.objects.all()
    list_two=ais.objects.filter(ApprovedByQUA=True,ApprovedByProduction=True,ApprovedByped=True,ApprovedByHod=True)
    one_not_two = set(list_one).difference(list_two)
    return render(request,'reject_status_1.html',{'a':one_not_two})
    
def production_approve(request,product_part_number):
    g = ais.objects.all()

    your_datetime = datetime.date.today()
    date=your_datetime
    a=ais.objects.filter(product_part_number=product_part_number).update(ApprovedByProduction = True,ApprovedByProductionUser=localStorage.getItem("user_name"),
                                                                         ApprovedByProductiondate=date)
    data = ais.objects.get(product_part_number=product_part_number)
    data2 = production_Approve(product_part_number = data)
    data2.save()
    return redirect('/production_page')
             
   
    
def reject_production(request,product_part_number):
    g = ais.objects.all()
    data = ais.objects.get(product_part_number=product_part_number)
    if request.method == 'POST':
        command=request.POST["command"]
        a=ais.objects.filter(product_part_number=product_part_number).update(RejectdByProductioncommand=command)
        data2 = production_Reject(product_part_number = data,command=command)
        data2.save()
        
        #update to database
        product_list = request.POST.getlist('boxes')
      
        tem=0
        for i in product_list:
            a=ais.objects.filter(product_part_number=i).update(RejectdByProduction = True)
            tem=1
            if tem==1:
                return redirect('/production_page')
             
    else:
        return render(request,'reject.html',{'data':data})
##########    QUALITY APROVE   ####################
def quality_page(request):
    list_one=ais.objects.all()
    list_two=ais.objects.filter(ApprovedByQUA=False,ApprovedByped=True,ApprovedByProduction=True)
    one_not_two = set(list_one).difference(list_two)
    return render(request,'quality_page.html',{'g':list_two})
def approved_ais_2(request):
    a=ais.objects.filter(ApprovedByHod=True)
    
    return render(request,'approved_ais_2.html',{'a':a})
def reject_status_2(request):
    list_one=ais.objects.all()
    list_two=ais.objects.filter(ApprovedByQUA=True,ApprovedByProduction=True,ApprovedByped=True,ApprovedByHod=True)
    one_not_two = set(list_one).difference(list_two)
    return render(request,'reject_status_2.html',{'a':one_not_two})
def add_pdi(request):
    fo=pdiForm
    if request.method=="POST":
        s=pdiForm(request.POST,request.FILES)
        if s.is_valid():
            s.save()
            return redirect("/all_pdi")
    return render(request,'pdi.html',{"fo":fo})
def add_pdis(request):
    fo=pdiForm
    if request.method=="POST":
        s=pdiForm(request.POST,request.FILES)
        s.save
        return redirect("/all_pdi")
    return render(request,"pdi.html",{"fo":fo})
def all_pdi(request):
    a=pdi.objects.all()
    return render (request,"all_pdi.html",{"a":a})
def pdi_delete(request,id):
    s=pdi.objects.get(id=id)
    s.delete()
    return redirect('/all_pdi')
def padi_update(request,product_part_number):
    fo=pdi.objects.get(product_part_number=product_part_number)
    if request.method=="POST":
        k=pdiForm(request.POST,request.FILES,instance=fo)
        if k.is_valid():
            k.save()
            return redirect('/all_pdi')
    return render(request,'padi_update.html',{'s':fo})

def all_ais_2(request):
    a=ais.objects.filter(ApprovedByHod=False)
    return render(request,"all_ais_status_2.html",{'a':a})

def quality_approve(request,product_part_number):
    g = ais.objects.all()
    your_datetime = datetime.date.today()
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ :",your_datetime)
    dates=your_datetime
    a=ais.objects.filter(product_part_number=product_part_number).update(ApprovedByQUA = True,ApprovedByQUAUser=localStorage.getItem("user_name"),
                                                                         ApprovedByQUAdate=dates)
    data = ais.objects.get(product_part_number=product_part_number)
    data2 = QUALITY_Approve(product_part_number = data)
    data2.save()
       
    return redirect('/quality_page')
    
    
def quality_reject(request,product_part_number):
    g = ais.objects.all()
    data = ais.objects.get(product_part_number=product_part_number)
    if request.method == 'POST':
        command=request.POST["command"]
        a=ais.objects.filter(product_part_number=product_part_number).update(RejectdByQUAcommand=command)

        data2 = QUALITY_Reject(product_part_number = data,command=command)
        data2.save()
        
        #update to database
        product_list = request.POST.getlist('boxes')
      
        tem=0
        for i in product_list:
            a=ais.objects.filter(product_part_number=i).update(RejectdByQUA = True)
            tem=1
            if tem==1:
                return redirect('/quality_page')
             
    else:
        return render(request,'reject.html',{'data':data})

  ##########    HOD APROVE   ####################   
def hod_page(request):
    
    list_two=ais.objects.filter(ApprovedByHod=False,ApprovedByQUA=True,ApprovedByped=True,ApprovedByProduction=True)
    return render(request,'hod_pages.html',{'g':list_two})
def all_ais_details_hod(request):
    a=ais.objects.filter(ApprovedByHod=False)
    return render(request,"all_ais_details_hod.html",{'a':a})
def approved_ais_hod(request):
    a=ais.objects.filter(ApprovedByHod=True)
    return render(request,"approved_ais_hod.html",{'a':a})
def reject_status_hod(request):
    list_one=ais.objects.all()
    list_two=ais.objects.filter(ApprovedByQUA=True,ApprovedByProduction=True,ApprovedByped=True,ApprovedByHod=True)
    one_not_two = set(list_one).difference(list_two)
    return render(request,'reject_status_hod.html',{'a':one_not_two})
def search_hod(request):
    product_part_number=request.POST.get('product_part_number')
    a = ais.objects.filter(ApprovedByped=True,ApprovedByQUA=True,product_part_number=product_part_number,ApprovedByHod = True,ApprovedByProduction=True)
    return render(request,'search_hod.html',{'a':a})
def update_hod (request,product_part_number):
    fo=ais.objects.get(product_part_number=product_part_number)
    if request.method=="POST":
        k=aisForm(request.POST,request.FILES,instance=fo)
        if k.is_valid():
            k.save()
            return redirect('/hod_page')
    return render(request,'update_hod.html',{'s':fo})
def delete_hod(request,id):
    s=ais.objects.get(id=id)
    s.delete()
    return redirect('/approved_ais_hod')

def hod_approve(request,product_part_number):
    g = ais.objects.all() 
    your_datetime =datetime.date.today() 
    
    dates=your_datetime
       
    a=ais.objects.filter(product_part_number=product_part_number).update(ApprovedByHod = True,ApprovedByHodUser=localStorage.getItem("user_name"),
                                                                         ApprovedByHoddate=dates)
    data = ais.objects.get(product_part_number=product_part_number)
    data2 = Hod_Approve(product_part_number = data)
    data2.save()

        
        #update to database
        #product_list = request.POST.getlist('boxes')
      
       # tem=0
        #for i in product_list:
       
    return redirect('/hod_page')
def hod_reject(request,product_part_number):
    g = ais.objects.all()
    data = ais.objects.get(product_part_number=product_part_number)
    if request.method == 'POST':
           
        command=request.POST["command"]
        a=ais.objects.filter(product_part_number=product_part_number).update(RejectdByHodcommand=command)

        data2 = QUALITY_Reject(product_part_number = data,command=command)
        data2.save()
       
        #update to database
        product_list = request.POST.getlist('boxes')
        for i in product_list:
            ais.objects.filter(product_part_number=i).update(RejectdByHod = True)

        return redirect('/hod_page')
    
    else:
        return render(request,'reject.html',{'data':data})


##########    LOGIN PAGE   ####################
def login(request):
    return render(request,'login.html')

def go_for_login(request):
    user_name=request.POST.get('user')
    password=request.POST.get('password')
    s=admin_login.objects.all()
    a=production_login.objects.all()
    b=quality_login.objects.all()
    c=hod_login.objects.all()
    d=oparator_login.objects.all()
    tem=0
    for i in s:
        if i.user==user_name and i.password==password:
            localStorage.setItem("user_name",user_name)   
            tem=1
            break  
            
       
    for i in a:
        
        if i.user==user_name and i.password==password:
            localStorage.setItem("user_name",user_name)
            tem=2
            break           
            
                 
    for i in b:
        if i.user==user_name and i.password==password:
            localStorage.setItem("user_name",user_name)
            tem=3
            break
           
      
    for i in c:
        if i.user==user_name and i.password==password:
            localStorage.setItem("user_name",user_name)
            tem=4
            break
            
        
        
    for i in d:
        if i.user==user_name and i.password==password:
            localStorage.setItem("user_name",user_name)
            tem=5
            break
           
    if tem==1:
        return redirect('/ped_page')
    elif tem==2:
        return redirect("/production_page")
    elif tem==3:
        return redirect("/quality_page")
    elif tem==4:
        return redirect('/hod_page')
    elif tem==5:
         return redirect("/oparator_search")
    else:
        return redirect('/login')
        
    
    
##########    ADMIN PAGE   ####################
def admin_page(request):
    a=ais.objects.all()
    return redirect('/ped_page')
def all_ais_details(request):
    a=ais.objects.filter(ApprovedByHod=False)
    return render(request,"all_ais_details.html",{'a':a})
def approved_ais(request):
    a=ais.objects.filter(ApprovedByHod=True)
    return render(request,"approved_ais.html",{'a':a})
def ais_status_1(request):
    a=ais.objects.filter(ApprovedByHod=False)
    return render(request,"all_ais_status_1.html",{'a':a})
def search_Admin(request):
    product_part_number=request.POST.get('product_part_number')
    a = ais.objects.filter(ApprovedByped=True,ApprovedByQUA=True,product_part_number=product_part_number,ApprovedByHod = True,ApprovedByProduction=True)
    return render(request,'search_Admin.html',{'a':a})


def reject_satus(request):
    list_one=ais.objects.all()
    list_two=ais.objects.filter(ApprovedByQUA=True,ApprovedByProduction=True,ApprovedByped=True,ApprovedByHod=True)
    one_not_two = set(list_one).difference(list_two)
    return render(request,'reject_status.html',{'a':one_not_two})
##########    practic ########################

####################################
    
def add(request):
    fo=aisForm()
    if request.method=="POST":
        s=aisForm(request.POST,request.FILES)
        if s.is_valid():
            s.save()
            return redirect('/ped_page')
    return render(request,'add.html',{'fo':fo})
def add_product(request):
    fo=aisForm
    if request.method=="POST":
        s=aisForm(request.POST,request.FILES)
        if s.is_valid():
            s.save()
            return redirect("/ped_page")
    return render(request,'add.html',{"fo":fo})


##########    OPARATOR   ####################

def update_to_live(request):
    
    return render(request,'operator_search.html')

def update_to_lives(request):
    product_part_number=request.POST.get('product_part_number')
    a = ais.objects.filter(ApprovedByped=True,ApprovedByQUA=True,product_part_number=product_part_number,ApprovedByHod = True,ApprovedByProduction=True)
    return render(request,'operator.html',{'a':a})
def controll_copy(request,product_part_number):
    a = ais.objects.filter(ApprovedByped=True,ApprovedByQUA=True,product_part_number=product_part_number,ApprovedByHod = True,ApprovedByProduction=True)
    return render(request,'controll_copy.html',{'a':a})
def pdi_search(request):
    return render (request,"pdi_search.html")
    
def pdi_searchs(request):
    product_part_number=request.POST.get('product_part_number')
    a=pdi.objects.filter(product_part_number=product_part_number)
    return render(request,"pdi_searchs.html",{"a":a})
    ##########    FORGOT PASSWORD   ####################
def forgot(request):
    return render(request,'forgot.html')

def check(request):
    user=request.POST['user']
    email=request.POST['mail']
    a=admin_login.objects.all()
    b=production_login.objects.all()
    c=quality_login.objects.all()
    d=hod_login.objects.all()
    e=oparator_login.objects.all()
    tem=0
    for i in e:
        if i.user==user and i.mail==email:
            return render(request,'reset.html',{'d':i}) 
    for i in a:
        if i.user==user and i.mail==email:
            return render(request,'reset.html',{'d':i})
        
    for i in b:
        if i.user==user and i.mail==email:
            return render(request,'reset.html',{'d':i})    
    for i in c:
        if i.user==user and i.mail==email:
            return render(request,'reset.html',{'d':i}) 
    for i in d:
        if i.user==user and i.mail==email:
            return render(request,'reset.html',{'d':i}) 
    

def reset(request,id):
    a=admin_login.objects.get(id=id)
    b=production_login.objects.get(id=id)
    c=quality_login.objects.get(id=id)
    d=hod_login.objects.get(id=id)


    if request.method=='POST':
        f=admin_loginForm(request.POST,instance=d)
        if f.is_valid():
            f.save()
            return redirect('/login')
    if request.method=='POST':
        f=production_loginForm(request.POST,instance=d)
        if f.is_valid():
            f.save()
            return redirect('/login')
    if request.method=='POST':
        f=quality_loginForm(request.POST,instance=d)
        if f.is_valid():
            f.save()
            return redirect('/login') 
    if request.method=='POST':
        f=hod_loginForm(request.POST,instance=d)
        if f.is_valid():
            f.save()
            return redirect('/login')
    return render(request,'change.html',{'d':a,"d":b,"d":c,"d":d})

########################### ADD NEW USER ############################
def user_type(request):
    return render(request,"user_type.html")
def Admin_new_user(request):
    fo=admin_loginForm()
    if request.method=='POST':
        s=admin_loginForm(request.POST)
        if s.is_valid():
            s.save()
            return redirect('/login')
    return render(request,'new_user.html',{'fo':fo})
def production_new_user(request):
    fo=production_loginForm()
    if request.method=='POST':
        s=production_loginForm(request.POST)
        if s.is_valid():
            s.save()
            return redirect('/login')
    return render(request,'new_user.html',{'fo':fo})
def quality_new_user(request):
    fo=quality_loginForm()
    if request.method=='POST':
        s=quality_loginForm(request.POST)
        if s.is_valid():
            s.save()
            return redirect('/login')
    return render(request,'new_user.html',{'fo':fo})
def hod_new_user(request):
    fo=hod_loginForm()
    if request.method=='POST':
        s=hod_loginForm(request.POST)
        if s.is_valid():
            s.save()
            return redirect('/login')
    return render(request,'new_user.html',{'fo':fo})
def operator_new_user(request):
    fo=operator_loginForm()
    if request.method=='POST':
        s=operator_loginForm(request.POST)
        if s.is_valid():
            s.save()
            return redirect('/login')
    return render(request,'new_user.html',{'fo':fo})

######################### ADMIN - REJECT -UPDATE ######################
def update(request,product_part_number):
    fo=ais.objects.get(product_part_number=product_part_number)
    if request.method=="POST":
        k=aisForm(request.POST,request.FILES,instance=fo)
        if k.is_valid():
            k.save()
            return redirect('/ped_page')
    return render(request,'update.html',{'s':fo})
def delete(request,id):
    s=ais.objects.get(id=id)
    s.delete()
    return redirect('/approved_ais')
#################TRAIAL#####################
def traial(request):
    return render(request,"check.html")

    