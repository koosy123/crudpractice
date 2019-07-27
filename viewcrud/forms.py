from django import forms
from .models import Blog
from .models import Comment

class NewBlog(forms.ModelForm):
    class Meta:
        model = Blog
        # fields = '__all__'
        fields = ['title', 'body']

class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_textfield']
        widgets = {
            'comment_textfield': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'cols': 40})
            }
        labels = {'comment_textfield':''}
    
    