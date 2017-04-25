from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from shopping_app.views import index, signup, activate, accountactivationsent, category, cart_add, \
    cart, cart_edit, cart_delete, popular, like, comment, detail, comment_delete, comment_edit, comment_update

urlpatterns = [
    # url(r'^register/', CreateView.as_view(
    #     template_name='auth/register.html',
    #     form_class=RegisterForm,
    #     success_url='/'
    # ),name='register'),
    url(r'^register/$', signup, name='register'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$',auth_views.login, {'template_name': 'auth/login.html'}, name='login'),
    url(r'^logout/',auth_views.logout,{'next_page':'/'}, name='logout'),
    url(r'^$', index, name='home'),
    url(r'^popular/$', popular, name='popular'),


    url(r'^accountactivationsent/$', accountactivationsent, name='accountactivationsent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),


    # url(r'^accounts/', include('allauth.urls')),
    url(r'', include('social_django.urls', namespace='social')),
    # url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--
    # url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^detail/(?P<id>[0-9]+)/$', detail, name='detail'),

    # product like
    url(r'^detail/(?P<id>[0-9]+)/like/$', like, name='like'),

    url(r'^category/(?P<id>[0-9]+)/$', category, name='category'),

    # comment
    url(r'^detail/(?P<id>[0-9]+)/comment/$', comment, name='comment'),
    url(r'^detail/(?P<id>[0-9]+)/comment/(?P<commentid>[0-9]+)/delete/$', comment_delete, name='deletecomment'),
    url(r'^detail/(?P<id>[0-9]+)/comment/(?P<commentid>[0-9]+)/edit/$', comment_edit, name='editcomment'),
    url(r'^detail/(?P<id>[0-9]+)/comment/(?P<commentid>[0-9]+)/update/$', comment_update, name='updatecomment'),

    # cart
    url(r'^cart/$', cart, name='cart'),
    url(r'^cart/add/(?P<id>[0-9]+)/$', cart_add, name='cartadd'),
    url(r'^cart/edit/(?P<id>[0-9]+)/$', cart_edit, name='cartedit'),
    url(r'^cart/delete/(?P<id>[0-9]+)/$', cart_delete, name='cartdelete'),




    # 이걸 꼭 추가 해야한다 아니면 이미지를 찾지를 못하던데 ??
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)