from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from api.urls import include_doc_urlpatterns
from drf_yasg.generators import OpenAPISchemaGenerator

class CustomOpenAPISchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, *args, **kwargs):
        schema = super().get_schema(*args, **kwargs)
        schema.basePath = '/api/'
        return schema


schema_view = get_schema_view(
    openapi.Info(
        title="Market API",
        default_version='v1',
        description="Market Documentation",
        contact=openapi.Contact(email=""),
        license=openapi.License(name="NerdFactory"),
    ),
    generator_class=CustomOpenAPISchemaGenerator,
    patterns=include_doc_urlpatterns,
    validators=['flex'],
    public=True,
    permission_classes=(AllowAny,),
)