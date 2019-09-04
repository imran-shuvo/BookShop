from django.urls import path
from . import views


urlpatterns = [


    path('buy/<book_id>',views.add_cart,name = 'buy'),
    path('cart-remove/<book_id>',views.cart_remove,name = 'cart-remove'),
    path('buy-list/',views.buy_list,name = 'buy-list'),
    path('checkout/',views.check_out,name = 'checkout'),
    path('record/',views.save_record,name = 'record'),
]
