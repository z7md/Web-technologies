# forms.py
from django import forms
from .models import Book , Student,Student2,Address , Product

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'edition']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name","address"]

class Student2Form(forms.ModelForm):
    class Meta:
        model = Student2
        fields = ['name', 'address']

    # If you want to customize the field (optional)
    address = forms.ModelMultipleChoiceField(
        queryset=Address.objects.all(),  # Make sure the queryset includes all Address objects
        widget=forms.CheckboxSelectMultiple  # You can change this widget to any other suitable widget
    )

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description','image']


