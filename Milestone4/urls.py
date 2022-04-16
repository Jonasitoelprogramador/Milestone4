"""Milestone4 URL Configuration

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
from django.urls import re_path, include
from django.contrib import admin
from django.urls import path
from accounts import urls as urls_accounts
from users import urls as urls_users
from django.conf import settings
from django.conf.urls.static import static
from .views import homepage
from products.views import CreateCheckoutSessionView, Cancel, Success, StripeWebhook, ProductView, ProductDelete, ProductAdd


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(urls_accounts)),
    path('users/', include(urls_users)),
    path('', homepage, name='homepage'),
    path('create-session-view/', CreateCheckoutSessionView, name='create-session-view'),
    path('cancel/', Cancel, name='cancel'),
    path('success/', Success, name='success'),
    path('webhooks/stripe', StripeWebhook, name='stripe-webhook'),
    path('product-admin/(?P<pk>\w+)/', ProductView, name='product-admin'),
    path('product-admin/', ProductView, name='product-admin'),
    path('product-delete/(?P<pk>\w+)/', ProductDelete, name='product-delete'),
    path('product-add', ProductAdd, name='product-add')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)