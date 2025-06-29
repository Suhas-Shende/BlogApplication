from django.shortcuts import render,HttpResponse
from .models import Post
# Create your views here.
def bloghome(request):
    allPost=Post.objects.all()
    
    return render(request,'bloghome.html',{"allpost":allPost})


def blogpost(request,slug):
    post=Post.objects.filter(slug=slug).first()
    return render(request,'blogpost.html',{"post":post})

def blogpt(request):
    return HttpResponse(f"Hello blogpost ")