from django.shortcuts import render,redirect
from .models import contacttable,registrationtable

# Create your views here.
 
def index(request):
    return render(request,"index.html")

def innerpage(request):
    return render(request,'port.html')

def co_vw(request):
    return render(request,'contactview.html')

def login(request):
    return render(request,'homepage.html')

def register(request):
    return render(request,'registration.html')





def contactform(request):
    dict={}
    try:
        c_name = request.POST['name']
        c_email = request.POST['email']
        c_subject = request.POST['subject']
        c_message = request.POST['message']
        add=contacttable(name=c_name,email=c_email,subject=c_subject,message=c_message)
        add.save()
        dict['msg']='thank you'
        return render(request,'index.html',dict)
    except Exception as e:
        print(e)
        dict['msg']='cant reach , try again'
        return render(request,'index.html',dict)
    


#contacters viewing functions    
def contactview(request):
    con_view=contacttable.objects.all()
    return render(request,'contactview.html',{'cont_view':con_view})


#updating contacters for admin only 
def updatecontact(request):
    if request.method=='POST':
        c_name = request.POST['name']
        c_email = request.POST['email']
        c_subject = request.POST['subject']
        c_message = request.POST['message']
        registerid = request.GET['idd']
        contactdata = contacttable.objects.filter(id=registerid).update(name=c_name,email=c_email,subject=c_subject,message=c_message)
        return redirect('/cv/')
    else:
        registerid=request.GET['idd']
        contactdata=contacttable.objects.filter(id=registerid)
        return render(request,'updatingcontact.html',{'cont_view':contactdata})
    

#deleting contacters for admin only
def deletecontact(request):
    registerid = request.GET['idd']
    contactdata = contacttable.objects.filter(id=registerid).delete()
    return redirect('/cv/')


#registration

def registrationform(request):
    dict2={}
    try:
        mail = request.POST['email']
        passwor = request.POST['password']
        re_passwor = request.POST['re_password']
        if passwor == re_passwor:
            add=registrationtable(email=mail,password=passwor,re_password=re_passwor)
            add.save()
            dict2['msg2']='THANKS'
            return render(request,'homepage.html',dict2)
        else:
            dict2['msg2']='somthing went wrong'
            return render(request,'registration.html',dict2)
    except Exception as e:
        print(e)
        dict2['msg2']='try agian'
        return render(request,'registration.html',dict2)

#login 
def loginform(request):
    if request.method == 'POST':
        Lemail = request.POST['email']
        Lpass = request.POST['password']
        check = registrationtable.objects.filter(email=Lemail,password=Lpass)
        if check:
            for i in check:
                request.session['id']=i.id
            return render(request,'index.html',{'success':'Hello im Emily'})
        else:
            return render(request,'homepage.html',{'error':'Sorry, Please register'})
    else:
        return render(request,'index.html')
    

#logout

def logout(request):
    if request.session.has_key('id'):
        del request.session['id']
    return redirect('/')
    



