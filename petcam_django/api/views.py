from rest_framework import viewsets
from .models import *
from .serializers import *
from .paginations import VideoPageNumberPagination

class ArticleViewSet(viewsets.ModelViewSet): 
    queryset = Article.objects.all() 
    serializer_class = ArticleSerializer   

class SnapshotFileViewSet(viewsets.ModelViewSet): 
    queryset = SnapshotFile.objects.all() 
    serializer_class = SnapshotFileSerializer   

class VideoFileViewSet(viewsets.ModelViewSet): 
    queryset = VideoFile.objects.all() 
    serializer_class = VideoFileSerializer  
    pagination_class = VideoPageNumberPagination