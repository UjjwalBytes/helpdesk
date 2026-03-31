from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Ticket
from .forms import RegisterForm
from django.contrib.auth import logout
# from django.shortcuts import redirect
# from django.shortcuts import get_object_or_404

from .models import FAQ
from django.http import JsonResponse



def chatbot(request):
    if request.method == "POST":
        user_query = request.POST.get('query').lower()

        faqs = FAQ.objects.all()

        for faq in faqs:
            if faq.question.lower() in user_query:
                return JsonResponse({
                    'response': faq.answer,
                    'found': True
                })

        return JsonResponse({
            'response': "I couldn't find an answer. Please login to raise a ticket.",
            'found': False
        })



def home(request):
    return render(request, 'home.html')


# ✅ REGISTER VIEW

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


# ✅ DASHBOARD
@login_required
def dashboard(request):
    tickets = Ticket.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'tickets': tickets})


# ✅ CREATE TICKET
@login_required
def create_ticket(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']

        Ticket.objects.create(
            user=request.user,
            title=title,
            description=description
        )

        return redirect('dashboard')

    return render(request, 'create_ticket.html')
  



# this is for editing the ticket when admin is unable to understand the issue
@login_required
def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)

    if request.method == 'POST':
        ticket.title = request.POST['title']
        ticket.description = request.POST['description']

        ticket.needs_more_info = False  # reset flag
        ticket.status = 'Pending'      # send back to admin

        ticket.save()

        return redirect('dashboard')

    return render(request, 'edit_ticket.html', {'ticket': ticket})


def custom_logout(request):
    logout(request)
    return redirect('login')