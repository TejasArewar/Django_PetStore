from django.shortcuts import render, redirect
from Accounts.models import Cust_register, Profile_pictures
from django.contrib import messages
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

def register(request) :
    if request.method == "POST" :
        name = request.POST['name']
        mobile = request.POST['mobile']
        email = request.POST['email']
        city = request.POST['city']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        pincode = request.POST['pincode']

        if confirm_password == password :
            if Cust_register.objects.filter(email=email).exists() :
                messages.info(request, 'Email exists')
                return redirect('/Accounts/')
            elif Cust_register.objects.filter(mobile=mobile).exists() :
                messages.info(request, 'Mobile number exists')
                return redirect('/Accounts/')
            
            else :
                password = make_password(password)
                user = Cust_register.objects.create(name=name, mobile=mobile,email=email,city=city, state=state, pincode=pincode, address=address, password=password)
                user.save()
                return redirect('/Accounts/login/')

        else :
            messages.info(request, 'Password and Confirm_Password doesnt match')
            return redirect('/Accounts/')

    return render(request, 'register.html', {'register' : register})


def login(request):
    if request.method=="POST":
        mobile = request.POST['mobile']
        password = request.POST['password']
        
        try:
            user = Cust_register.objects.get(mobile=mobile)
            if user.mobile == int(mobile) and check_password(password,user.password):     # check_password is used to unhash the password
                request.session['id'] = user.id
                return redirect('/profile/')
            else:
                messages.info(request,'Invalid Credentials')
                return redirect('/Accounts/login')
            
        except Cust_register.DoesNotExist:
            messages.info(request,'Mobile number does not exists')
            return redirect('/Accounts/login/')
        
    return render(request, 'login.html', {'login':login})



def profile_pic(request,id) :
    if request.method == "POST" :
        profile_picture = request.FILES.get('profile_pic')
        user_id = request.session.get('id')

        try :
            user = Cust_register.objects.get(id = user_id)
            profile_pics, created = Profile_pictures.objects.get_or_create(user = user)
            profile_pics.profile_pic = profile_picture
            profile_pics.save()

        except Cust_register.DoesNotExist :
            return redirect('/profile/')
        
    return redirect('/profile/')


def delete_profile_pic(request, id) :
    pic = Profile_pictures.objects.get(id = id)
    pic.delete()
    return redirect('/profile/')
