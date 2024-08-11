from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Book, Collection
from .forms import BookForm, RegisterForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            
            next_url = request.POST.get('next') or request.GET.get('next') or 'index'
            return redirect(next_url)
        else:
            error_message = 'Invalid credentials!'
            return render(request, 'accounts/login.html', {'error': error_message})
    else:
        return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        new_user = RegisterForm(request.POST)

        if new_user.is_valid():
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')

            new_user = User.objects.create_user(username, email, password)
            new_user.save()

            next_url = request.POST.get('next') or request.GET.get('next') or 'login'
            return redirect(next_url)
    else:
        return render(request, 'accounts/register.html')

@login_required
def favorite_book(request):
    return render(request, 'my-favorite.html')

@login_required
def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'book-detail.html', context={'book': book})

@login_required
def add_book(request):
    if request.method == 'POST':
        new_book = BookForm(request.POST, request.FILES)
        
        if new_book.is_valid():
            new_book.save()

            next_url = request.POST.get('next') or request.GET.get('next') or 'index'
            return redirect(next_url)
    else:
        new_book = BookForm()
        return render(request, 'add-book.html', {'form': new_book})

@login_required
def edit_book(request, id):
    if request.method == 'POST':
        # new_book = BookForm(request.POST, request.FILES)
        
        # if new_book.is_valid():
        #     new_book.save()
        #     next_url = request.POST.get('next') or request.GET.get('next') or 'index'
        #     return redirect(next_url)
        return render(request, 'edit-book.html', {'form': 'POST'})
    else:
        # new_book = BookForm()
        return render(request, 'edit-book.html', {'form': 'GET'})

@login_required
def delete_book(request, id):
    Book.objects.filter(id=id).delete()
    
    next_url = request.POST.get('next') or request.GET.get('next') or 'index'
    return redirect(next_url)

@login_required
def index(request):
    num_books = None
    books = None

    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        num_books = Book.objects.filter(title__contains=keyword).count()
        books = Book.objects.filter(title__contains=keyword)
    
    else:
        num_books = Book.objects.all().count()
        books = Book.objects.all()

    context = {
        'num_books': num_books,
        'books': books,
    }

    return render(request, 'index.html', context)

@login_required
def logout_view(request):
    logout(request)
    
    next_url = request.POST.get('next') or request.GET.get('next') or 'index'
    return redirect(next_url)