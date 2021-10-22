from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import *
from songline import Sendline as sl
from .emailsystem import *

# Create your views here.

# def Home(request):
#     return HttpResponse('<h1>Hello World</h1><br><p>Anurak Choosri</p><br><p>ELECTRONIC ENGINEERING</p>')

def Login(request):

    context = {}

    if request.method == 'POST':
        data = request.POST.copy()
        username = data.get('username')
        password = data.get('password')

        try:
            user = authenticate(username = username, password = password)
            login(request, user)
        except:
            context['message'] = 'Username or Password incorrect ! Please contact to Admin'

    return render(request, 'company/contact.html', context)


def Home(request):
    allproduct = Product.objects.all()
    context = {'allproduct' : allproduct}
    return render(request, 'company/home.html', context)


def Aboutus(request):
    return render(request, 'company/aboutus.html')


def ContactUs(request):

    context = {}

    if request.method == 'POST':
        data = request.POST.copy()
        title = data.get('title')
        email = data.get('email')
        detail = data.get('detail')
        print('----------' * 5)
        print('Title: {}' .format(title))
        print('Email: {}' .format(email))
        print('Detail: {}' .format(detail))
        print('----------' * 5)
        if title == '' and email == '':
            context['message'] = 'Please enter your email !!'
            return render(request, 'company/contact.html', context)
        # ContactList(title = title, email = email, detail = detail).save()
        else:
            newrecord = ContactList()
            newrecord.title = title
            newrecord.email = email
            newrecord.detail = detail
            newrecord.save()
            context['message'] = 'ตอนนี้ได้รับข้อความแล้ว ทางเราจะติดต่อกลับไปใน 24 ชั่วโมง'

            # ส่งเมลล์
            text = ''' สวัสดีคุณลูกค้า
            ทางเราได้รับคำร้องของท่านเรียบร้อยแล้ว ทางเราจะติดต่อกลับภายใน 24 ชั่วโมง
            '''
            sendthai(email, 'AI-Link', text)

            # ส่งไลน์

            token = 'ypbXW9XITlfH2iwAknIctV3u658MOP3x0TJpDT9Your'
            m = sl(token)
            m.sendtext(f'หัวข้อ: {title}\nEmail: {email}\nรายละเอียด: {detail}')
            
    return render(request, 'company/contact.html', context)
    

def Accountant(request):
    # Reverse by someone else
    # contact = ContactList.objects.all().order_by('-id')
    
    contact = ContactList.objects.all()
    context = {'contact' : contact}
    return render(request, 'company/accountant.html', context)


def Register(request):

    context = {}

    if request.method == 'POST':
        data = request.POST.copy()
        fullname = data.get('fullname')
        mobile = data.get('mobile')
        username = data.get('username')
        password = data.get('password')
        con_password = data.get('password2')
        try:
            fullname = fullname.split(' ')
            first_name = fullname[0]
            last_name = fullname[1]
        except:
            first_name = fullname
        
        
        try:
            check = User.objects.get(username = username)
            context['warnig'] = 'Email นี้มีการสมัครสมาชิกไปแล้ว กรุณาใช้ Email อื่น' .format(username)
            return render(request, 'company/register.html', context)

        except:
            if password != con_password:
                context['warning'] = 'กรุณากรอกรหัสผ่านให้ตรงกัน'
                return render(request, 'company/register.html', context)

            newUser = User()
            newUser.username = username
            newUser.email = username
            newUser.set_password(password)
            newUser.first_name = first_name
            newUser.last_name = last_name
            newUser.save()

            newprofile = Profile()
            newprofile.user = User.objects.get(username = username)
            newprofile.mobile = mobile
            newprofile.save()

        try:
            user = authenticate(username = username, password = password)
            login(request, user)
        except:
            context['message'] = 'Username or Password incorrect ! Please contact to Admin'

    return render(request, 'company/register.html', context)
