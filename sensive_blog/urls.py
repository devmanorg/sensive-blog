from django.contrib import admin
from blog import views
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('admin/', admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path('page/<int:page>', views.index, name='index'),
    path('post/<slug:slug>', views.post_detail, name='post_detail'),
    path('tag/<slug:tag_title>', views.tag_filter, name='tag_filter'),
    path('contacts/', views.contacts, name='contacts'),
    path('', views.index, name='index'),
    
    
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
