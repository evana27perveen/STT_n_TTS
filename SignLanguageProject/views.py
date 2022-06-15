from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
import pyttsx3
from gtts import gTTS
from playsound import playsound
from django.urls import reverse
import speech_recognition as sr

engine = pyttsx3.init()


def home_view(request):
    return render(request, "home.html")


def say_engine(request):
    if request.method == 'POST':
        text = request.POST.get('userText')
        engine.say(text)
        # engine.runAndWait()
        return HttpResponse("Success")


def speechToText(request):
    return render(request, 'speechToText.html')

