from django import forms
from .models import FeedBack
class sendFeedBack(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=FeedBack
        
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['room'].widget=forms.HiddenInput()
        self.fields['message'].widget=forms.Textarea()
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control',})
        
        
    