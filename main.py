# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")