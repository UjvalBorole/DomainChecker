from django.shortcuts import render,redirect
from .models import *
from .forms import *
import pandas as pd
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout
from django.views import View

def test(loc):
    data = pd.read_csv(loc)
    data[' Resolved IP'] = data[' Resolved IP'].fillna('')
    formatted_data = [(row['Domain Name'], row[' Resolved IP']) for _, row in data.iterrows()]
    valid_domains = []
    invalid_domains = []

    for domain, ip in formatted_data:
        if "-icicibank.com" in domain:
            valid_domains.append((domain, ip))
        elif "icicibank.com" == domain:
            valid_domains.append((domain, ip))
        elif ".icicibank.com" in domain:
            valid_domains.append((domain, ip))
        else:
            invalid_domains.append((domain, ip))
    hgd = [valid_domains,invalid_domains]
    return hgd

@login_required
def valid_data(request):
    try:
        user = request.user
        path = Path.objects.filter(user = user)
        loc = path[len(path)-1]
        data = test(loc.path)
        data1 = data[0]
        length = len(data1)
        return render(request,"data.html",{"data1":data1,"user":user,"isvalid":"valid_data","length":length})
    except:
        return render(request,"error.html")
        

@login_required
def Invalid_data(request):
    try:
        user = request.user
        path = Path.objects.filter(user = user)
        loc = path[len(path)-1]
        data = test(loc.path)
        data1 = data[1]
        length = len(data1)
        return render(request,"data.html",{"data1":data1,"user":user,"isvalid":"Invalid_data","length":length})
    except:
        return render(request,"error.html")

        
@login_required
def home(request):
    if(request.method == "POST"):
        user = request.user
        file =request.POST.get('file')
        print(file)
        dat = str(file)
        data = f'app/static/{dat}'
        if(dat != None ):
            Path(user = user,path= data).save()
        print(data)
        path = Path.objects.filter(user = user)
        inst = path[len(path)-1]
        # print(inst.path)
        return render(request,'home.html')
    if(request.method == "GET"):
        return render(request,'home.html')
    
@login_required
def index(request):
    return render(request,"base.html")

@login_required
def profile(request):
    try:
        user = request.user
        path = Path.objects.filter(user = user)
        loc = path[len(path)-1]
        data = test(loc.path)
        data1 = len(data[0])
        data2 = len(data[1])
        valid_data = {}
        invalid_data = {}
        for i in range(5):
            valid_data[data[0][i][0]] = data[0][i][1]

        for i in range(5):
            invalid_data[data[1][i][0]] = data[0][i][1]
        return render(request,"profile.html",{"email":request.user.email,"valid_data":valid_data,"data1":data1,"data2":data2,"invalid_data":invalid_data})
    except:
        return render(request,"error.html")




class customerregistration(View):
    def get(self, request):
        fm = CustomerRegistrationForm()
        return render(request, 'auth/customerregistration.html', {'form': fm})

    def post(self, request):
        fm = CustomerRegistrationForm(data=request.POST)
        if fm.is_valid():
            # messages.success(request,'Congratulations !! Register Successfully')
            fm.save()
        return render(request, 'auth/customerregistration.html', {'form': fm})
        # return redirect('login')



@login_required
def custom_logout(request):
    data = Path.objects.filter(user = request.user)
    for i in range(len(data)):
        data[i].delete()
    logout(request)
    return redirect("login")