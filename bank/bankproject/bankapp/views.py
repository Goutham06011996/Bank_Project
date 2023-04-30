from django.shortcuts import render, redirect
from .forms import ApplicationForm
from bankapp.models import Branch, Account
from datetime import date, timedelta
from bankapp.models import District
from django.http import JsonResponse
from django.views.generic import ListView
from django.contrib import messages


def index(request):

    return render(request,'index.html')



def application_form(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,"Application Accepted")
            user = request.user
            user_id = user.id
            application = Account.objects.filter(user_id=user_id)
            context = {
                'application_list': application
            }

            return render(request, 'landing.html',{'form': form,'application_list':application,})
    else:
        # create an instance of Account to pass to the form
        account_instance = Account()
        form = ApplicationForm(instance=account_instance)
    return render(request, 'form.html', {'form': form})


# def application_form(request):
#     if request.method == 'POST':
#         form = ApplicationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages="Form submitted successfully"
#             username=request.session['username']
#             application = Account.objects.filter(name=username)
#             context = {
#                 'application_list': application
#             }
#
#             return render(request, 'landing.html',{'form': form, 'messages':messages,'application_list':application})
#     else:
#         # create an instance of Account to pass to the form
#         account_instance = Account()
#         form = ApplicationForm(instance=account_instance)
#     return render(request, 'application_form.html', {'form': form})



def load_branches(request):

    district_id = request.GET.get('district_id')
    branches = Branch.objects.filter(district_id=district_id).order_by('name')
    data = {'branches': list(branches.values('id', 'name'))}
    return JsonResponse(data)


def form(request):
    today = date.today()
    user = request.user
    user_id = user.id
    district = District.objects.all()
    max_date = today - timedelta(days=365*100) # 100 years ago
    min_date = today - timedelta(days=365)  # 1 year ago
    print(user_id)
    context = {'max_date': max_date, 'min_date': min_date, 'districts': district,'user_id':user_id}
    return render(request,'form.html',context)