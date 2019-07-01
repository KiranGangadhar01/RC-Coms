from django.shortcuts import render
from django.views.generic import (TemplateView,CreateView,
                                    DetailView, ListView,)

from .forms import ContactForm, PostForm
from .models import Post
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(TemplateView):
    template_name = 'computer/index.html'

def contact_email(request):

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            recipients = ['kiran.gangadhar.01@gmail.com']
            recipients.append(sender)

            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/home/')  # Redirect after POST
    else:
        form = ContactForm()  # An unbound form
    return render(request, 'computer/contact-us.html', {'form': form, })


class OffersView(ListView):
    template_name = 'computer/offers.html'

    def get_queryset(self):
        return Post.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')


class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'computer/post_detail.html'

    form_class = PostForm

    model = Post

class PostDetailView(DetailView):
    model = Post
