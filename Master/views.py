from django.http.response import JsonResponse
from django.shortcuts import render
from Master.forms import *
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from Master.models import *

# Create your views here.

def home(request):
    dict = {}
    return render(request, 'master/base.html', context=dict)

def viewmobiles(request):
    
    
    mobile = Mobiles.objects.all()

    context  = {
        'mobile' : mobile,
        
    }
    print(context)
    return render(request, 'master/view.html', context)

def createmobiles(request):
    
    form = MobileForm()

    if request.method == 'POST':
        form = MobileForm(request.POST, request.FILES)
        try:
            if form.is_valid():
                data = form.save(commit = False)
                
                data.save()
                return redirect('viewmobiles') 
        except Exception as e:
            messages.error(request, str(e))
         

    context  = {
        'form' : form,
        
    }
    return render(request, 'master/add_mobile.html', context)


def delete(request, varCode):
    

    deletedVal = Mobiles.objects.get(id = varCode)
    print(deletedVal)

    if request.method == 'POST':
        try:
            deletedVal.delete()
            return redirect('viewmobiles')  
        except Exception as e:
            messages.error(request, str(e))  

    context  = {
        
        'deletedVal' : deletedVal,
        
    }
    return render(request, 'master/delete.html', context)


def search(request):
    
    results = Mobiles.objects.all()
    print(results)
    
    context = {
        'results' : results,
        
    }
    print(context)
        
    return render(request, 'master/search.html', context)


def searchoutput(request):
    
    
    if request.is_ajax():
        res = None
        model = request.POST.get('model')
        jan = request.POST.get('jan')
        print(model)
        results = Mobiles.objects.filter(Q(model__icontains=model) & Q(jan__icontains=jan))
        if len(results) > 0:
            data = []
            for i in results:
                item = {
                    'brand': i.brand,
                    'model': i.model,
                    'color': i.color,
                    'jan': i.jan,
                    'image': str(i.image),
                    
                }
                data.append(item)
            res = data
        else:
            res = []
    
    
    
        print(results)
        return JsonResponse({'data': res})
    return JsonResponse({})
    

def viewdetails(request, varCode):
    
    mobile = Mobiles.objects.get(id = varCode)
    print(mobile)

    

    context = {
        'mobile' : mobile,
        
        

    }
    return render(request, 'master/details.html',context )

