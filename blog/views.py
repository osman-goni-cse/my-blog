from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Post, Category
# Create your views here.

def home(request):
  posts = Post.objects.all()[:11] # 10 ta post dekabo initially
  print(posts)

  categories = Category.objects.all()

  data = {
    'posts': posts,
    'categories': categories,
  }
  return render(request, 'home.html', data)


def posts(request, url):

  post = Post.objects.get(url=url)
  posts = Post.objects.all()
  print(post)
  categories = Category.objects.all()

  data = {
    'posts': posts,
    'post': post,
    'categories': categories,
  }
  return render(request, 'post.html', data)


def categories(request, url):
  categories = Category.objects.all()
  category = Category.objects.get(url=url)
  posts = Post.objects.filter(cat = category)

  data = {
    'categories':categories,
    'category': category,
    'posts': posts,
  }

  return render(request, 'category.html', data)