from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.http import HttpResponse
from django.shortcuts import redirect

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():

            author = request.user
            title = form.cleaned_data.get("title") 
            pic = request.FILES.get('picture')
            text =  form.cleaned_data.get("text") 
            published_date = timezone.now()

            post = Post.objects.create(
                author = author,
                title = title,
                picture = pic,
                text = text,
                published_date = published_date
            )
            print('Processing picture')
            print(form.cleaned_data['picture'])
            print(pic)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
        return render(request, 'blog/post_edit.html', {'form':form})