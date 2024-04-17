from django.shortcuts import render
from core.models import Fixture, Prediction
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    fixtures = Fixture.objects.all()
    predictions = [f.predictions.filter(user=request.user).first() for f in fixtures]
    context = {
        'fixtures_and_predictions': zip(fixtures, predictions),
    }
    return render(request, 'index.html', context)