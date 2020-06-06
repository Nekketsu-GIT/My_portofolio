from butter_cms import ButterCMS
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.core.mail import send_mail
from personal_portoflio.forms import ContactForm
from projects.models import Project
from django.contrib import messages


client = ButterCMS('3af08233eb3984f6590f8cd06f6eca9b86e95c42')


def home(request, page=1):
    latest_projects_list = Project.objects.order_by('-created_on')[:3]
    response = client.posts.all({'page_size': 3, 'page': page})
    try:
        recent_posts = response['data']
    except:
        # In the event we request an invalid page number, no data key will exist in response.
        raise Http404('Page not found')

    context = {
        'latest_projects_list': latest_projects_list,
        'recent_posts': recent_posts
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']

            message = "{0} has sent you a new message:\nSubject: {3}\n{1}\n You can contact him with {2}".format(sender_name, form.cleaned_data['message'], sender_email, form.cleaned_data['subject'])

            if send_mail('New Enquiry', message, 'josedacosta.pro.dev@gmail.com', ['josedacosta339@gmail.com'], fail_silently=False) == 1:
                messages.success(request, "Success: I received your message, Contact you soon ")
            else:
                messages.error(request, "Error: There is an, error please try again")
    else:
        form = ContactForm()

    return render(request, 'contact-us.html', {'form': form})