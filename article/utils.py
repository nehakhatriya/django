import random
from django.utils.text import slugify

def slugify_title(instance,save=False,new_slug=None):
    if new_slug is not None:
        slug=new_slug
    else:
        slug=slugify(instance.title)
    #Auto generate new slug
    Klass=instance.__class__
    qs=Klass.objects.filter(slug=slug).exclude(id=instance.id)
    if qs.exists():
        val=random.randint(30000,40000)
        slug=f'{slug}-{val}'
        return slugify_title(instance,save=save,new_slug=slug)
    instance.slug=slug
    if save:
         instance.save()
    return instance