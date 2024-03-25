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
    hu = HistoryUpdate.objects.all
    ni = NodeInfo.objects.all
    context['HistoryUpdateAll'] = hu
    context['NodeInfoAll'] = ni
    
    c1x = HistoryUpdate.objects.values_list('soil_temp_0')
    c1y = HistoryUpdate.objects.values_list('update_time')
    chart_data1 = {
        'x': c1x,
        'y': c1y,
    }
    print(chart_data1)
    context["chart_data1"] = chart_data1

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
            dashboard(request)
        
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
