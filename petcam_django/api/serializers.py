from rest_framework import serializers 
from .models import *
class ArticleSerializer(serializers.ModelSerializer): 
    class Meta: 
       model = Article
       fields = ('id','title','content', 'reg_date','update_date') # 필드 설정


class SnapshotFileSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = SnapshotFile
        exclude = [] # 전체 필드 지정
        # fields = ('id', 'owner', 'image_file', 'filename', 'reg_date')

class VideoFileSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = VideoFile
        exclude = []