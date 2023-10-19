from django.shortcuts import render

def Index(request):
    return render(request , "index.html")


def another_page(request):
    return render(request , "another_page.html")
