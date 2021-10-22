from rest_framework import serializers
from .models import *

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id','title','content', 'reg_date','update_date') # 필드 설정
        exclude =[]

