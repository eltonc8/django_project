from django.shortcuts import render

def about(request):
    title = "About Us"

    context = {
        "title": title,
    }

    return render(request, "about.html", context)
