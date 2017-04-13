
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.edit import CreateView
from shopping_app.forms import RegisterForm
from django.contrib.auth import views as auth_views
from shopping_app.views import index, signup, account_activation_sent, activate, aaa

urlpatterns = [
    # url(r'^register/', CreateView.as_view(
    #     template_name='auth/register.html',
    #     form_class=RegisterForm,
    #     success_url='/'
    # ),name='register'),
    url(r'^register/', signup, name='register'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/',auth_views.login, {'template_name': 'auth/login.html'}, name='login'),
    url(r'^logout/',auth_views.logout,{'next_page':'/'}, name='logout'),
    url(r'^', index, name='home'),


    url(r'^account_activation_sent/$', account_activation_sent, name='account_activation_sent'),
    url(r'^aaa/$', aaa, name='aaa'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),


    # url(r'^accounts/', include('allauth.urls')),
    # url(r'', include('social_django.urls', namespace='social')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--

]

