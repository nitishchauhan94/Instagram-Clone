from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import send_mail, SignUpForm
from .models import SignUp



def home(request):
    title = 'Sign Up Now'
    form = SignUpForm(request.POST or None)
    context = {
        "title": title,
        "form": form
    }
    if form.is_valid():

        instance = form.save(commit=False)

        username = form.cleaned_data.get("username")
        if not username:
            username = "New full name"
        instance.username = username

        instance.save()
        context = {
            "title": "Thank you"
        }

    if request.user.is_authenticated() and request.user.is_staff:
        queryset = SignUp.objects.all().order_by('-timestamp')
        context = {
            "queryset": queryset
        }

    return render(request, "post_list.html", context)


def contact(request):
    title = 'Contact Us'
    title_align_center = True
    form = send_mail(request.POST or None)
    if form.is_valid():

        form_email = form.cleaned_data.get("email")

        form_username = form.cleaned_data.get("username")
        # print email, message, full_name
        subject = 'Site contact form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, 'youotheremail@email.com']
        contact_message = "%s: via %s" % (
            form_username,

            form_email)
        some_html_message = """
		<h1>hello</h1>
		"""
        send_mail(subject,
                  contact_message,
                  from_email,
                  to_email,

                  )

    context = {
        "form": form,
        "title": title,
        "title_align_center": title_align_center,
    }
    return render(request, "forms.html", context)
