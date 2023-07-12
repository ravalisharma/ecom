from django.conf.urls import url


from .views import(
    cart_home,
    cart_update,
    checkout_home,
)

urlpatterns = [
    url('',cart_home,name='home'),
    url('update/',cart_update,name='update'),
    url('checkout/',checkout_home,name='checkout'),
]