from django.shortcuts import render

from .forms import SignUpForm

# Create your views here.
def home(request):
    title = 'Welcome '
    # if request.user.is_authenticated():
    #     title = "My Title %s" %(request.user)
    # if request.method == "POST":
    #     print request.POST
    form = SignUpForm(request.POST or None)
    context = {
        "template_title": title,
        "form": form,
    }

    if form.is_valid():
        # form.save()
        instance = form.save(commit=False)
        print request.POST['email']
        full_name = form.cleaned_data.get("full_name")
        if not full_name:
            full_name = "New full name"
        instance.full_name = full_name
        # if not instance.full_name == None:
        #     instance.full_name = "Justin"
        instance.save()
        context = {
            "title": "Thank you"
        }

    return render(request, "base.html", context)
