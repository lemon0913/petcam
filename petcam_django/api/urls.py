from django.urls import path, include
from rest_framework import routers 
from api.views import *

router = routers.DefaultRouter() 
router.register('board', ArticleViewSet) # api/board
router.register('snapshot', SnapshotFileViewSet) # api/snpashot
router.register('video', VideoFileViewSet) # api/video
urlpatterns = [
    path('', include(router.urls)),
]