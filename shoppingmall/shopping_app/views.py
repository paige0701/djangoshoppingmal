from django.contrib.sites.shortcuts import get_current_site
from django.core.mail.backends import console
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from shopping_app.forms import RegisterForm
from django.contrib.auth import login
# Create your views here.
from shopping_app.models import User, Product, Category
from shopping_app.tokens import account_activation_token
from django.contrib.auth.backends import ModelBackend
from django.core.mail import send_mail
from django.conf import settings


from django.conf import settings

from shopping_app.utils import ViewIncrease


def beforelogin(request):
    return render(request,'beforelogin.html')

def accountactivationsent(request):
    print("activation sent !!!")
    return render(request, 'auth/account_activation_sent.html')

def index(request):
    print("$$$ this is called !!cl")

    # product = Product.objects.all()
    product = Product.objects.order_by('-views')
    category = Category.objects.all()


    # Poducts.object.all()

    return render(request, 'home.html', {'product':product, 'category':category})


def signup(request):

    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('auth/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            # user.email_user(subject,message, settings.DEFAULT_FROM_EMAIL)
            from_email = settings.EMAIL_HOST_USER
            to_list = [user.email,settings.EMAIL_HOST_USER]
            send_mail(subject, message, from_email, to_list)

            print("current site = ", current_site)
            # return redirect('account_activation_sent')

            return redirect('accountactivationsent')
            # return render(request, 'auth/account_activation_sent.html')
            # return HttpResponseRedirect('/aaa/')
    else:
        print('hello')
        form = RegisterForm()
    return render(request, 'auth/register.html', {'form':form})


def aaa(request):
    print("here ???")
    console.log("hello ?")
    return render(request, 'aaa.html')


def activate(request, uidb64, token):
    print('여기 까지 오나 ?')
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user, backend=ModelBackend)
        return redirect('home')
    else:
        return render(request, 'auth/account_activation_invalid.html')


def detail(request, id):

    # increase view count
    ViewIncrease().increaseview(id=id)


    product = Product.objects.get(id=id)
    print("view count = ", product.views)
    return render(request, 'productdetail.html', {'product':product})


def category(request, id):

    one = Category.objects.get(id=id)
    product = Product.objects.filter(category=id)

    return render(request, 'category.html', {'product':product, 'one':one})