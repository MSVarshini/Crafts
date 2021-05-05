from django.urls import path
from Toys import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

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
	 path('image_upload/', views.hotel_image_view, name = 'image_upload'),
    path('success/', views.success, name = 'success'),

]
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)