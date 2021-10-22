from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.permissions import AllowAny

class ArticleViewSet(viewsets.ModelViewSet):
 permission_classes = (AllowAny, ) # JWT 인증 제외
 queryset = Article.objects.all()
 serializer_class = ArticleSerializer
 pagination_class = None # 페이지네이션을 하지 않을 경우
