from django.conf.urls import url
from django.views.generic import detail
from .views import HomePageView, postDetailView, AddPostView

from django.conf import settings
from django.conf.urls.static import static

app_name = 'feed'

urlpatterns = [
    url('', HomePageView.as_view(), name='index'),
    url('detail/<int:pk>/', postDetailView.as_view(), name='detail'),
    url('post/', AddPostView.as_view(), name='post'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)