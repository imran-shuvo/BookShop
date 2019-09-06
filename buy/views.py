from django.shortcuts import render,redirect
# from  .models import BuyBook
from book.models import BookInfo
from .forms import AddBuyRecord
from  .models import BuyRecord,BuyTotal
from django.contrib.auth.models import User

from django.contrib.auth.models import User




mylist = []
# def xfunc(myst = [], *args):
#     mylist = myst
#     return 1

def save_record(request):

    if request.method == 'POST':
        text = list(request.POST.getlist('book'))
        x = BookInfo.objects.get(book_name = text[0])
        num_book = len(text)
        if request.user.is_authenticated :
            c = request.user.username
            username = User.objects.get(username=c)

        total= request.POST['total'] #total model price
        tdata = {
            'user':username,
            'total':total,
            'num_book':num_book,
        }
        tform = BuyTotal(**tdata)
        tform.save()
        i = 0
        for i in range(num_book):
            book = BookInfo.objects.get(book_name = text[i])
            data = {'user':username,
                'book' : book,
                 }
            form =BuyRecord(**data)
            form.save()
            i = i + 1
        context= {}
        return redirect('checkout')

    else :

        return redirect('buy-list')









def del_cart(x):
    if x:
        global mylist
        mylist = []
    return 0


def add_cart(request,book_id):
    mylist.append(book_id)
    return redirect('book-list')



def buy_list(request):
    mlist = list(set(mylist))
    buys = []
    t_price = 0
    for i in mlist:
        buy = BookInfo.objects.get(id=i)
        bx = BookInfo.objects.values('book_price').get(id=i)
        t_price = t_price + bx['book_price']
        buys.append(buy)

    context = { 'buys': buys,'t_price':t_price }
    return render(request,'buy/buylist.html',context)



def check_out(request):
    del_cart(True)
    return render(request,'buy/checkout.html')

def cart_remove(request,book_id):
    mylis = list(set(mylist))
    i=0
    for i in range(len(mylis)):
        if mylis[i] == book_id:
            del mylis[i]
            break
        else:
            i = i+1
    global mylist
    mylist = mylis
    return redirect('buy-list')
