from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [

   path('', views.index, name='index'),
   # path('index.html', RedirectView.as_view(url='/', permanent=False), name='index1'),
   # path('index.php', RedirectView.as_view(url='/', permanent=False), name='index2'),
   path('posts/', views.posts, name='allposts'),
   path('post/<slug>/', views.post, name='post'),
   path('faq/', views.faq, name='faq'),
   path('contacts/', views.contacts, name='contacts'),
   path('order/<pass_type>/', views.order, name='order'),
   path('new_order/', views.new_order, name='new_order'),
   path('order_complete/<order_id>/', views.order_complete, name='order_complete'),
   path('about/', views.about, name='about'),
   path('callback', views.callback, name='callback'),
   path('check_order/<qr>/', views.check_order, name='check_order'),
   # path('robots.txt', views.robots, name='robots'),



]
