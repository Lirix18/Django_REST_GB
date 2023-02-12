"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from users.views import MyUserViewSet
from TODO.views import ProjectViews, TodoViews
from drf_yasg.views import get_schema_view
from drf_yasg.openapi import Info, License, Contact

schema_view = get_schema_view(
    Info(
        title='TODO',
        default_version='1.0',
        description='description',
        license=License(name='MIT'),
        contact=Contact(email='test@test.ru')
    )
)

# router = DefaultRouter()
# router.register('users', MyUserViewSet)
# router.register('projects', ProjectViews)
# router.register('todos', TodoViews)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include('users.urls')),
    path('api/2.0/', include('users.urls', namespace='2.0')),
    path('api-token-auth/', views.obtain_auth_token),
    path('api/2.0/', include('users.urls', namespace='2.0')),
    path('swagger', schema_view.with_ui()),
    re_path(r'swagger(?P<format>\.json|\.yaml)', schema_view.without_ui()),
]
