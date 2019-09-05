from django.shortcuts import render,redirect
# from  .models import BuyBook
from book.models import BookInfo
from .forms import AddBuyRecord
from  .models import BuyRecord

from django.contrib.auth.models import User




mylist = []
# def xfunc(myst = [], *args):
#     mylist = myst
#     return 1

def save_record(request):
    print(request.POST)

    if request.method == 'POST':
        text = list(request.POST.getlist('book'))
        x = BookInfo.objects.get(book_name = text[0])

        print(x)
        y = User.objects.get(username=request.POST['user'])
        print(x)
        i = 0
        for i in range(len(text)):
            amount = list(request.POST.getlist('amount'))
            total = list(request.POST.getlist('total'))

        # user = request.POST.
            data = {'user':y,
                'book' : x,
                'amount' : amount[i],
                 'total' : total[i] }
            form =BuyRecord(**data)
            form.save()
            i = i + 1

        # print(text['book'][0])
        # print(text['book'][1])
        # print(text['book'][1])
        # print(text['book'][2])
        # print(len(text))
        context= {}
        return redirect('buy-list')

    else :
        form = AddBuyRecord()
        context = {'form':form }
        return render(request,'buy/buylist.html',context )









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
