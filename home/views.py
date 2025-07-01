from django.shortcuts import render,HttpResponse,redirect
from .models import Contact,Post
from django.contrib import messages


# Create your views here.
def home(request):
        allPost=Post.objects.all()
    
        return render(request,'home/bloghome.html',{"allpost":allPost})





def blogpost(request,slug):
    post=Post.objects.filter(slug=slug).first()
    return render(request,'home/blogpost.html',{"post":post})












def contact(request):
    
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']

        
        if len(name)<2 or len(email)<3 or len(phone)<3 or len(message)<3:
            messages.error(request,"Please enter valid details")
        else:
            contact=Contact(name=name,email=email,phone=phone,message=message)
            contact.save()
            messages.success(request,"Welcome,your blog is posted")
        print(name,email,phone,message)

    return render(request,'home/contact.html',{})


def search(request):
    allposts=request.GET['query']
    post=Post.objects.filter(title__icontains=allposts)
    return render(request,'home/search.html',{"allpost":post})
# render(request,'home/search.html',{})


def searchpost(request,slug):
    post=Post.objects.filter(slug=slug).first()
    return render(request,'home/blogpost.html',{"post":post})




def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        author = request.POST['author']
        slug = request.POST['slug']
        image = request.FILES.get('image')  # important for image uploads

        if len(title) < 3 or len(content) < 10 or len(author) < 2 or len(slug) < 2 or not image:
             if not image:
               messages.error(request, "Image field should not be null. Please upload an image.")
               return render(request, 'home/create.html')
             else:
                 messages.error(request, "Please fill all fields correctly.")
        else:
            post = Post(title=title, content=content, author=author, slug=slug, image=image)
            post.save()
            messages.success(request, "✅ Blog post created successfully!")
            redirect('home/create.html')

    return render(request, 'home/create.html',{})