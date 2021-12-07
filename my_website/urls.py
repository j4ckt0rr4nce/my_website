"""my_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from core.views import IndexView, AboutMeView, ServicesView, SamplesView, BlogView, ContactView, PrivacyPolicyView, tag

urlpatterns = [
    path('blog/', include('core.urls-blog', namespace='blog')),
    path('ukazky/', include('core.urls-samples', namespace='ukazky')),
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index-view'),
    path('o_mne/', AboutMeView.as_view(), name='o_mne'),
    path('sluzby/', ServicesView.as_view(), name='sluzby'),
    path('ukazky/', SamplesView.as_view(), name='ukazky'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('kategoria/<str:tag>', tag, name='tag'),
    path('kontakt/', ContactView.as_view(), name='kontakt'),
    path('zasady-ochrany-osobnych-udajov/', PrivacyPolicyView.as_view(), name='zasady-ochrany-osobnych-udajov'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
