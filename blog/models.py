from django.db import models
from django.utils.html import format_html
from tinymce.models import HTMLField

# Create your models here.

# Category Model

class Category(models.Model):
  cat_id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=100)
  description = models.TextField()
  url = models.CharField(max_length=100)
  image = models.ImageField(upload_to='category/')
  add_date = models.DateTimeField(auto_now_add=True, null=True)

  def image_tag(self):
    return format_html('<img src="/media/{}" style="width:50px;height:50px;" />'.format(self.image))

  def __str__(self):
    return self.title


# POST model

class Post(models.Model):
  post_id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=200)
  content = HTMLField()
  url = models.CharField(max_length=100)
  cat = models.ForeignKey(Category, on_delete=models.CASCADE)
  created_on = models.DateTimeField(auto_now_add=True)
  # image = models.ImageField(upload_to='post/')
  
  class Meta:
    ordering = ['-created_on']

  def __str__(self):
    return self.title


class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
  name = models.CharField(max_length=80)
  email = models.EmailField()
  body = models.TextField()
  created_on = models.DateTimeField(auto_now_add=True)
  active = models.BooleanField(default=False)

  class Meta:
    ordering = ['created_on']

  def __str__(self):
    return 'Comment {} by {}'.format(self.body, self.name)