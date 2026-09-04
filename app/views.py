from django.shortcuts import render,redirect,get_object_or_404

from app.models import *


from django.http import HttpResponse
# Create your views here.
def base(req):
    return render(req,'base.html')

def home(req):
    books=Book.objects.order_by('id')[:3]# recent book
    total_books=Book.objects.count()
    return render(req,'home.html',{'books':books,'total_books':total_books})

def book_list(req):
    books=Book.objects.all()
    return render(req,'book_list.html',{'books':books})

def book_detail(req):
    if req.method=='POST':
        book_id=req.POST.get("book_id")
        book=get_object_or_404(Book,id=book_id)
        return render(req,'book_detail.html',{'book':book})
    else:
        return redirect('book_list')

def author_list(req):
    authors=Author.objects.all()
    return render(req,'author_list.html',{'authors':authors})

def member_list(req):
    members=Member.objects.all()
    return render(req,'member_list.html',{'members':members})

def add_book(req):
    obj=bookform()
    if req.method=='POST':
        final_data=bookform(req.POST)
        final_data.save()
        return redirect('/book_list')
    else:
        return render(req,'book_form.html',{'key':obj})

def add_member(req):
    obj=memberform()
    if req.method=='POST':
        final_data=memberform(req.POST)
        final_data.save()
        return redirect('/member_list')
    else:
        return render(req,'member_form.html',{'key':obj})