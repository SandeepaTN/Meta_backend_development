from django import forms
jobs = [("Developer", "Developer"), ("Tester", "Tester"),   #(value stored, wshown in page)
        ("DevOps engineer", "DevOps engineer")]

# class Application(forms.Form):
#     name=forms.CharField(label='Enter name')
#     email = forms.EmailField(help_text="college mail",)
#     password=forms.PasswordInput()
#     passout_year=forms.IntegerField(required=False,min_value=2022,max_value=2024,initial=2022)      #default True
#     about=forms.CharField(widget=forms.Textarea(attrs={'rows':5}))
#     available_on=forms.DateField(widget=forms.NumberInput(attrs={'type':'date'}))
#     applying_to=forms.ChoiceField(choices=jobs)   
#     resume=forms.FileField()
    


from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model=Application
        fields='__all__'