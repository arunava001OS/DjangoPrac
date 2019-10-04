from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog_Admin
# from django.template import loader

# Create your views here.

def index(request):
    all_posts = Blog_Admin.objects.all()
    # template = loader.get_template('admin_blog/index.htm')
    context = {'all_posts' : all_posts}
    # return HttpResponse(template.render(context,request))
    return render(request,'admin_blog/index.htm',context)           ##HTTPRESPONSE inbuilt withon the render function