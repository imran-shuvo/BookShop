from django.shortcuts import render,redirect
from  .models import BookInfo,BookCategory
from .forms import AddCategory,AddBook


# Create your views here.
def show_book_list(request):
    book_lists = BookInfo.objects.all()
    # images = Upload.objects.filter(file_type='image')
    # return render(request,'gallery.html',{"img":img, 'media_url':settings.MEDIA_URL})
    context = {'book_lists':book_lists}
    return render(request,'book/book_list.html',context)

def book_details(request,book_id):
    details = BookInfo.objects.get(id = book_id)
    # images = Upload.objects.filter(file_type='image')
    # return render(request,'gallery.html',{"img":img, 'media_url':settings.MEDIA_URL})
    context = {'details':details}
    return render(request,'book/book_detail.html',context)

def add_category(request):
    if(request.method == 'POST'):
        form =  AddCategory(request.POST)
        form.save()
        return redirect('add-category')
    else :
        form = AddCategory

    context = { 'form':form }

    return render(request,'book/add_category.html',context)



def show_category(request):
    category = BookCategory.objects.all()
    # images = Upload.objects.filter(file_type='image')
    # return render(request,'gallery.html',{"img":img, 'media_url':settings.MEDIA_URL})
    context = {'category':category}
    return render(request,'book/category.html',context)



def add_book(request):
    if(request.method == 'POST'):
        form =  AddBook(request.POST)
        form.save()
        return redirect('add-book')
    else :
        form = AddBook

    context = { 'form':form }

    return render(request,'book/add_book.html',context)


def edit_book(request,book_id):

    edit = BookInfo.objects.get(id=book_id)

    if(request.method == 'POST'):
        form =  AddBook(request.POST,instance = edit)
        form.save()
        return redirect('book-list')
    else :
        form = AddBook(instance=edit)

    context = { 'form':form }

    return render(request,'book/edit_book.html',context)


def delete_book(request,book_id):
    dele = BookInfo.objects.get(id=book_id)
    dele.delete()
    return redirect('book-list')
