from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.core.mail import send_mail
from .assistant import query

api_key = 'sk-proj-enLT2BrMg1Ca9WyOmt4yT3BlbkFJPWexPPBmhjuVidbIx02m'


# Create your views here.

def contact(request):
    name, email, subject, body = request.data.get('name'), request.data.get("email"), request.data.get(
        "subject"), request.data.get("body")
    data = [name, email, subject, body]
    if not all(data):
        return Response({"message": "None of the fields cannot be left empty"}, status.HTTP_400_BAD_REQUEST)
    try:
        send_mail(subject, body, email, [settings.DEFAULT_FROM_EMAIL], fail_silently=True)
        return Response({"message": "Mail sent successfully"})
    except:
        return Response({"message": "Internal server error"}, status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
def chat(request):
    question = request.query_params.get("question")
    try:
        answer = query(question, api_key=api_key)
        return Response({"answer": answer})
    except:
        return Response({"answer": "Internal service error"}, status.HTTP_500_INTERNAL_SERVER_ERROR)
