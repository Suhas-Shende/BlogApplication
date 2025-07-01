from django.db import models

# Create your models here.
class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    message=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True ,blank=True)
    def __str__(self):
        return 'message for '+ self.name +" "+self.email
    



from django.db import models
from PIL import Image
# Create your models here.
class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    content=models.TextField()
    author=models.CharField(max_length=50)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)  # Allow optional i
    slug=models.CharField(max_length=50)
    timestamp=models.DateTimeField(auto_now_add=True ,blank=True)
    def __str__(self):
        return self.title +" "+self.author
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            img = Image.open(self.image.path)

            # Resize if larger than 800x600
            max_width = 800
            max_height = 600

            if img.height > max_height or img.width > max_width:
                output_size = (max_width, max_height)
                img.thumbnail(output_size)  # maintains aspect ratio
                img.save(self.image.path)
