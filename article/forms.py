from django import forms
from .models import Article
class ArticleForm(forms.ModelForm):
    class Meta:
        model= Article
        fields=['title',"content","publish"]
    
    def clean(self):
        data=self.cleaned_data
        title=data.get("title")
        qs=Article.objects.filter(title__icontains=title)
        if qs.exists():
            return self.add_error('title',f"\"{title}\" already exists. Please pick another title")
        return data

class ArticleFormOld(forms.Form):
    title=forms.CharField()
    content=forms.CharField()


    def clean(self):
        cleaned_data=self.cleaned_data
        title=cleaned_data.get("title")
        content=cleaned_data.get("content")
        if title.lower().strip() == "the office":
            self.add_error("title","this title already exist")
        if "office" in content or "office" in title:
            self.add_error('content',"Office is not allowed in content")
            raise forms.ValidationError("office is not allowed")