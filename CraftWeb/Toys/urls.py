from django.urls import path
from Toys import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns=[
	path('home/',views.home,name="home"),
	path('login/',views.login,name="login"),
	path('register/',views.register,name="register"),
	path('cart/',views.cart,name="cart"),
	path('checkout/',views.checkout,name="checkout"),
	path('contact/',views.contact,name="contact"),
	path('myAccount/',views.myAccount,name="myAccount"),
	path('productDetail/',views.productDetail,name="productDetail"),
	path('productList/',views.productList,name="productList"),
	path('wishlist/',views.wishlist,name="wishlist"),


]
urlpatterns += staticfiles_urlpatterns()