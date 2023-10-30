from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import FormSubmission



# Create your views here.
def demo(request):
    return render(request,"index.html")
def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        firstname = request.POST.get('first_name', '')
        lastname = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        cpassword = request.POST.get('password1', '')

        if not username or not firstname or not lastname or not email or not password or not cpassword:
            # Check if any of the required fields are empty
            messages.info(request, "Please fill out all required fields")
            return redirect('register')

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=firstname, last_name=lastname, email=email)
                messages.success(request, "User created successfully")
                return redirect('login')
        else:
            messages.info(request, "Passwords do not match")
            return redirect('register')

    return render(request, "register.html")
def form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        department = request.POST.get('department')
        courses = request.POST.get('courses')
        purpose = request.POST.get('purpose')
        materials = request.POST.getlist('materials')

        form_data = FormSubmission(
            name=name,
            dob=dob,
            age=age,
            gender=gender,
            phone=phone,
            email=email,
            address=address,
            department=department,
            courses=courses,
            purpose=purpose,
            materials=materials
        )
        form_data.save()

        if purpose == 'enquiry':
            success_message = 'Enquiry submitted successfully.'
        elif purpose == 'place_order':
            success_message = 'Order placed successfully.'
        elif purpose == 'return':
            success_message = 'Return request submitted successfully.'
        else:
            success_message = 'Form submitted successfully.'

        messages.success(request, success_message)

    # Retrieve any messages and display them in the template
    stored_messages = messages.get_messages(request)
    message_list = list(stored_messages)

    return render(request, 'form.html', {'messages': message_list})

# def form(request):
#     if request.method == 'POST':
        
#         # Retrieve form data from request.POST
#         name = request.POST.get('name')
#         dob = request.POST.get('dob')
#         age = request.POST.get('age')
#         gender = request.POST.get('gender')
#         phone = request.POST.get('phone')
#         email = request.POST.get('email')
#         address = request.POST.get('address')
#         department = request.POST.get('department')
#         courses = request.POST.get('courses')
#         purpose = request.POST.get('purpose')
#         materials = request.POST.getlist('materials')  # Get a list of selected materials

#         form_data = FormSubmission(
#             name=name,
#             dob=dob,
#             age=age,
#             gender=gender,
#             phone=phone,
#             email=email,
#             address=address,
#             department=department,
#             courses=courses,
#             purpose=purpose,
#             materials=materials
#         )
#         form_data.save()
#         if purpose == 'enquiry':
#             success_message = 'Enquiry submitted successfully.'
#         elif purpose == 'place_order':
#             success_message = 'Order placed successfully.'
#         elif purpose == 'return':
#             success_message = 'Return request submitted successfully.'
#         else:
#             success_message = 'Form submitted successfully.'

#         # Set the success message
#         messages.success(request, success_message)
#         # messages.success(request, 'Form submitted successfully.')

        
#         # return redirect('form')

#     return render(request, 'form.html')

def logout(request):
    auth.logout(request)
    return redirect('/')






# def register(request):
#     if request.method == 'POST':
#         username=request.POST['username']
#         firstname=request.POST['first_name']
#         lastname=request.POST['last_name']
#         email=request.POST['email']
#         password=request.POST['password']
#         cpassword=request.POST['password1']
#         if password==cpassword:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request,"username already exist")
#                 return redirect('register')
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request,"email already exist")
#                 return redirect('register')
#             else:
#                 user=User.objects.create_user(username=username,password=password,first_name=firstname,last_name=lastname,email=email)

#             user.save();
#             print("user created")
#             return redirect('login')
#         else:
#             messages.info(request,"password not matching")
#             return redirect('register')
#         return redirect('/')
#     return render(request,"register.html")