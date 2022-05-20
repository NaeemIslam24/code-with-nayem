
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.schemas import get_schema_view # default schema for the API
from rest_framework.documentation import include_docs_urls # schema
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('about/', include('about.urls')),
    path('contact/', include('contact.urls')),
    path('blog/', include('blog.urls')),
    path('pricing/', include('pricing.urls')),
    path('services/', include('services.urls')),
    path('team/', include('team.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('account/', include('account.urls')),
    path('docs/', include_docs_urls(title='AgencyAPI')),

    # default schema for the API
    path('schema/', get_schema_view(
        title='Agency API',
        description = 'API for the agency API',
        version = '1.0.0'
    ), name = 'openapi-schema'),


]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


