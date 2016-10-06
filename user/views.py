from django.shortcuts import render, get_object_or_404
# from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from author.models import Author
from .models import User, Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from django.forms.models import inlineformset_factory

authors = Author.objects.all()

# Create your views here.
def render_main_page(request):
    return render(request, "main.html", {"authors": authors,
                                         "section": "main_page"})


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user) # set the user in the session
                    request.session["username"] = user.username
                    request.session["user_id"] = user.id
                    request.session["user_email"] = user.email
                    request.session["user_is_staff"] = user.is_staff
                    return HttpResponseRedirect('/users/') # Authenticated successfully
                else:
                    # url = reverse('user:login_again', args=["disabled"])
                    # return HttpResponseRedirect(url) # Disabled account
                    auth_status = "disabled"
            else:
                # url = reverse('user:login_again', args=["invalid"])
                # return HttpResponseRedirect(url) # Invalid credentials
                auth_status = "invalid"
    else:
        auth_status = ""
        form = LoginForm()
    return render(request, "registration/login.html", {"authors": authors,
                                                       "form": form,
                                                       "auth_status": auth_status})


def user_logout(request):
    logout(request)
    messages.info(request, "Вы вышли из аккаунта")
    # return render(request, "registration/logged_out.html", {"authors": authors})
    return render(request, "main.html", {"authors": authors,
                                         "section": "main_page"})

def need_login(request):
    return render(request, "registration/need_login.html", {"authors": authors})

def user_register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST, request.FILES)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yer
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data["password1"])
            # Save the User object
            new_user.save()
            new_profile = Profile.objects.create(user = new_user,
                                                 date_of_birth = user_form.cleaned_data["date_of_birth"],
                                                 gender = user_form.cleaned_data["gender"])

            if request.FILES.get("photo", False):
                new_profile.photo = request.FILES["photo"]
            new_profile.save()
            return render(request, "registration/registration_done.html", {"authors": authors})
    else:
        user_form = UserRegistrationForm()
    return render(request, "registration/registration.html", {"form": user_form,
                                                              "authors": authors,
                                                              "section": "registration"})

@login_required
def user_page(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile = get_object_or_404(Profile, user = user)
    return render(request, "users/user/user_page.html", {"profile": profile,
                                                         "authors": authors,
                                                         "section": "user_page"})

@login_required
def edit_user_page(request, user_id):
    # user_id is not used for now
    if request.method == "POST":
        user_form = UserEditForm(instance = request.user, data = request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data = request.POST,
                                       files = request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Данные пользователя {} успешно изменены".format(request.user))
    else:
        user_form = UserEditForm(instance = request.user)
        profile_form = ProfileEditForm(instance = request.user.profile)
    return render(request,
                 "users/user/edit_user_page.html",
                 {"authors": authors,
                  "section": "user_page",
                  "user_form": user_form,
                  "profile_form": profile_form})
