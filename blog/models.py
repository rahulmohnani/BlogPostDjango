from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.dispatch import receiver
from django.db.models.signals import post_save 


class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')
    

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = RichTextField(blank=False, null=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to='images/profile/')
    
    
    def __str__(self):
        return str(self.user)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
	    if created:
		    Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
     

class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to='images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=False, null=True)
    post_date = models.DateField(auto_now_add=True)
    date_time = models.DateTimeField(auto_now_add=True, blank=True)
    category = models.CharField(max_length=255)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    
    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return f'{self.title}: {self.author.first_name} {self.author.last_name}'
    
    def get_absolute_url(self):
        return reverse('home')
    
    
class Comment(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Comment by {}'.format(self.name)
    
    