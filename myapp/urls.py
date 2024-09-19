from django.urls import path
from .views import *

urlpatterns = [
    path("", Home, name="home"),
    path("aboutus", AboutUs, name="about-us"),  # www.EXZ.com/aboutus
    path("contact", Contact, name="contact"),  # www.Exz.com/contact
    path("tracking", TrackingPage, name="tracking"),
    path("ask", Ask, name="ask"),
    path("sawatdee", Sawatdee),
    path("questions", Questions, name="questions"),
    path("answer/<int:askid>", Answer, name="answer"),
    path("blogs/", Posts, name="post"),
    path("blog/<slug:slug>/", PostDetail, name="post-detail"),
    # Register and Login
    path("register", Register, name="register"),
    path("login", Login, name="login"),
    # Product
    path("products/", AllProduct, name="all-product"),
    path("discount/", DiscountPage, name="discount"),
    path("product/<slug:slug>/", ProductDetail, name="product-detail"),
    path("tracking-order/<str:tid>/", TrackingOrderId, name="tracking-order-id-page"),
    # Cart
    path("add-cart/<int:pid>/", AddToCart, name="add-to-cart"),
    path("cart/", MyCart, name="my-cart"),
    path('edit-cart/',MyCartEdit, name='my-cart-edit'),
    path('checkout/',CheckOut, name='checkout'),
    path('orders/',CartOrderProduct, name='cart-order-product'),
    path('upload-slip/<str:order_id>/',OrderUploadSlip, name='my-order-upload-slip'),
    path('customer-all-order/',CustomerAllOrder, name='customer-all-order'),
    path('update-status/<str:order_id>/<str:status>/',UpdatePaid, name='update-status'),
    path('update-tracking/<str:order_id>/',CartOrderUpdateTracking, name='cart-order-update-tracking'),
    path('my-order/<str:order_id>/',MyOrder, name='my-order'),
]




    
