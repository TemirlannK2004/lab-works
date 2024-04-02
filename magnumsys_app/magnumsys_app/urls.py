
from django.contrib import admin
from django.urls import path,include
from app_sys import views
from app_sys.views import home
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app_sys.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)