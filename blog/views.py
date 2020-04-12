from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Post, Like, Comment
from .forms import CommentForm, PostForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.utils.text import slugify

class PostList(generic.ListView):
    queryset = Post.objects.order_by('-created_on')
    template_name = 'index.html'

def liked_list(request):
    if not request.user.is_authenticated:
        return HttpResponseNotFound('<h1>User not authenticated</h1>')

    template_name = 'liked_list.html'
    like_list = Like.objects.filter(user=request.user).order_by('created_on')
    post_list = [like.post for like in like_list]

    return render(
        request,
        template_name,
        {
            'post_list': post_list
        }
    )

# class PostDetail(generic.DetailView):
#     model = Post 
#     template_name = 'post_detail.html'

def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.order_by('-created_on')
    new_comment = None 
    
    if request.method == 'POST' and 'type' in request.POST:
        if request.POST['type'] == 'like':
            try:
                item = Like.objects.get(user=request.user, post=post)
                print('Error: item already exist')
            except Like.DoesNotExist: 
                Like.objects.create(user=request.user, post=post)
        elif request.POST['type'] == 'dislike':
            try:
                item = Like.objects.get(user=request.user, post=post)
                item.delete()
            except Like.DoesNotExist:
                print("Error: item not exist")

    if request.method == 'POST' and 'type' not in request.POST:
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post 
            new_comment.save()

    if request.user.is_authenticated:
        try:
            Like.objects.get(user=request.user, post=post)
            liked = "true"
        except Like.DoesNotExist:
            liked = "false"
    else:
        liked = "false"

    # comments = Comment.objects.all()
    return render(
        request, 
        template_name, 
        {
            'post': post,
            'comments': comments,
            'new_comment': new_comment,
            'comment_form': CommentForm(),
            'liked': liked
        }
    )

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
        
    return render(request, 'signup.html', {'form': form})

def addPost(request):
    template_name = 'add_post.html'
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user 
            post.slug = slugify(post.title)
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    
    return render(request,template_name, {'form': form})

def like(request):
    if request.method == 'POST':
        # user = request.POST['user']
        print(request.POST)

def dislike(request):
    if request.method == 'POST':
        # user = request.POST['user']
        print(request.POST)