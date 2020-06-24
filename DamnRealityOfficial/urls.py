"""DamnRealityOfficial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from DamnReality import views as viewsdr


urlpatterns = [
    path('admin/', admin.site.urls),
   # path('', views.home, name = 'home'),
    path('', viewsdr.crud, name = 'home'),
    path('category/<str:cat>', viewsdr.showcategory, name = 'showcategory'),
    path('product/<str:product_id>', viewsdr.showproduct, name = 'showproduct'),
    path('order/', viewsdr.order, name = "order"),
    path('DamnReality/', include('DamnReality.urls')),
    path('signup/', views.signup, name = "signup"),
    path('logout/', views.logout_request, name = "logout"),
    path('login/', views.login_request, name = "login"),
    path('account/', views.account, name = "account"),
    path('api/', include('api.urls')),
    path("about/", viewsdr.about, name="AboutUs"),
    path("contact/", viewsdr.contact, name="ContactUs"),
    path("tracker/", viewsdr.tracker, name="TrackingStatus"),
   
]   + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 
