from django.shortcuts import render,redirect

from django.http import HttpResponse
from . models import BookList
# Create your views here.

def index(request):
    books = BookList.objects.all()
    return render(request,'restapi/index.html',
        {
            'books':books,
        }
    )


def create(request):
    return render(request,'restapi/create.html')

def store(request):
    title = request.POST['title']
    price = request.POST['price']
    author = request.POST['author']
    new_book = BookList(title=title,price=price,author=author)
    new_book.save()
    return redirect('restapi:index')


def edit(request,book_id):
    book = BookList.objects.get(id=book_id)
    return render(request,'restapi/edit.html',{'book':book,})


def update(request):
    book_id = request.POST['book_id']
    title = request.POST['title']
    price = request.POST['price']
    author = request.POST['author']

    book = BookList.objects.get(pk=book_id)
    book.title = title
    book.price = price
    book.author = author

    book.save()
    return redirect('restapi:index')
    # print(title)


def delete(request,book_id):
    book = BookList.objects.get(pk=book_id)
    book.delete()
    return redirect('restapi:index')
