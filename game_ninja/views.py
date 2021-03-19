from django.shortcuts import render, redirect
import random
from time import gmtime, strftime
def index (request):
    request.session ['farm_gold'] = random.randint(10,20)
    request.session ['cave_gold'] = random.randint(5,10)
    request.session ['house_gold'] = random.randint(2,5)
    request.session ['casino_gold'] = random.randint(-50,50)
    if 'total' not in request.session:
        request.session['total'] = 0
    
    if 'activities' not in request.session:
        request.session['activities'] = []
    
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }

    return render(request, "index.html", context)

def process (request):
    
    

    if (request.POST['location']=='farm'):
        request.session['total'] += request.session ['farm_gold']

        request.session['activities'].append("You earned " + str(request.session ['farm_gold']) + " golds from farm -- " + strftime("%Y-%m-%d %H:%M %p", gmtime()))
    elif(request.POST['location']=='cave'):
        request.session['total'] += request.session ['cave_gold']

        request.session['activities'].append("You earned " + str(request.session ['cave_gold']) + " golds from cave -- " + strftime("%Y-%m-%d %H:%M %p", gmtime()))
    elif(request.POST['location']=='house'):
        request.session['total'] += request.session ['house_gold']

        request.session['activities'].append("You earned " + str(request.session ['house_gold']) + " golds from house -- " + strftime("%Y-%m-%d %H:%M %p", gmtime()))
    elif(request.POST['location']=='casino'):
        request.session['total'] += request.session ['casino_gold']

        if (request.session ['casino_gold']>=0):
            request.session['activities'].append("You earned " + str(request.session ['casino_gold']) + " golds playing in casino -- " + strftime("%Y-%m-%d %H:%M %p", gmtime()))
        else:
            request.session['activities'].append("You lost " + str(request.session ['casino_gold']*-1) + " golds playing in casino -- " + strftime("%Y-%m-%d %H:%M %p", gmtime()))
    return redirect ('/')

def reset (request):
    request.session.flush()
    return redirect ('/')