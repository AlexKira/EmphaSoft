# social_app/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from myapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.login, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('', include('social_django.urls', namespace='social')),
    path("", include('myapp.urls', namespace="myapp")),
    path('forms/', include('forms.urls', namespace="forms")),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
