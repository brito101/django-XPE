from django import forms
from .models import User

# modelForm

class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ["name", "phone", "email"]
        
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        


# form.Form