from django import forms


from .models import Company


class PostForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            "company_name",
            "content",
            "image",
            "draft",
            "publish",
        ]