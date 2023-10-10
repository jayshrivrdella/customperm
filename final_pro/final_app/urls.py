from django.urls import path
from .views import *
from .models import *

from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Custom Token Authentication API",
        default_version='v1',
        description="This API is meant for giving role based custom token authentication",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('permissiongenerator/', PermissionGenerator.as_view()),
    path('rolecreation/', RoleCreation.as_view()),
    path('usercreation/', UserCreation.as_view()),
    path('login/', Login.as_view()),
    path('product_creation/', CreateProduct.as_view()),
    path('view_products/', ViewProducts.as_view()),
    path('change_product/', ChangeProduct.as_view()),
    path('delete_product/', RemoveProduct.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

