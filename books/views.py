from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from books.models import Book



class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['model','Qty','Price','image']

def book_list(request, template_name='book_list.html'):
    book = Book.objects.all()
    data = {}
    data['object_list'] = book
    return render(request, template_name, data)

def book_view(request, pk, template_name='book_detail.html'):
    book= get_object_or_404(Book, pk=pk)    
    return render(request, template_name, {'object':book})

def book_create(request, template_name='book_form.html'):
    if request.method == "POST":
        form=BookForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            return render(request,template_name,{"obj":obj})  
    else:
        form=BookForm()    
    img=Book.objects.all()
    return render(request,template_name,{"img":img,"form":form})



def book_update(request, pk, template_name='book_form.html',):
    book= get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, template_name, {'form':form})

def book_delete(request, pk, template_name='book_confirm_delete.html'):
    book= get_object_or_404(Book, pk=pk)    
    if request.method=='POST':
        book.delete()
        return redirect('book_list')
    return render(request, template_name, {'object':book})



def home(request, template_name='home.html'):
    book = Book.objects.all()
    data = {}
    data['object_list'] = book
    return render(request, template_name, data)


def search_item(request):
  if request.method == "POST":
      searche = request.POST['searched']
      items = Book.objects.filter(model__contains=searche)
      return render(request,'serch.html',{'searche':searche,'items':items})
  else:
      return render(request,'serch.html')
 

# Create your views here.
def index(request):
    
    if request.method == "POST":
        form=BookForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            return render(request,"index.html",{"obj":obj})  
    else:
        form=BookForm()    
    img=Book.objects.all()
    return render(request,"index.html",{"img":img,"form":form})


