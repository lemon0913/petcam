from django.db import models

class Article(models.Model):
    title = models.CharField('제목', max_length=120) # 제목
    content = models.TextField('내용')
    reg_date = models.DateTimeField('등록일', auto_now_add=True,
        null=True, blank=True)
    update_date = models.DateTimeField('수정일', auto_now=True,
        null=True, blank=True)
        
    def __str__(self): 
        return self.title