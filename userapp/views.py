from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views import View
from .forms import CustomUserCreationForm
from django.views import View
from django.contrib.auth.decorators import login_required
from .forms import PostForm

class SignUpView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'registration/signup.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post_all')
        return render(request, 'registration/signup.html', {'form': form})


@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.is_approved = False
            post.save()
            return redirect('post_all')
    else:
        form = PostForm()

    return render(request, 'postapp/add_post.html', {'form': form})
