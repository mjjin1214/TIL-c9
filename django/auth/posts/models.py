from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
# ResiazeToFill : 300, 300 맞추고 넘치는 부분 잘라냄.
# ResizeToFit : 300, 300 맞추고 남는 부분을 빈 공간으로 둠.


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # image = models.ImageField(blank=True) # FileField()
    image = ProcessedImageField(
            upload_to='posts/images', # 저장 위치
            processors=[ResizeToFill(300,300)], # 처리할 작업 목록
            format='JPEG', # 저장 포맷 (확장자)
            options={'quality':90}, # 저장 포맷 관련 옵션
        )
    created_at = models.DateTimeField(auto_now_add=True) #create 될 때, 딱 한 번 현재 시각
    updated_at = models.DateTimeField(auto_now=True) #변경이 될 때 마다, 현재 시각

    def __str__(self):
        return self.title
        

#Post : Commnet = 1 : N
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    
    # on_delete 옵션
    # 1. CASCADE : 부모가 삭제되면, 자기 자신도 삭제.
    # 2. PROTECT : 자식이 존재하면, 부모 삭제 불가능.
    # 3. SET_NULL : 부모가 삭제되면, 자식의 부모 정보에 NULL.