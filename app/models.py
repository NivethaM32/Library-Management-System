from django.db import models

# Create your models here.
#TABLE 1
class Author(models.Model):
    name=models.CharField(max_length=100) #required??
    bio=models.TextField(blank=True)
    birth_date=models.DateField(null=True,blank=True)
    def __str__(self):
        return self.name

#TABLE 2
class Category(models.Model):
    name=models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name
    

#TABLE 3
class Book(models.Model):
    title=models.CharField(max_length=200)  #required??
    author=models.ForeignKey(Author , on_delete=models.CASCADE)
    category=models.ForeignKey(Category, on_delete=models.SET_NULL,null=True)  #SET_NULL??
    published_date=models.DateField() #required
    isbn=models.CharField( max_length=13, unique=True)
    available_copies=models.IntegerField(default=1)
    def __str__(self):
        return self.title

#TABLE 4
class Member(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    phone_number=models.CharField( max_length=15)
    joined_date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name

#creating for without using form
from django import forms
class bookform(forms.ModelForm):
    # author=forms.IntegerField(label='author_id')
    # category = forms.IntegerField(label="category_id")
    class Meta:
        model=Book
        fields='__all__'

class memberform(forms.ModelForm):
    class Meta:
        model=Member
        fields='__all__'