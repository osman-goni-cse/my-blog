from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category
from .forms import CommentForm
# Create your views here.

def home(request):
  posts = Post.objects.all()[:10] # 10 ta post dekabo initially
  # print(posts)

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


  # For comment handling
  comments = post.comments.filter(active=True)
  new_comment = None
  # Comment posted
  
  comment_form = CommentForm(data=request.POST)
  
  if request.method == 'POST':
    if comment_form.is_valid():

      # Create Comment object but don't save to database yet
      new_comment = comment_form.save(commit=False)
      # Assign the current post to the comment
      new_comment.post = post
      # Save the comment to the database
      new_comment.save()
    else:
      comment_form = CommentForm()

  data = {
    'posts': posts,
    'post': post,
    'categories': categories,
    'comments': comments,
    'new_comment': new_comment,
    'comment_form': comment_form,
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


def allPosts(request):
  posts = Post.objects.all()
  categories = Category.objects.all()

  data = {
    'posts':posts,
    'categories': categories,
  }

  return render(request, 'allPosts.html', data)


def about(request):
  categories = Category.objects.all()

  data = {
    'categories': categories,
  }
  return render(request, 'about.html', data)