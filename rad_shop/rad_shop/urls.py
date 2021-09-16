from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView, TemplateView

urlpatterns = [
    path('branches/', include('branches.urls')),
    path('', TemplateView.as_view(template_name='first-page.html'), name='first-page'),
    re_path(r'^admin/login/?$', RedirectView.as_view(pattern_name='account_login')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('accounts/', include('allauth.urls')),
    path('orders/', include('orders.urls')),
    path('catalog/', include('catalog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [path('captcha/', include('captcha.urls')), ]
