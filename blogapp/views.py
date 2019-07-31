from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog, Comment
from django.core.paginator import Paginator

def home(request):
    blogs = Blog.objects
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list,3) 
    page = request.GET.get('page')
    posts = paginator.get_page(page) 
    return render(request, 'home.html',{'blogs':blogs, 'posts':posts})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    blog = Blog.objects.get(id=blog_id)
    comment = Comment.objects.filter(blog=blog)
    return render(request, 'detail.html',{'blog':blog , 'comment':comment})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))

def c_create(request,blog_id): 
    if request.method == "POST":
        comment = Comment() 
        comment.user = request.user 
        comment.blog = Blog.objects.get(id=blog_id) 
        comment.body = request.POST['comment'] 
        anonymous = request.POST.get('anonymous',False)  
        if anonymous == "1":
            comment.anonymous = True
        comment.save() 
        return redirect(detail,comment.blog.id)

def search(request):
    
    search_text=request.GET['search']
    search_filter=request.GET['search_filter']
    if search_filter == "제목": 
        posts=Blog.objects.filter(title__icontains=search_text)
    elif search_filter == "내용":
        posts=Blog.objects.filter(content__icontains=search_text)
    elif search_filter == "제목+내용":
        posts=Blog.objects.filter(Q(title__icontains=search_text)|Q(content__icontains=search_text))

    return render(request,'search.html',{'posts':posts})

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))

def update(request,blog_id):
    if request.method == "GET":
        blog=Blog.objects.get(id=blog_id)
        context={
            "blog":blog,
        }
        return render(request,'update.html',context)

    elif request.method == "POST":
        post = Blog.objects.get(id=blog_id)
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.save()
        return redirect(home)

def delete(request,blog_id):
    post = Blog.objects.get(id=blog_id)
    post.delete()
    return redirect(home)