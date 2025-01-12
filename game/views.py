from django.shortcuts import render, redirect
from .forms import myForm
import random

guessed_number = random.randint(1, 100)

def index(request):
    return render(request, 'game/index.html')

def submit_guess(request):
    global guessed_number
    if request.method == 'POST':
        guess = int(request.POST.get('guess'))
        difficulty = request.POST.get('difficulty')
        message = ''

        if guess == guessed_number:
           message = 'Congratulations! You guessed the number!'
           guessed_number = random.randint(1, 100)
        else:
           message = 'Sorry, that is not the number. Try again!'

        return render(request, 'game/index.html', {'message': message, 'difficulty': difficulty})
    return redirect('index')