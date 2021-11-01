"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path

from django.urls import include,path
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from deploying import views
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),

    path('contact/', views.contact, name='contact'),
    path('product/', views.product, name='product'),
    path('services/',views.services, name='services'),
    path('single/', views.single, name='single'),
    path('single1/<str:id>', views.single, name='single1'),
    path('single2/<str:id>', views.single,name='single2')




]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,
                         document_root=settings.MEDIA_ROOT)



