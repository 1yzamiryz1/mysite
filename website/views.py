from django.shortcuts import render
from website.forms import ContactForm, NewsletterForm
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages


def index_view(request):
    return render(request, "website/index.html")


def about_view(request):
    return render(request, "website/about.html")


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.instance.name = "Anonymous"
            form.save()
            messages.add_message(
                request, messages.SUCCESS, "your ticket submitted successfully"
            )
        else:
            messages.add_message(
                request, messages.ERROR, "your ticket didn't submitted"
            )
    form = ContactForm()
    context = {"form": form}
    return render(request, "website/contact.html", context)


def newsletter_view(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Thank you! Your subscription was successful."
            )
            return HttpResponseRedirect("/")
        else:
            messages.add_message(
                request, messages.ERROR, "Oops! Something went wrong. Please try again."
            )
            return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")
