from django.shortcuts import render,redirect
from django.core.mail import send_mail
import random 
from django.conf import settings
from .models import *
from django.shortcuts import render
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
from django.http import HttpResponse


razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

def index(request):
    try:
        global Data
        Data = Users.objects.get(email= request.session['user_data'])
        return render(request,"index.html",{'home':'xyz','username':Data})
    except:
        return render(request,"index.html",{'home':'xyz'})
def about(request):
    try:
         Data = Users.objects.get(email= request.POST['email'])
         return render(request,"about.html",{'about':'pqr','username':Data})
    except:
        return render(request,"about.html",{'about':'pqr'})
def contact(request):
    return render(request,"contact.html")
def register(request):
    return render(request,'register.html')
def reg_submit(request):
    if request.POST['password'] == request.POST['repassword']:
            global gen_otp 
            global info
            info = [request.POST['fname'],
                      request.POST['lname'],
                      request.POST['username'],
                      request.POST['email'],
                      request.POST['password'],
                      ]
            gen_otp = random.randint(100000,999999)
            send_mail('Welcome Welcome',
                  f"Your OTP is {gen_otp}",
                  settings.EMAIL_HOST_USER,
                  [request.POST['email']])
            return render(request,"otp.html")
    else:
         return render(request,'register.html',{'msg':'PLEASE ENTER THE PASSWORD AGAIN'})     
               
def otp(request):
    try:
     if int(request.POST['verification']) == gen_otp:
            Users.objects.create(first_name = info[0],
                                last_name = info[1],
                                username = info[2],
                                email = info[3],
                                password = info[4]
                                ) 
            return render(request,'register.html', {'msg':'Successfully Registered!!','username':Data})   
     else: 
        return render(request,'otp.html',{'msg':'invalid code !! please re-enter the code'})   
    except:
         return render(request,'register.html',{'msg':'error'})
    
def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        try:
            global Data
            Data = Users.objects.get(email= request.POST['email'])
            if request.POST['log_password'] == Data.password:
                request.session['user_data'] = request.POST['email']
                return render(request,'index.html',{'username': Data})
            else:
                return render(request,'login.html',{'msg':'enter the valid password'})
        except:

            return render(request,'register.html',{'msg':'please register yourself first'})

        
def log_out(request):
    try:
        del request.session['user_data']
        global Data
        del Data
        return render(request,'index.html') 
    except:
        return redirect('login')

def add(request):
    if request.method == 'GET':
       
        try:
            return render(request,'add_items.html',{'username':Data})
        except:
            return redirect('index') 
    else:
       blog.objects.create(
        recipe_name = request.POST['recp_name'],
        username = Data,
        categories = request.POST['cate'],
        description = request.POST['description'],
        file=request.FILES['photo']  
       )
       return redirect('index')
    
def my_account(request):
     if request.method == 'GET':
        try:
            Data=Users.objects.get(email = request.session['user_data'])
            return render(request,'my_account.html',{"username":Data})
        except:
            return redirect('login')
     else:
        user_data=Users.objects.get(email = request.session['user_data'])
        user_data.first_name=request.POST['fname']
        user_data.last_name=request.POST['lname']
        user_data.username=request.POST['username']
        user_data.save()
        return render(request,'my_account.html',{'userdata':Data})
     

def dessert_drinks(request):
    filtered_recipe = blog.objects.filter(categories=dessert_drinks)
    return render(request,'dessert.html',{'dessert_recipe':filtered_recipe})

def vegetarian(request):
    filtered_recipe = blog.objects.filter(categories=vegetarian)
    return render(request,'veg.html',{'veg_recipe':filtered_recipe})

def nonveg(request):
    filtered_recipe = blog.objects.filter(categories=nonveg)
    return render(request,'non_veg.html',{'nonveg_recipe':filtered_recipe})

def search(request):
    output=request.POST['search']
    Data=Users.objects.get(email = request.session['user_data'])

    filtered_data=blog.objects.filter(description__icontains = output)
    return render(request,'search.html',{'blogs':filtered_data,'userdata':Data})

def save_changes(request):
    pass
def payment(request):
    return render(request,'payment.html')



def homepage(request,bid):
    # try:
    user_obj = Users.objects.get(email = request.session['user_data'])
    global blog_obj
    blog_obj= blog.objects.get(id=bid)
    if request.method == 'POST':     
        currency = 'INR'
        global amount
        amount = int(request.POST['pamount']) * 100 
        # wertyblog = request.POST['blog-names']
        # a=request.POST['blog-names'] 
       
        # Create a Razorpay Order
        razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                        currency=currency,
                                                        payment_capture='0'))
    
        # order id of newly created order.
        razorpay_order_id = razorpay_order['id']
        callback_url = 'paymenthandler/'
    
        # we need to pass these details to frontend.
        context = {}
        context['razorpay_order_id'] = razorpay_order_id
        context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
        context['razorpay_amount'] = amount
        context['currency'] = currency
        context['callback_url'] = callback_url
    
        return render(request, 'abto.html', context=context)
    else:
        return render(request, 'payment.html', {'blog_id':blog_obj ,'userdata': user_obj } )
    # except:
    #     return redirect('login')
    




#----------------PURA COPIED FUNCTION-----------------------#
@csrf_exempt
def paymenthandler(request):
 
    # only accept POST request.
    if request.method == "POST":
        user_obj = Users.objects.get(email = request.session['user_data'])
        # try:
           
            # get the required parameters from post request.
        payment_id = request.POST.get('razorpay_payment_id', '')
        razorpay_order_id = request.POST.get('razorpay_order_id', '')
        signature = request.POST.get('razorpay_signature', '')
        params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
 
            # verify the payment signature.
        result = razorpay_client.utility.verify_payment_signature(
                params_dict)
        if result is not None:
                
                # try:
                    global amount
                    # capture the payemt
                    razorpay_client.payment.capture(payment_id, amount)
                    return render(request, 'success.html')
                    # render success page on successful caputre of payment
                    Payment.objects.create(
                        pay_by = user_obj,
                        pay_to = blog_obj,
                        amount = amount/100 #1000/100
                    )
                    

                # except:
 
                    # if there is an error while capturing payment.
                    return HttpResponse('paisa not found')
        else:
 
                # if signature verification fails.
                return HttpResponse('paisa not found')
        # except:
 
            # if we don't find the required parameters in POST data
        return HttpResponseBadRequest()
    else:
       # if other than POST request is made.
        return HttpResponseBadRequest()
