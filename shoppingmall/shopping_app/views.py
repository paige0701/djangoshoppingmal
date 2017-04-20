from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail.backends import console
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from shopping_app.forms import RegisterForm, CommentForm
from django.contrib.auth import login
from shopping_app.models import User, Product, Category, Comment, Cart, Like
from shopping_app.tokens import account_activation_token
from django.contrib.auth.backends import ModelBackend
from django.core.mail import send_mail
from django.conf import settings
from shopping_app.utils import ViewIncrease, CommentClass, CartClass


def beforelogin(request):
    return render(request,'beforelogin.html')


def accountactivationsent(request):
    print("activation sent !!!")
    return render(request, 'auth/account_activation_sent.html')


def index(request):

    product = Product.objects.order_by('-created_at')

    category = Category.objects.all()

    return render(request, 'home.html', {'product':product, 'category':category})


def popular(request):

    product = Product.objects.order_by('-views')
    category = Category.objects.all()

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


# 로그인을 하지 않으면 detail 페이지로 갈 수 없게 한다
# if not logged in, it redirects to login (setting.py 에 설정 했음)
@login_required
def detail(request, id):

    # increase view count
    ViewIncrease().increaseview(id=id)

    product = Product.objects.get(id=id)

    comment = Comment.objects.filter(product=id)

    form = CommentForm()

    return render(request, 'productdetail.html', {'product':product, 'form':form, 'comment':comment} )

@login_required
def comment(request,id):

    # if comment form is submitted
    if request.method == 'POST':
        form = CommentForm(request.POST)

        # and if form that is submitted is validated
        if form.is_valid():
            # getting the content from the form
            content = request.POST.get('content')

            # adding the comment
            CommentClass().addcomment(request.user.id, content, id)

            # only getting the comment related to this product id
            comment = Comment.objects.filter(product=id)

            return redirect(reverse('detail', kwargs={'id':id}))


def category(request, id):

    one = Category.objects.get(id=id)
    product = Product.objects.filter(category=id)

    return render(request, 'category.html', {'product':product, 'one':one})


def cart(request):

    cart = Cart.objects.filter(user=request.user.id)
    total = 0

    for x in cart:
        total += x.get_subtotal()
    print("total = ", total)

    return render(request, 'cart.html', {'cart': cart, 'total':total})


def cart_edit(request, id):
    print("here")
    total = 0
    user = request.user.id
    if request.method == 'POST':

        quantity = request.POST.get('quantity')

        CartClass().editCart(user,id, quantity)

        cart = Cart.objects.filter(user=user)

        for x in cart:
            total += x.get_subtotal()

        return render(request, 'cart.html', {'cart': cart, 'total': total} )


def cart_add(request,id):
    total = 0
    if request.method == 'POST':
        user =request.user.id
        product_id = id
        quantity = request.POST.get('quantity')

        CartClass().addCart(user, product_id, quantity)

        cart = Cart.objects.filter(user=user)
        for x in cart:
            total += x.get_subtotal()


        return render(request, 'cart.html', {'cart': cart, 'total':total} )

def cart_delete(request,id):
    total = 0
    user = request.user.id
    user = User.objects.get(id=user)
    product = Product.objects.get(id=id)

    if request.method =='POST':

        cart = Cart.objects.filter(user=user, product=product)
        cart.delete()

        for x in cart:
            total += x.get_subtotal()


        cart = Cart.objects.filter(user=user)

        return render(request, 'cart.html', {'cart': cart, 'total':total} )


def like(request,id):


    user_id = request.user.id
    product = Product.objects.get(id=id)


    like = Like.objects.filter(user_id=user_id, product_id=id)
    if like :
        like.delete()
        product.likes -= 1
        product.save()

    else:
        like = Like(user_id=user_id, product_id=id)
        like.save()
        product.likes += 1
        product.save()

    return redirect(reverse('detail', kwargs={'id':id}))