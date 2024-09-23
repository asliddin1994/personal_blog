from lib2to3.fixes.fix_input import context

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Comment, Post, Tag
from .forms import CommentForm
from skillapp.models import Skill

def getPosts(request):
    template_name = 'postapp/list.html'
    posts = Post.objects.filter(is_approved=True).order_by('-created_on')
    context = {
        'posts': posts
    }
    return render(request, template_name=template_name, context=context)

def getPost(request, pk):
    template_name = 'postapp/detail.html'
    post = Post.objects.get(pk=pk)
    tags = post.tags.all()
    print(tags)
    comments = post.comments.all()
    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            parent_obj = None
            try:
                parent_id = request.POST.get('parentId')
            except:
                parent_id = None
            if parent_id:
                parent_obj = Comment.objects.get(pk=parent_id)
            if parent_id:
                cf = comment_form.save(commit=False)
                cf.post_id = post.id
                cf.save()
                comment_form = CommentForm()
            return redirect('post_detail', pk=post.pk)
    context = {
        'post': post,
        'comment_form': comment_form,
        'comments': comments,
        'tags': tags
    }
    return render(request, template_name=template_name, context=context)

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