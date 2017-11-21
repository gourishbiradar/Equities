from django.http import HttpResponse
from django.shortcuts import render, redirect,render_to_response
from django.contrib.auth import login, authenticate
from .models import *
from .forms import *
#from djanfo.forms.models import inlineformset_factory
#from django.core.exceptions import PermissionDenied
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

app_name='Equity'

@login_required
def home(request):
    return render(request,"Equity/home.html")

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            current_site = get_current_site(request)
            return redirect('DashBoard')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def MostVolatileDeriavatives(request):
    if request.method=='POST':
        form=VolatileDeriavativesForm(request.POST)
        d=[]
        if form.is_valid():
            dtype=form.cleaned_data['selectType']
            if dtype=='Futures':
                #return redirect("DisplayVolatileFutures")
                deriavatives=Most_Volatile_Futures.objects.all()
            else:
                deriavatives=Most_Volatile_Options.objects.all()
                #return redirect("DisplayVolatileOptions")
                
    else:
        form=VolatileDeriavativesForm()
        deriavatives=""
        d=""
    return render(request,'Equity/MostVolatileDeriavatives.html', {'form': form,'deriavatives':deriavatives}) 

@login_required
def SpecificDeriavatives(request):
    if request.method=='POST':
        form=DeriavativesForm(request.POST)
        if form.is_valid():
            dtype=form.cleaned_data['selectType']
            date1=form.cleaned_data['selectDate']
            symbol1=form.cleaned_data['selectSymbol']
            if dtype=='Futures':
                try:
                    deriavative=Futures.objects.get(TimeS__exact=date1,symbol__exact=symbol1)
                    FutSer=FutureSearches(user=request.user,symbol=deriavative)
                    FutSer.save()
                except:
                    deriavative="Input data is invalid!"
                #return redirect("DisplayFutures",date=date1,symbol=symbol1)
            else:
                try:
                    deriavative=Options.objects.get(TimeS__exact=date1,symbol__exact=symbol1)
                    OptSer=OptionSearches(user=request.user,symbol=deriavative)
                    OptSer.save()
                except:
                    deriavative="Input data is invalid!"
                #return redirect("DisplayOptions",date=date1,symbol=symbol1)
    else:
            form=DeriavativesForm()
            deriavative=""
    return render(request,"Equity/Deriavatives.html",{'form': form,'deriavative':deriavative})

@login_required
def SectorwisePerformances(request):
    if request.method=='POST':
        form=SectorForm(request.POST)
        if form.is_valid():
            sname1=form.cleaned_data['sectorName']
            #sector=Sectors.object.get(sname__exact=sname1)
            try:
                sector=Sectors.objects.get(sname__exact=sname1)
            except:
                sector="Input data is invalid!"
    else:
        form=SectorForm()
        sector=""
    return render(request,"Equity/SectorWisePerformance.html",{'form':form,'sector':sector})

@login_required
def FutureInv(request):
    if request.method=='POST':
        form=FutureInvForm(request.POST)
        d=[]
        if form.is_valid():
            symb=form.cleaned_data['selectSymbol']
            date1=form.cleaned_data['selectDate']
            quantity=form.cleaned_data['quantity']
            try:
                deriavative=Futures.objects.get(TimeS__exact=date1,symbol__exact=symb)
                uif=UserFutures(user=request.user,symbol=deriavative,quantity=quantity)
                uif.save()
                obj=UserFutures.objects.filter(user=request.user)
                for q in obj:
                    f=Futures.objects.get(id=q.symbol_id)
                    d.append(f)
            except:
                d="No Future with the given data"
    else:
        form=FutureInvForm()
        d=""
        obj=""
    return render(request,"Equity/FutureInv.html",{'form':form,'d':d})

@login_required
def History(request):
    fut=[]
    opt=[]
    futs=FutureSearches.objects.filter(user=request.user)
    opts=OptionSearches.objects.filter(user=request.user)
    for x in futs:
        f=Futures.objects.get(id=x.symbol_id)
        fut.append(f)
    for y in opts:
        o=Options.objects.get(id=y.symbol_id)
        opt.append(o)
    return render(request,"Equity/History.html",{'fut':fut,'opt':opt})

@login_required
def OptionInv(request):
    if request.method=='POST':
        form=OptionInvForm(request.POST)
        d=[]
        if form.is_valid():
            symb=form.cleaned_data['selectSymbol']
            date1=form.cleaned_data['selectDate']
            quantity=form.cleaned_data['quantity']
            try:
                deriavative=Options.objects.get(TimeS__exact=date1,symbol__exact=symb)
                uif=UserOptions(user=request.user,symbol=deriavative,quantity=quantity)
                uif.save()
                obj=UserOptions.objects.filter(user=request.user)
                for q in obj:
                    f=Options.objects.get(id=q.symbol_id)
                    d.append(f)
            except:
                d="No Option with the given data"
    else:
        form=OptionInvForm()
        d=""
    return render(request,"Equity/OptionInv.html",{'form':form,'d':d})


def AboutUs(request):
    return render(request,"Equity/AboutUs.html")

def ContactUs(request):
    return render(request,"Equity/ContactUs.html")

@login_required
def DashBoard(request):
    return render(request,"Equity/DashBoard.html")

