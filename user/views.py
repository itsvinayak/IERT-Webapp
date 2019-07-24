from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm,User_detailsForm
from aside.models import facultys
from home.models import degree_detail
from extra_links.models import notice_board
from .models import User_details
from django.contrib.auth.models import User

#################for email send when register############################\

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context



########################################################################
########### register here #####################################

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            ######################### mail system ####################################
            htmly = get_template('user/Email.html')
            d = { 'username': username }
            subject, from_email, to = 'welcome to iert', 'itssvinayak@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            ##################################################################
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})

###################################################################################
################login forms###################################################

def Login(request):
    if request.method == 'POST':

        #AuthenticationForm_can_also_be_used__

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request,user)
            messages.success(request, f' wecome {username} !!')
            return redirect('index')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'user/login.html', {'form':form,'title':'log in'})


#####################################################################################
# user profile update ############################

@login_required
def Profile_update(request):
    if request.method == 'POST':
        pd_form = User_detailsForm(request.POST, instance=request.user.user_details)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if p_form.is_valid() and u_form.is_valid() and pd_form.is_valid():
            pd_form.save(commit=True)
            p_form.save()
            u_form.save()
            messages.success(request, f'profile is updated')
            return redirect('profile')

    pd_form = User_detailsForm(instance=request.user.user_details)
    p_form = ProfileUpdateForm(instance=request.user.profile)
    u_form = UserUpdateForm(instance=request.user)

    context = {
        'pd_form':pd_form,
        'p_form':p_form,
        'u_form': u_form,
        'title':'profile update for {}'.format(request.user),
    }
    return render(request, 'user/profile_update.html', context)

#########################################################################################
################ user profile #######################################


@login_required
def Profile(request):
    ###########################select particular teacher #######################
    teacher = facultys.objects.all().filter(branch=request.user.user_details.branch)
    notices = notice_board.objects.filter(branch=request.user.user_details.branch)
    context = {
        'title':request.user,
        'teacher':teacher,
        'notices':notices,
    }
    return render(request, 'user/profile.html', context)
