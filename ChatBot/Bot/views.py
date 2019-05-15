from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
import os
from django.views.decorators.csrf import csrf_exempt
from .models import Conversation
import random

# DICTIONARY...
responses = {
    "AoA": [
        "WalaikumAsSalam. Kesy hain ap?",
        "Walaikum. Hukum kren"
    ],
    "Ma theek hn ap sunaen": [
        "Duaen hn ap ki",
        "Alhumdulillah"
    ],
    "Ap ka naam kia ha?": [
        "Allah Deta",
        "Naa cheez ko Allah Deta kehty hn",
        "A girl has no name"
    ],
    "Ziada shaloo paloo hony ka zrort nai ha": "he he. mazak tha..",
}

wrongQueries = [
    "Arey kehna kia chaty hoe?..",
    "I beg your pardon",
    "Ap pagal ho kia?"
]


def respond(message):
    if message in responses:
        res = random.choice(responses[message])
        swp = swap_pronouns(res)
        return swp
    else:
        return random.choice(wrongQueries)


def Home(request):
    return render(request, 'Bot/home.html')


def Post():
    pass
