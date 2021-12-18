from django.contrib import admin
from django.urls import path
from drf_yasg import openapi
from netflix_2.views import MovieList, aMovie
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

doc_view = get_schema_view(
    openapi.Info(
        title="Netflix",
        default_version='v1',
        description="(REST API) Clone of Netflix using Django Rest Framework",
        contact=openapi.Contact("Abdumutalib Mirzajonov <adumutalib1989@gmail.com>")
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/', MovieCreateList.as_view()),
    path('doc/', doc_view.with_ui("swagger", cache_timeout=0), name="swagger-doc"),
    path('redoc/', doc_view.with_ui("redoc", cache_timeout=0), name="redoc-doc"),
    path('movie/', ActorCreateList.as_view()),
    path('movie/<int:pk', aMovie.as_view()),
]
