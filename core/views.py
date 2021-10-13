from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .models import Message, Contact, Comment, Blog
from .forms import MessageForm, ContactForm, CommentForm
from django.views.generic import TemplateView, FormView, ListView
from django.http import JsonResponse


class IndexView(FormView):
    form_class = MessageForm
    template_name = 'index.html'
    success_url = '/'

    def form_invalid(self, form):
        response = super(IndexView, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        data = {}
        response = super(IndexView, self).form_valid(form)
        if self.request.is_ajax():
            message = "{name} / {email} / {service} said: ".format(
                name=form.cleaned_data.get('name'),
                email=form.cleaned_data.get('email'),
                service=form.cleaned_data.get('service'),
                )
            message += "\n\n{0}".format(form.cleaned_data.get('message'))
            send_mail(
                subject=form.cleaned_data.get('service').strip(),
                message=message,
                from_email= settings.EMAIL_HOST_USER,
                recipient_list=['ciapivan@gmail.com'],
                fail_silently=False,)
            form.save()
            data['status'] = 'ok'
            return JsonResponse(data)
        else:
            return response


        
class AboutMeView(FormView):
    form_class = MessageForm
    template_name = 'about-me.html'
    success_url = '/o_mne/'

    def form_invalid(self, form):
        response = super(AboutMeView, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        data = {}
        response = super(AboutMeView, self).form_valid(form)
        if self.request.is_ajax():
            message = "{name} / {email} / {service} said: ".format(
                name=form.cleaned_data.get('name'),
                email=form.cleaned_data.get('email'),
                service=form.cleaned_data.get('service'),
                )
            message += "\n\n{0}".format(form.cleaned_data.get('message'))
            send_mail(
                subject=form.cleaned_data.get('service').strip(),
                message=message,
                from_email= settings.EMAIL_HOST_USER,
                recipient_list=['ciapivan@gmail.com'],
                fail_silently=False,)
            form.save()
            data['status'] = 'ok'
            return JsonResponse(data)
        else:
            return response



class SamplesView(FormView):
    form_class = MessageForm
    template_name  = 'samples.html'
    success_url = '/cennik/'

    def form_invalid(self, form):
        response = super(SamplesView, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        data = {}
        response = super(SamplesView, self).form_valid(form)
        if self.request.is_ajax():
            message = "{name} / {email} / {service} said: ".format(
                name=form.cleaned_data.get('name'),
                email=form.cleaned_data.get('email'),
                service=form.cleaned_data.get('service'),
                )
            message += "\n\n{0}".format(form.cleaned_data.get('message'))
            send_mail(
                subject=form.cleaned_data.get('service').strip(),
                message=message,
                from_email= settings.EMAIL_HOST_USER,
                recipient_list=['ciapivan@gmail.com'],
                fail_silently=False,)
            form.save()
            data['status'] = 'ok'
            return JsonResponse(data)
        else:
            return response



class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = '/kontakt/'

    def form_valid(self, form):
        message = "{name} {surname} / {email} / {subject} said: ".format(
            name=form.cleaned_data.get('name'),
            surname=form.cleaned_data.get('surname'),
            email=form.cleaned_data.get('email'),
            subject=form.cleaned_data.get('subject'))
        message += "\n\n{0}".format(form.cleaned_data.get('message'))
        send_mail(
            subject=form.cleaned_data.get('subject').strip(),
            message=message,
            from_email= settings.EMAIL_HOST_USER,
            recipient_list=['ciapivan@gmail.com'],
            fail_silently=False,)
        form.save()
        messages.success(self.request, 'Vaša správa bola úspešne odoslaná.')
        return super().form_valid(form)

    def form_invalid(self, form):
        form.add_error(None, 'Ups .. niečo je zle.')
        return super().form_invalid(form)



def blog_1(request):
    c_form = CommentForm(request.POST or None)
    comments = Comment.objects.filter(blog_no='Blog_1', reply=None)
    page = request.GET.get('page', 1)
    paginator = Paginator(comments, 5)

    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        if c_form.is_valid():   
            instance = c_form.save(commit=False)
            reply_id = request.POST.get('comment_id')
            comment_qs = None
            if reply_id:
                comment_qs = Comment.objects.get(id=reply_id)
            comment = Comment.objects.create(reply=comment_qs)
            comment.save()
            messages.success(request, 'Vaša správa bola úspešne odoslaná.')
            instance.blog_no ='Blog_1'
            instance.save()
            
            return redirect('blog:co_je_datova_analyza')
    else:
        c_form = CommentForm()

    context = {
	'c_form':c_form,
    'comments':comments,
	}

    return render(request, 'blog-1.html', context)



def blog_2(request):
    c_form = CommentForm(request.POST or None)
    comments = Comment.objects.filter(blog_no='Blog_2')
    page = request.GET.get('page', 1)
    paginator = Paginator(comments, 5)

    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        if c_form.is_valid():
            instance = c_form.save(commit=False)
            messages.success(request, 'Vaša správa bola úspešne odoslaná.')
            instance.blog_no ='Blog_2'
            instance.save()

            return redirect('blog:co_je_kniznica_numpy')
    else:
        c_form = CommentForm()

    context = {
	'c_form':c_form,
    'comments':comments,
	}

    return render(request, 'blog-2.html', context)



def blog_3(request):
    c_form = CommentForm(request.POST or None)
    comments = Comment.objects.filter(blog_no='Blog_3')
    page = request.GET.get('page', 1)
    paginator = Paginator(comments, 5)

    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        if c_form.is_valid():
            instance = c_form.save(commit=False)
            messages.success(request, 'Vaša správa bola úspešne odoslaná.')
            instance.blog_no ='Blog_3'
            instance.save()

            return redirect('blog:co_je_kniznica_pandas')
    else:
        c_form = CommentForm()

    context = {
	'c_form':c_form,
    'comments':comments,
	}

    return render(request, 'blog-3.html', context)



class BlogView(ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'blogs'
    ordering = ['-created']
    paginate_by = 6



class ServicesView(TemplateView):
    template_name = 'services.html'

class PrivacyPolicyView(TemplateView):
    template_name = 'privacy-policy.html'

class Sample1View(TemplateView):
    template_name = 'sample-1.html'

class Sample2View(TemplateView):
    template_name = 'sample-2.html'

class Sample3View(TemplateView):
    template_name = 'sample-3.html'

class Sample4View(TemplateView):
    template_name = 'sample-4.html'

class Sample5View(TemplateView):
    template_name = 'sample-5.html'

class Sample6View(TemplateView):
    template_name = 'sample-6.html'
