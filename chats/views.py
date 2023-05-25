from django.shortcuts import render
import openai

# Create your views here.

key="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"

openai.api_key = key

def home(request):
    return render(request, "chats/home.html")

def answer(request):
    question = request.POST.get('question')

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= question,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
        )
    
    text = response['choices'][0]['text']

    responses = {
        'answer':text,
    }

    return render(request, 'chats/answer.html', responses)