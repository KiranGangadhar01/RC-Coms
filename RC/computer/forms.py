from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author', 'title', 'text', 'image')

        widgets = {
            'author': forms.TextInput(attrs={'class':'form-control'}),
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'text': forms.Textarea(attrs={'class':'form-control', 'rows':"5"}),
        }

class ContactForm(forms.Form):
    subject = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Subject'}) )
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder':'Please enter your message along with Contact details(Mobile number)' , 'class':'form-control editable medium-editor-textarea postcontent'}),)
    sender = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder':'your Email', 'class':'form-control'}))
