from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models.signals import post_save,pre_save
from .utils import  slugify_title
from django.urls import reverse

User=settings.AUTH_USER_MODEL
class Article(models.Model):
    title=models.CharField(max_length=120)
    slug=models.SlugField(unique=True,null=True,blank=True)
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    publish=models.DateField(auto_now=False,auto_now_add=False,null=True, blank=True,default=timezone.now)
    user=models.ForeignKey(User,blank=True,null=True,on_delete=models.SET_NULL)
    # def save(self,*args,**kwargs):
    #     if self.slug is None:
    #         self.slug=slugify(self.title)
    #     super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('article:detail', kwargs={"slug":self.slug})

def article_presave(sender, instance, *args,**kwargs):
    if instance.slug is None:
            slugify_title(instance,save=False)

pre_save.connect(article_presave,sender=Article)

def article_postsave(sender,instance,created,*args,**kwargs):
     if created:
          slugify_title(instance,save=True)

post_save.connect(article_postsave,sender=Article)