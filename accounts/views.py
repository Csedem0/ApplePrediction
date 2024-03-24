from django.shortcuts import render, redirect
from . import ml_predict
from .models import Prediction
from django.contrib import messages
from .forms import PredForm
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from .models import UserProfile
from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser

@login_required
def home(request):
    if request.method == 'POST':
        form = PredForm(request.POST or None)
        if form.is_valid():
            prediction = form.save(commit=False)
            prediction.user = request.user
            prediction.save()
            messages.success(request, 'New item added.....')

    selected_fields = Prediction.objects.filter(user=request.user).values(
        'id', 'Size', 'Weight', 'Sweetness', 'Crunchiness', 'Juiciness', 'Ripeness', 'Acidity'
    )

    # Check if the user is anonymous, and set user_id to None
    user_id = request.user.id if isinstance(request.user, AnonymousUser) else None

    return render(request, 'index.html', {'selected_fields': selected_fields, 'user_id': user_id})

@login_required
def result(request):
    # Extract input values from GET parameters
    Size = float(request.GET.get('Size', 0.0))
    Weight = float(request.GET.get('Weight', 0.0))
    Sweetness = float(request.GET.get('Sweetness', 0.0))
    Crunchiness = float(request.GET.get('Crunchiness', 0.0))
    Juiciness = float(request.GET.get('Juiciness', 0.0))
    Ripeness = float(request.GET.get('Ripeness', 0.0))
    Acidity = float(request.GET.get('Acidity', 0.0))

    # Check if there are predictions for the current user
    predictions = Prediction.objects.filter(user=request.user)

    if predictions.exists():
        # Call the prediction function with the extracted input values
        user_input = ml_predict.pred_models_svm(Size, Weight, Sweetness, Crunchiness, Juiciness, Ripeness, Acidity)
        return render(request, 'result.html', {'home_input': user_input, 'predictions': predictions})
    else:
        messages.warning(request, 'No predictions yet.')
        return redirect('home')

def delete(request, list_id):
    item = Prediction.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item deleted....'))
    return redirect(reverse('home'))

def posts(request, pk_test):
    post = Prediction.objects.get(id=pk_test)
    return render(request, 'posts.html', {'post':post})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Check if user is not None before trying to create a profile
            if user is not None:
                # Check if a UserProfile already exists for the user
                if not UserProfile.objects.filter(user=user).exists():
                    # Create a user profile for the new user
                    UserProfile.objects.create(user=user)
                
                return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('login')