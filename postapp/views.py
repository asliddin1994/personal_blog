from lib2to3.fixes.fix_input import context

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Comment, Post, Tag
from .forms import CommentForm
from skillapp.models import Skill
from django.utils import timezone
from datetime import timedelta



def getPosts(request):
    template_name = 'postapp/list.html'

    # Barcha tasdiqlangan postlar
    posts = Post.objects.filter(is_approved=True).order_by('-created_on')

    # Eng yangi postlar
    newest_posts = Post.objects.filter(is_approved=True).order_by('-created_on')[:5]

    # Eng ko'p ko'rilgan postlar
    most_viewed_posts = Post.objects.filter(is_approved=True).order_by('-views')[:5]

    # Haftaning eng ommabop postlari
    last_week = timezone.now() - timedelta(days=7)
    weekly_popular_posts = Post.objects.filter(is_approved=True, created_on__gte=last_week).order_by('-views')[:5]

    # Oyning eng ommabop postlari
    last_month = timezone.now() - timedelta(days=30)
    monthly_popular_posts = Post.objects.filter(is_approved=True, created_on__gte=last_month).order_by('-views')[:5]

    # Tavsiya qilingan postlar
    recommended_posts = Post.objects.filter(is_approved=True, recommended=True)[:5]

    context = {
        'posts': posts,
        'newest_posts': newest_posts,
        'most_viewed_posts': most_viewed_posts,
        'weekly_popular_posts': weekly_popular_posts,
        'monthly_popular_posts': monthly_popular_posts,
        'recommended_posts': recommended_posts,
    }
    return render(request, template_name=template_name, context=context)

def getPost(request, pk):
    template_name = 'postapp/detail.html'
    post = get_object_or_404(Post, pk=pk)

    # Ko'rishlar sonini oshirish
    post.views += 1
    post.save()

    tags = post.tags.all()
    comments = post.comments.filter(parent=None)  # Faqatgina asosiy kommentlarni olish
    comment_form = CommentForm()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            parent_obj = None
            parent_id = request.POST.get('parentId')

            if parent_id:
                try:
                    parent_obj = Comment.objects.get(pk=parent_id)
                except Comment.DoesNotExist:
                    parent_obj = None

            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.parent = parent_obj
            new_comment.save()
            return redirect('post_detail', pk=post.pk)

    context = {
        'post': post,
        'comment_form': comment_form,
        'comments': comments,
        'tags': tags
    }
    return render(request, template_name, context)

def getPostsByTag(request, tagName):
    filter = True
    template_name = 'postapp/list.html'
    posts = Post.objects.filter(tags__name=tagName).all()
    context = {
        'posts': posts,
        'filter': filter
    }
    return render(request=request, template_name=template_name, context=context)



def about(request):
    template_name = 'postapp/about.html'
    skills = Skill.objects.all()
    context = {
        'skills': skills
    }
    return render(request=request, template_name=template_name, context=context)