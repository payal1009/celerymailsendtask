from django.shortcuts import render
from django.http import HttpResponse
from .task import test_func
from .mail_task import test_mail
def test(request):
    test_func.delay()
    return HttpResponse("Done")
def send_mail_to_all(request):
    test_mail.delay()
    return HttpResponse("Sent")




