# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import HistoryUpdate, NodeInfo
import json



@login_required(login_url="/login/")
def dashboard(request):
    context = {'segment': 'dashboard'}
    hu = HistoryUpdate.objects.filter().order_by('-id')[:6]
    hu = reversed(hu)
    ni = NodeInfo.objects.all()
    context['hu'] = hu
    context['ni'] = ni
    print(hu, ni)

    
    c1x = list(HistoryUpdate.objects.values_list('soil_temp_0', flat=True))
    c1y = list(HistoryUpdate.objects.values_list('update_time', flat=True))
    
    chart_data1 = json.dumps({
        'values': c1x,
        'labels': [str(y) for y in c1y],  # Convert datetime or any objects to string if necessary
    })
    
    context["c1"] = chart_data1
    html_template = loader.get_template('home/dashboard.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        load_template = request.path.split('/')[-1]
        context['segment'] = load_template
        print(load_template)
        
        if load_template == 'dashboard.html':
            context = {'segment': 'dashboard'}
            hu = HistoryUpdate.objects.filter().order_by('-id')[:6]
            hu = reversed(hu)
            ni = NodeInfo.objects.all()
            context['hu'] = hu
            context['ni'] = ni
            
            c1x = list(HistoryUpdate.objects.values_list('soil_temp_0', flat=True))
            c1y = list(HistoryUpdate.objects.values_list('update_time', flat=True))
            
            chart_data1 = json.dumps({
                'values': c1x,
                'labels': [str(y) for y in c1y],  # Convert datetime or any objects to string if necessary
            })
            print(c1x, c1y)

            context["c1"] = chart_data1
            html_template = loader.get_template('home/dashboard.html')
            return HttpResponse(html_template.render(context, request))
        
        elif load_template == "each_update_full.html":
            all_data = HistoryUpdate.objects.all
            context['all_data'] = all_data
            html_template = loader.get_template('data_query/' + load_template)
            return HttpResponse(html_template.render(context, request))

        
        elif load_template == "node_information.html":
            all_data = NodeInfo.objects.all
            context['all_data'] = all_data
            html_template = loader.get_template('data_query/' + load_template)
            return HttpResponse(html_template.render(context, request))
        
        elif load_template == "node_1.html":
            all_data = HistoryUpdate.objects.filter(node_id=1)
            context['all_data'] = all_data
            html_template = loader.get_template('data_query/' + load_template)
            return HttpResponse(html_template.render(context, request))
        
        elif load_template == "node_2.html":
            all_data = HistoryUpdate.objects.filter(node_id=2)
            context['all_data'] = all_data
            html_template = loader.get_template('data_query/' + load_template)
            return HttpResponse(html_template.render(context, request))
        
        elif load_template == "node_3.html":
            all_data = HistoryUpdate.objects.filter(node_id=3)
            context['all_data'] = all_data
            html_template = loader.get_template('data_query/' + load_template)
            return HttpResponse(html_template.render(context, request))
        

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))
            

    except template.TemplateDoesNotExist:
        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
