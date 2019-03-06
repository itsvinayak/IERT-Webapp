from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm,User_detailsForm
from aside.models import facultys
from home.models import degree_detail
from .models import User_details
from django.contrib.auth.models import User


########################################################################
########### register here #####################################

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
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
        'title':'profile',
    }
    return render(request, 'user/profile_update.html', context)

#########################################################################################
################ user profile #######################################


@login_required
def Profile(request):
    ###########################select perticular teacher #######################
    teacher = facultys.objects.all().filter(Designation='Computer science and engg')
    branch = degree_detail.objects.all()
    year = request.user.user_details.year
    print(year)
    for i in branch:
        if i.branch == "Computer science and engg":
            if year == '1st':
                table=i.timetable_1_year
            elif year == '2nd':
                table=i.timetable_2_year
            elif year == '3rd':
                table=i.timetable_3_year
            elif year == '4th':
                table=i.timetable_4_year
            else:
                table=""
        if i.branch == "Computer science and engg":
            if year == '1st':
                table=i.timetable_1_year
            elif year == '2nd':
                table=i.timetable_2_year
            elif year == '3rd':
                table=i.timetable_3_year
            elif year == '4th':
                table=i.timetable_4_year
            else:
                table=""
        if i.branch == "Computer science and engg":
            if year == '1st':
                table=i.timetable_1_year
            elif year == '2nd':
                table=i.timetable_2_year
            elif year == '3rd':
                table=i.timetable_3_year
            elif year == '4th':
                table=i.timetable_4_year
            else:
                table=""
        if i.branch == "Computer science and engg":
            if year == '1st':
                table=i.timetable_1_year
            elif year == '2nd':
                table=i.timetable_2_year
            elif year == '3rd':
                table=i.timetable_3_year
            elif year == '4th':
                table=i.timetable_4_year
            else:
                table=""

    context = {
        'title':'profile',
        'teacher':teacher,
        'timetable':table,
    }
    return render(request, 'user/profile.html', context)
