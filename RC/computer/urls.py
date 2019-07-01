from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('contact-us/',views.contact_email, name='contact-us'),
    path('offers/',views.OffersView.as_view(), name='offers'),
    path('post/new',views.CreatePostView.as_view(),name='post_new'),
    path('post/<int:pk>',views.PostDetailView.as_view(), name='post_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
