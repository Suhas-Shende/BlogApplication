from django.shortcuts import render,HttpResponse
from .models import Contact
from django.contrib import messages
from blogapp.models import Post
# Create your views here.
def home(request):
    return render(request,'home/home.html',{})


def contact(request):
    
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content=request.POST['content']

        
        if len(name)<2 or len(email)<3 or len(phone)<3 or len(content)<3:
            messages.error(request,"Please enter valid details")
        else:
            contact=Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request,"Welcome,your blog is posted")
        print(name,email,phone,content)

    return render(request,'home/contact.html',{})

def about(request):
    return render(request,'home/about.html',{})

def search(request):
    allposts=request.GET['query']
    post=Post.objects.filter(title__icontains=allposts)
    return render(request,'home/search.html',{"allpost":post})
# render(request,'home/search.html',{})