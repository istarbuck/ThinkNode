from django.conf.urls import *
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='main_page.html')),

    # Admin interface
    url(r'^admin/', include(admin.site.urls)),
)
