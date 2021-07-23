"""suari URL Configuration

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
from django import urls
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from api.views import PersonViewSet
from api.views import PersonTypeViewSet
from api.views import PersonMediaTypeViewSet
from api.views import PersonMediaViewSet
from api.views import PersonAuditViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register(r'person', PersonViewSet)
router.register(r'person-type', PersonTypeViewSet)
router.register(r'person-media-type', PersonMediaTypeViewSet)
router.register(r'person-media', PersonMediaViewSet)
router.register(r'person-audit', PersonAuditViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('docs/', include_docs_urls(title="API Suari"), name="api-docs")

]