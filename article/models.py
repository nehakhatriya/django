from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save,pre_save
from .utils import  slugify_title
class Article(models.Model):
    title=models.CharField(max_length=120)
    slug=models.SlugField(unique=True,null=True,blank=True)
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    publish=models.DateField(auto_now=False,auto_now_add=False,null=True, blank=True,default=timezone.now)

    # def save(self,*args,**kwargs):
    #     if self.slug is None:
    #         self.slug=slugify(self.title)
    #     super().save(*args,**kwargs)


def article_presave(sender, instance, *args,**kwargs):
    if instance.slug is None:
            slugify_title(instance,save=False)

pre_save.connect(article_presave,sender=Article)

def article_postsave(sender,instance,created,*args,**kwargs):
     if created:
          slugify_title(instance,save=True)

post_save.connect(article_postsave,sender=Article)