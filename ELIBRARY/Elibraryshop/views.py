from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import  redirect, render,get_object_or_404
from .models import user_reg,Book
from django.http import Http404



# Create your views here.
def index(request):
    return render(request,'index.html')

def user_home(request):
    return render(request,'user_home.html')

def library(request):
    return render(request,'library.html')


# user register

def user_register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if email is lowercase
        if email != email.lower():
            return render(request, 'user_register.html', {'msg': 'Email must be in lowercase'})

        # Validate email format
        try:
            EmailValidator()(email)
        except ValidationError:
            return render(request, 'user_register.html', {'msg': 'Invalid email format'})

        # Check if email already exists
        if user_reg.objects.filter(email=email).exists():
            alert_message = "<script>alert('EMAIL ALREADY EXISTS');window.location.href='/userregistration/';</script>"
            return HttpResponse(alert_message)

        # Check if passwords match
        if password != confirm_password:
            return render(request, 'user_register.html', {'msg': 'Passwords do not match'})

        # Save user to the database
        user_reg(name=name, phone=phone, email=email, password=password).save()
        return redirect('user_login')
    else:
        return render(request, 'user_register.html')

def user_login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        us=user_reg.objects.filter(email=email,password=password)
        if us:
            userd=user_reg.objects.get(email=email,password=password)
            id=userd.id
            email=userd.email
            password=userd.password
            request.session['id']=id
            request.session['email']=email
            request.session['password']=password
            return redirect('user_home')

        else:
            msg = 'invaild password or email'  
            return render(request,'user_login.html',{'msg':msg})

    return render(request,'user_login.html') 

def user_list(request):
    users = user_reg.objects.all()
    return render(request, 'user_list.html', {'users': users})


#admin

def adminlogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        u='admin'
        p='1234'
        if username==u:
            if password==p:
                return render(request,'adminhome.html')   
    return render(request,'adminlogin.html')
    
def adminhome(request):
    return render(request,'adminhome.html')       
    
# profile

def profile(request):
    email = request.session.get('email')
    
    if not email:
        return render(request, 'index.html', {'error': 'No user logged in'})
    
    try:
        # Use case-insensitive filtering for email
        admin = get_object_or_404(user_reg, email__iexact=email)
    except Http404:
        print(f"No user found with email: {email}")
        return render(request, 'index.html', {'error': 'User not found. Please register or log in.'})
    
    user_info = {
        'adminname': admin.name,
        'phone': admin.phone,
        'email': admin.email,
        'password': admin.password,
        'confirm_password': admin.confirm_password,
    }
    
    return render(request, 'user_profile.html', user_info)

def update_profile(request):
    email= request.session.get('email')
    us =user_reg.objects.get(email=email)
    if us:
        user_info = {
            'adminname':us.name,
            'phone':us.phone,
            'email':us.email,
            'password':us.password,
            'confirm_password':us.confirm_password
        }
        return render(request,'update_profile.html',user_info)
    else:
        return render(request,'update_profie.html')
    

def user_proupdate(request):
    email = request.session.get('email')
    if not email:
        return redirect('user_login')
    if request.method == 'POST':
        user = user_reg.objects.get(email=email)
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password =request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        user.name = name
        user.phone = phone
        user.password = password
        user.confirm_password = confirm_password

        user_info = {
            'name': user.name,
            'email':user.email,
            'phone':user.phone,
            'password':user.password,
            'confirm_password':user.confirm_password
        }
        return render(request,'user_profile.html',user_info)
    else:
        return render(request,'update_profile.html')
        
    
def books(request):
    return render(request,'books.html')

def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        if Book.objects.filter(title=title).exists():
            alert_message = "<script>alert('THIS DOG ALREADY EXISTS');window.location.href='/add_pet/';</script>"
            return HttpResponse(alert_message)

        book = Book(title=title, author=author, description=description, image=image)
        book.save()

        return redirect('my_books') 

    return render(request, 'add_book.html')

def my_books(request):
    books = Book.objects.all()
    return render(request, 'my_books.html', {'books': books})

def book_details(request,bk):
    book = get_object_or_404(Book, id=bk )
    return render(request, 'book_details.html',{'book':book})

def book_list(request):
    bookss= Book.objects.all()
    return render(request, 'book_list.html', {'bookss':bookss})
   
def my_library(request):
    books = Book.objects.all()
    return render(request, 'my_library.html', {'books': books})

def library_details(request,lb):
    library = get_object_or_404(Book, id=lb )
    return render(request, 'library_details.html',{'library':library})

def search_books(request):
    query = request.GET.get('q', '')
    results = Book.objects.filter(title__icontains=query) if query else []
    return render(request, 'search_result.html', {'query': query, 'results': results})
