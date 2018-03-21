from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
from django.contrib import messages

from models import *

# Create your views here.
def index(request):
    print "hello!"
    if 'order_history_cost' not in request.session:
        request.session['order_history_quantity'] = 0
        request.session['order_history_cost'] = 0
        request.session['order_total_cost'] = 0
    else:
        request.session['order_total_cost'] = 0
    return render(request, 'amadon/index.html')

def checkout(request):
    print "Checking out"

    prices = {
        'tshirt': float(19.99),
        'sweater': float(29.99),
        'cup': float(4.99),
        'book': float(49.99)
    }
    print prices

    # calculate this order
    request.session['quantity'] = int(request.POST['quantity'])
    request.session['price'] = float(prices[request.POST['product_id']])
    print "request.session['quantity']: ", request.session['quantity'], "request.session['price']: ", request.session['price']
    request.session['order_total_cost'] = float(request.session['quantity'])*float(request.session['price'])
    print "request.session['order_total_cost']: ", request.session['order_total_cost']

    # add this order to order history
    request.session['order_history_quantity'] += int(request.session['quantity'])
    print "request.session['order_history_quantity']: ", request.session['order_history_quantity']

    request.session['order_history_cost'] += float(request.session['order_total_cost'])
    print "request.session['order_history_cost']: ", request.session['order_history_cost']

    #
    #
    # if 'order_history_quantity' not in request.session:
    #     print "This is your first order."
    #     request.session['order_history_quantity'] = int(request.session['quantity'])
    #     print "request.session['order_history_quantity']: ", request.session['order_history_quantity']
    # else:
    #     request.session['order_history_quantity'] += int(request.session['order_history_quantity'])
    #     print "request.session['order_history_quantity']: ", request.session['order_history_quantity']
    # if 'order_history_cost' not in request.session:
    #     print "This is your first order."
    #     request.session['order_history_cost'] = float(request.session['order_total_cost'])
    #     print "request.session['order_history_cost']: ", request.session['order_history_cost']
    # else:
    #     request.session['order_history_cost'] += float(request.session['order_history_cost'])
    #     print "request.session['order_history_cost']: ", request.session['order_history_cost']

    return redirect('/amadon/review')

def review(request):
    return render(request, 'amadon/result.html')

def reset(request):
    print "You have logged out and cleared the session."
    request.session.clear()
    return redirect('/')
