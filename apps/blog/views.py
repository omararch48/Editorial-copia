from django.shortcuts import render, redirect
from .models import Post, Category


# Create your views here.
def BlogListView(request):
    try:
        posts = Post.objects.get_availables_posts()
        categories = Category.objects.all()
    except:
        posts = None
        categories = None
    if not posts or not categories:
        return redirect('core:home')
    context = {'posts': posts, 'categories': categories, 'slug': ''}
    return render(request, 'blog/blog.html', context)


def BlogListCategoryView(request, slug):
    try:
        posts = Post.objects.get_availables_posts_by_category(slug)
        categories = Category.objects.all()
    except:
        posts = None
        categories = None
    if not posts or not categories:
        return redirect('core:home')
    context = {'posts': posts, 'categories': categories, 'slug': slug}
    return render(request, 'blog/blog.html', context)


def PostView(request, slug):
    try:
        post = Post.objects.get_available_post_by_slug(slug)
        categories = Category.objects.all()
    except:
        post = None
        categories = None
    print(post)
    if not post or not categories:
        return redirect('contact:contact')
    context = {'post': post, 'categories': categories}
    return render(request, 'blog/post.html', context)