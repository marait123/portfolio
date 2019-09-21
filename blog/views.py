from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import blog

# Create your views here.
def allblogs(request):

    blogs = blog.objects

    return render(request,"blog/allblogs.htm",{'blogs':blogs})

def details(request, blog_id):
    detailBlog = get_object_or_404(blog, pk = blog_id)
    return  render(request, 'blog/detail.htm', {'blog':detailBlog})
    #return HttpResponse("<h1>hello i am here</h1>")
