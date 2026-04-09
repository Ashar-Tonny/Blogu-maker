from django import forms
from .models  import Article

class create(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title","body","Image","slug"]
        labels = {"title":"Title","body":"Content Text","Image":"Thumb","slug":"Link"}
        widgets = {
            "title": forms.TextInput(attrs={"class":"creator"}),
            "body": forms.Textarea(attrs={"placeholder":"Content","class":"creator"}),
            "Image": forms.FileInput(attrs={"class":"creator"}),
            "slug": forms.TextInput(attrs={"class":"creator"})
        }







