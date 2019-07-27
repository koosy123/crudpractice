from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100) 
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=True, null=True, related_name='comments')
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_user = models.TextField(max_length=20)
    comment_thumbnail_url = models.TextField(max_length=300,default='')
    comment_textfield = models.TextField()

    def __str__(self):
        return self.comment_textfield