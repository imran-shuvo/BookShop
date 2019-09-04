from django.shortcuts import render,redirect
# from  .models import BuyBook
from book.models import BookInfo



mylist = []
# def xfunc(myst = [], *args):
#     mylist = myst
#     return 1

def save_record(request):
    print(request.POST)
    if request.method == 'POST':
        print(request.POST)
        return redirect('record')
    else :
        return render(request,'buylist1')









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
    return render(request,'buy/buylist1.html',context)

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
