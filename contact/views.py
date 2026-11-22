from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import ContactForm


def send_message(request):
    form = ContactForm(request.POST if request.method == "POST" else None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Thanks! Your message has been sent.")
        return redirect("contact:send")
    return render(request, "contact/contact.html", {"form": form})
