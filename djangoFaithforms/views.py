from django.shortcuts import render
from .forms import UserReg
from .forms import UserMembers


def register(request):
    submit_button = request.POST.get("faith")
    name = ''
    email = ''
    password = ''

    reg_form = UserReg(request.POST or None)
    if reg_form.is_valid():
        name = reg_form.cleaned_data.get("name")
        email = reg_form.cleaned_data.get("email")
        password = reg_form.cleaned_data.get("password")

    context = {'reg_form': reg_form, 'name': name, 'email': email, 'password': password,
               'submit_button': submit_button}
    return render(request, 'register.html', context)


def members(request):
    submit_members = request.POST.get('members')
    name = ''
    age = ''
    phone = ''
    city = ''
    country = ''
    mem_form = UserMembers(request.POST or None)
    if mem_form.is_valid():
        name = mem_form.cleaned_data.get("name")
        age = mem_form.cleaned_data.get("age")
        phone = mem_form.cleaned_data.get("phone")
        city = mem_form.cleaned_data.get("city")
        country = mem_form.cleaned_data.get("country")

    context = {'mem_form': mem_form,
               'name': name,
               'age': age,
               'phone': phone,
               'city': city,
               'country': country,
               'submit_members': submit_members
               }
    return render(request, 'members.html', context)