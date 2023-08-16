from django.shortcuts import render
from .forms import UserForm


def index(request):
    return render(request, "user/index.html")


def create(request):
    if request.method == "GET":
        form = UserForm()
        context = {"form": form}
        return render(request, "user/create.html", context=context)
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                "name": form.cleaned_data["name"],
                "phone": form.cleaned_data["phone"],
                "email": form.cleaned_data["email"],
            }
            
        return render(request, "user/index.html", context=context)
    
def edit(request,user_id):
    print(user_id)
    return render(request, "user/index.html")
