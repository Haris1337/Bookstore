from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Book
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login, logout
from .forms import PurchaseForm


def book_list(request): #iterate through the book list.
	books = Book.objects.all()
	c = {'books':books}

	return render(request, 'book/book_list.html', c)



def add_view(request): #request the book parameters and add a new book to the array. If the user is a staff member, proceed to add.html, if not, return to login. user.is_staff not really necessary as it's handled in book_list.html.
	if request.user.is_staff:
		if(request.method == 'POST'):
			title = request.POST['title']
			price = request.POST['price']
			book = Book(title=title, price=price)
			book.save()
			return redirect('/books')
		else: 
			return render(request, 'book/add.html')
	else:
		return redirect('/login')


@login_required(login_url="/login/") #Get books by id and request the form parameters, book, book.price and logged in user. Save to DB.
def purchase(request, id):
	book = Book.objects.get(id=id)
	if request.method == 'POST':
	#	print '1'  Testing purposes
	#	print 'book.id: ', book.id
	#	print 'book.price: ', book.price
	#	print 'book.title: ', book.title
	#	print 'request.POST: ', request.POST
		pform = PurchaseForm(data=request.POST)
		if pform.is_valid():
			buy = pform.save(commit=False)
			buy.book = book
			buy.price = book.price
			buy.user = request.user
			buy.save()
		return redirect('/books')
	else:
		pform = PurchaseForm()
	return render(request, 'book/book_detail.html', {'book':book, 'pform':pform})


def login_view(request): #Using Authform to authenticate the user, and login to log them in.
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return redirect('/books')

	else:
		print 'hello'
		form = AuthenticationForm()
	return render(request, 'accounts/login.html', {'form':form})

def logout_view(request): #Use builtin logout to log the user out.
	if request.method == 'POST':
		logout(request)
		return redirect('/books')
	else:
		return redirect('/books')

def signup_view(request): #Using built in form for signup with the default backend that uses username as id, then logs them in.
	if request.method == 'POST':
		form = UserCreationForm(request.POST) 
		if form.is_valid():
			user = form.save()
			user.backend = 'django.contrib.auth.backends.ModelBackend' 
			login(request, user) 
			return redirect ('/books') 
	else:
		form = UserCreationForm()
	
	return render(request, 'accounts/signup.html', {'form':form})
	
