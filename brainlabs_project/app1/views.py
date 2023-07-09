from django.shortcuts import render
import requests
import random

# Create your views here.

data = requests.get('https://countriesnow.space/api/v0.1/countries/capital')


def index(request):
    if request.method == 'POST':
        currectCapital = request.session['currectCapital']
        browserCapiatal = request.POST.get('capital')
        country = request.POST.get('country')
        print(f"Correct Capital {currectCapital} Browser capital {browserCapiatal}")
        if currectCapital == browserCapiatal:
            return render(request, 'index2.html', {"question": country, "msg": "Correct"})
        else:
            return render(request, 'index2.html', {"question": country, "msg": "Wrong", 'correct': currectCapital})

    else:
        res = data.json()
        countr_list = res['data']
        randomIndex = random.randint(1, len(countr_list))
        question = countr_list[randomIndex]
        print(question)
        currectCapital = question.get('capital')
        request.session['currectCapital'] = currectCapital
        country = question.get('name')
        return render(request, 'index.html', {"question": country})



