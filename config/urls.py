"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
#이 줄은 Django의 설정 모듈을 가져옵니다.이를 통해 프로젝트 settings.py파일에 정의된 다양한 설정에 액세스할 수 있습니다.
from django.conf.urls.static import static
#이 줄은 Django urls 모듈에서 static 함수를 가져옵니다. 이 기능은 개발 중에 정적 및 미디어 파일을 제공하는 데 사용됩니다.
from django.contrib import admin
#Django 관리 인터페이스를 설정하고 사용할 수 있는 Django 관리 사이트 모듈을 가져옵니다.
from django.urls import path, include
#이 줄은 pathURL 패턴을 정의하는 데 사용되는 함수를 가져옵니다.
from config.views import index
#index import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gamelists/', include("gamelists.urls")),
    path('visited/', include("visited.urls")),
    path('ranking/', include("ranking.urls")),
    path('users/', include("users.urls")),
    path('games/', include("games.urls")),
    path("", index),
]

urlpatterns += static(
    prefix=settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)