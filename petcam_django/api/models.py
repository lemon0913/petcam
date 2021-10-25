from django.db import models
class Article(models.Model): 
    title = models.CharField('제목', max_length=120) # 제목
    
    content = models.TextField('내용')

    reg_date = models.DateTimeField('등록일', auto_now_add=True, 
    null=True, blank=True)

    update_date = models.DateTimeField('수정일', auto_now=True, 
    null=True, blank=True)
    class Meta:
        ordering = ('-reg_date',)
    def __str__(self): 
        return self.title
class SnapshotFile(models.Model):
    username = models.CharField('사용자명', max_length=20, 
    null=True, blank=True)
    
    image_file = models.FileField('스냅샷', upload_to="snapshot/%Y/%m", 
    null=True, blank=True)
   
    filename = models.CharField('파일명', max_length=64, null=True)
    
    content_type = models.CharField('Mimetype', max_length=128, null=True)
  
    size = models.IntegerField('파일크기')
  
    reg_date = models.DateTimeField('등록일', auto_now_add=True, 
    null=True, blank=True)
    class Meta:
        ordering = ('-reg_date',)  
    def __str__(self):
         return self.filename


class VideoFile(models.Model):
    username = models.CharField('사용자명', max_length=20, 
    null=True, blank=True)
  
    video_file = models.FileField('녹화 파일', upload_to="video/%Y/%m", 
    null=True, blank=True)

    filename = models.CharField('파일명', max_length=64, null=True)
 
    content_type = models.CharField('Mimetype', max_length=128, null=True)
  
    size = models.IntegerField('파일 크기')
   
    reg_date = models.DateTimeField('등록일', auto_now_add=True, 
    null=True, blank=True)
    class Meta:
        ordering = ('-reg_date',)    
    def __str__(self):
          return self.filename