from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpFrom, EditProfileForm, PasswordChangingForm, EditProfilePageForm
from blog.models import Profile, Post
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError


def validate_name(name):
    # Check if name entered by user is valid
    for c in name:
        if c in '[@_!#$%^&*()<>?/\|}{~:]':
            return False
    return True


def has_numbers(inputString):
    # Check if string has numbers
    return any(char.isdigit() for char in inputString)



class ShowProfileView(SuccessMessageMixin, DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'
    ordering = ['-date_time']
    
    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfileView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        user_posts = Post.objects.filter().order_by('-date_time')
        context['page_user'] = page_user
        context['user_posts'] = user_posts
        return context
    

class EditProfilePageView(SuccessMessageMixin, generic.UpdateView):
    model = Profile
    form_class = EditProfilePageForm
    template_name = 'registration/edit_profile_page.html'
    success_url = reverse_lazy('home')
        
        
class PasswordsChangeView(SuccessMessageMixin, PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')
    success_message = "Password Changed"


def password_success(request):
    logout(request)
    return render(request, 'registration/password_success.html')


class UserRegisterView(SuccessMessageMixin, generic.CreateView):
    form_class = SignUpFrom
    template_name = 'registration/register.html'   
    success_url = reverse_lazy('login')
    success_message = "Account Created.Login now!"
    
    def post(self,request,*args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            if validate_name(first_name) == False or has_numbers(first_name):
                self.object = None
                return self.form_invalid(form)
            if validate_name(last_name) == False or has_numbers(last_name):
                self.object = None
                return self.form_invalid(form)
            
            super(UserRegisterView,self).form_valid(form)
            return HttpResponseRedirect(self.get_success_url())

        self.object = None
        return self.form_invalid(form)
     
    
    
class UserEditView(SuccessMessageMixin, generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')
    
    def get_object(self):
        return self.request.user