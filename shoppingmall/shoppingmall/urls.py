from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.edit import CreateView
from django.contrib.auth import views as auth_views

from shopping_app.views import index, signup, activate, aaa, beforelogin, accountactivationsent, category
from social_django.urls import urlpatterns as social_django_urls

from shopping_app.views import detail

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


    url(r'^accountactivationsent/$', accountactivationsent, name='accountactivationsent'),
    url(r'^aaa/$', aaa, name='aaa'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),


    # url(r'^accounts/', include('allauth.urls')),
    url(r'', include('social_django.urls', namespace='social')),
    # url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--
    # url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^beforelogin/$', beforelogin, name='beforelogin'),

    url(r'^detail/(?P<id>[0-9]+)/$', detail, name='detail'),
    url(r'^category/(?P<id>[0-9]+)/$', category, name='category'),

    # 이걸 꼭 추가 해야한다 아니면 이미지를 찾지를 못하
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)