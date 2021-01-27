from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpRequest
from .models import blog, comment
from django.core import serializers
# Create your views here.
def allblogs(request):
    blogs = blog.objects
    return render(request,"blog/allblogs.htm",{'blogs':blogs})

def details(request, blog_id):
    detailBlog = get_object_or_404(blog, pk = blog_id)
    comments = comment.objects.filter(blog_id = blog_id)
    return  render(request, 'blog/detail.htm', {'blog':detailBlog, 'comments':comments})
    #return HttpResponse("<h1>hello i am here</h1>")
#TODO: 
# 1. store the comments 
# 2. check the validity of the passed data
# 3. check that the email exists
def add_comment(request:HttpRequest, blog_id):
    try:
        
        objComment= comment.objects.create(blog_id = blog.objects.get(pk=blog_id), user_name =request.POST.get('comment_author',None), email = request.POST.get('email',None), body = request.POST.get('comment',None))
        print(type(objComment))
        return JsonResponse({'comment': serializers.serialize('json',[objComment]) }, status=200)
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)

        return JsonResponse({}, status=403)