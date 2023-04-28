from django import forms
from .models import Post, Category

try:
    choices = Category.objects.all().values_list('name','name')
    choice_list = []
    for item in choices:
        choice_list.append(item)
    choice_list = set(choice_list.extend(Category.CHOICES))
except:
    pass


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 'author', 'category','body','header_image')
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'author' : forms.TextInput(attrs={'class':'form-control','value':'','id':'auth','type':'hidden'}),
            'category' : forms.Select(attrs={'class':'form-control'}, choices=choice_list),
            'body' : forms.Textarea(attrs={'class':'form-control','rows':5,'required':'true'}),
        }


class EditForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 'category', 'body','header_image')
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'category' : forms.Select(attrs={'class':'form-control'}, choices=choice_list),
            'body' : forms.Textarea(attrs={'class':'form-control','rows':4}),
        }