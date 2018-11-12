from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comment
from .forms import PostForm, SignUpForm, CommentAddForm, SearchForm
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.db.models import Avg




class Post_list(View):
    def get(self, request):
        posts = Post.objects.order_by('published_date').annotate(rating_average=Avg('comment__rating'))
        # posts_top_list = Post.objects.values('title', 'pk').annotate(rating_average=Avg('comment__rating')).order_by('-rating_average')[:10]
        posts_top_list = Post.objects.values('title', 'pk').annotate(rating_average=Avg('comment__rating')).order_by('-rating_average').exclude(rating_average=None)[:10]
        # posts_top_list = posts_top_list_all.filter(None)
        return render(request, 'items/post_list.html', {'posts': posts, 'posts_top_list': posts_top_list })





class Post_Detail(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        # posts = Post.objects.order_by('published_date').annotate(rating_average=Avg('comment__rating'))
        comments_last_ten = Comment.objects.filter(post=pk).values('created_date', 'text', 'name', 'rating').order_by('-created_date')
        comments = Comment.objects.filter(post=pk)
        form = CommentAddForm()
        return render(request, 'items/post_detail.html', {'post': post, 'comments': comments, "form": form, 'comments_last_ten': comments_last_ten})
                                  # , 'posts': posts
    def post(self, request, pk):
        posts_top_list = Post.objects.values('title', 'pk').annotate(rating_average=Avg('comment__rating')).order_by('-rating_average')
        form = CommentAddForm(request.POST)
        post = Post.objects.get(pk=pk)
        rating = request.POST.get('rating')
        if form.is_valid():
            Comment.objects.create(
                text=form.cleaned_data['text'],
                post=post,
                name=form.cleaned_data['name'],
                rating=rating,
                # posts_top_list=posts_top_list
                # rating_average=rating_average
                # rating=form.cleaned_data['rating'],
            )
            return redirect("post_detail", pk)


def search(request):
    form = SearchForm()
    posts = Post.objects.order_by('published_date').annotate(rating_average=Avg('comment__rating'))
    posts_top_list = Post.objects.values('title', 'pk').annotate(rating_average=Avg('comment__rating')).order_by(
        '-rating_average')[:10]
    query = request.GET.get("q")
    if query:
        posts = posts.filter(title__icontains=query)
    else:
        return redirect('post_list')
    return render(request, 'items/post_list.html', {'form': form, 'posts': posts, 'posts_top_list': posts_top_list})


    # def show(request):
    #     request.session['a'] = request.data.get('a', 'default rating value'),
    #     return redirect("/")




def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
        return render(request, 'items/post_edit.html', {'form': form})



class Post_Edit(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(instance=post)
        return render(request, 'items/post_edit.html', {'form': form})
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            # return render(request, 'items/post_edit.html', {'form': form, 'post': post})
            return redirect('post_detail', pk=post.pk)


class Login(View):
    def get(self, request):
        return render(request, "items/login.html", {'user': request.user})
    def post(self, request):
        login1 = request.POST.get("login")
        password = request.POST.get("password")
        user = authenticate(username=login1, password=password)
        if user:
            login(request, user)
            return redirect('post_list')
        return HttpResponse("ERROR %s %s" % (login1, password))


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect("post_list")


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('post_list')
    else:
        form = SignUpForm()
    return render(request, 'items/signup.html', {'form': form})

