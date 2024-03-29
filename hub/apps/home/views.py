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


def get_graph_data(val_list_x1, val_list_x2, val_list_x3, val_list_y):
    dic = json.dumps({
        'value1': val_list_x1,
        'value2': val_list_x2,
        'value3': val_list_x3,
        'labels': val_list_y
    })
    return dic

def get_average(n1, n2, n3, name):
    n1 = list(n1.values_list(name, flat=True))
    n2 = list(n2.values_list(name, flat=True))
    n3 = list(n3.values_list(name, flat=True))
    n = []
    for i in range(len(n1)):
        n.append((n1[i]+n2[i]+n3[i])/3)
    return n

def blocks(latest, last_latest, namelist, roundto):
    new = []
    old = []
    for name in namelist:
        new = new + list(latest.values_list(name, flat=True))
        old = old + list(last_latest.values_list(name, flat=True))
    newmax = round(max(new), 2)
    newmin= round(min(new), 2)
    avg = sum(new)/len(new)
    last_avg = sum(old)/len(old)
    diff = round(avg-last_avg, roundto)
    ratio = round(((avg-last_avg)/avg) * 100, roundto)
    return newmax, newmin, diff, ratio

@login_required(login_url="/login/")
def dashboard(request):
    context = {'segment': 'dashboard'}
    hu = HistoryUpdate.objects.filter().order_by('-id')[:6]
    hu = reversed(hu)
    ni = NodeInfo.objects.all()
    context['hu'] = hu
    context['ni'] = ni
    # three node
    node1 = HistoryUpdate.objects.filter(node_id=1).order_by('id')
    node2 = HistoryUpdate.objects.filter(node_id=2).order_by('id')
    node3 = HistoryUpdate.objects.filter(node_id=3).order_by('id')
    # update_time
    update_time = list(node1.values_list('update_time', flat=True))
    update_time = [str(y.month)+'-'+str(y.day)+' '+str(y.hour)+":00" for y in update_time]

    # soil_temp
    soil_temp_0 = get_average(node1, node2, node3, "soil_temp_0")
    soil_temp_10 = get_average(node1, node2, node3, "soil_temp_10")
    soil_temp_20 = get_average(node1, node2, node3, "soil_temp_20")
    context["c1"] = get_graph_data(soil_temp_0, soil_temp_10, soil_temp_20, update_time)
    
    # the upper four blocks
    latest = HistoryUpdate.objects.filter().order_by('-id')[:3]
    last_latest = HistoryUpdate.objects.filter().order_by('-id')[3:6]
    context["tmax"], context["tmin"], context["tdiff"] ,context["tratio"] = blocks(latest, last_latest, ["soil_temp_0", "soil_temp_10", "soil_temp_20"], 2)
    context["mmax"], context["mmin"], context["mdiff"], context["mratio"] = blocks(latest, last_latest, ["soil_moisture_0", "soil_moisture_10", "soil_moisture_20"], 2)
    context["phmax"], context["phmin"], context["phdiff"], context["phratio"] = blocks(latest, last_latest, ["ph_0", "ph_10", "ph_20"], 2)
    context["limax"], context["limin"], context["lidiff"], context["liratio"] = blocks(latest, last_latest, ["light_intensity_0"], -2)

    html_template = loader.get_template('home/dashboard.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
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
            # three node
            node1 = HistoryUpdate.objects.filter(node_id=1).order_by('id')
            node2 = HistoryUpdate.objects.filter(node_id=2).order_by('id')
            node3 = HistoryUpdate.objects.filter(node_id=3).order_by('id')
            # update_time
            update_time = list(node1.values_list('update_time', flat=True))
            update_time = [str(y.month)+'-'+str(y.day)+' '+str(y.hour)+":00" for y in update_time]

            # soil_temp
            soil_temp_0 = get_average(node1, node2, node3, "soil_temp_0")
            soil_temp_10 = get_average(node1, node2, node3, "soil_temp_10")
            soil_temp_20 = get_average(node1, node2, node3, "soil_temp_20")
            context["c1"] = get_graph_data(soil_temp_0, soil_temp_10, soil_temp_20, update_time)
            
            # the upper four blocks
            latest = HistoryUpdate.objects.filter().order_by('-id')[:3]
            last_latest = HistoryUpdate.objects.filter().order_by('-id')[3:6]
            context["tmax"], context["tmin"], context["tdiff"] ,context["tratio"] = blocks(latest, last_latest, ["soil_temp_0", "soil_temp_10", "soil_temp_20"], 2)
            context["mmax"], context["mmin"], context["mdiff"], context["mratio"] = blocks(latest, last_latest, ["soil_moisture_0", "soil_moisture_10", "soil_moisture_20"], 2)
            context["phmax"], context["phmin"], context["phdiff"], context["phratio"] = blocks(latest, last_latest, ["ph_0", "ph_10", "ph_20"], 2)
            context["limax"], context["limin"], context["lidiff"], context["liratio"] = blocks(latest, last_latest, ["light_intensity_0"], -2)

            html_template = loader.get_template('home/dashboard.html')
            return HttpResponse(html_template.render(context, request))
        
        elif load_template == 'dashboardmoisture.html':
            context = {'segment': 'dashboardmoisture'}
            hu = HistoryUpdate.objects.filter().order_by('-id')[:6]
            hu = reversed(hu)
            ni = NodeInfo.objects.all()
            context['hu'] = hu
            context['ni'] = ni
            # three node
            node1 = HistoryUpdate.objects.filter(node_id=1).order_by('id')
            node2 = HistoryUpdate.objects.filter(node_id=2).order_by('id')
            node3 = HistoryUpdate.objects.filter(node_id=3).order_by('id')
            # update_time
            update_time = list(node1.values_list('update_time', flat=True))
            update_time = [str(y.month)+'-'+str(y.day)+' '+str(y.hour)+":00" for y in update_time]

            # soil_temp
            soil_temp_0 = get_average(node1, node2, node3, "soil_moisture_0")
            soil_temp_10 = get_average(node1, node2, node3, "soil_moisture_10")
            soil_temp_20 = get_average(node1, node2, node3, "soil_moisture_20")
            context["c1"] = get_graph_data(soil_temp_0, soil_temp_10, soil_temp_20, update_time)
            
            # the upper four blocks
            latest = HistoryUpdate.objects.filter().order_by('-id')[:3]
            last_latest = HistoryUpdate.objects.filter().order_by('-id')[3:6]
            context["tmax"], context["tmin"], context["tdiff"] ,context["tratio"] = blocks(latest, last_latest, ["soil_temp_0", "soil_temp_10", "soil_temp_20"], 2)
            context["mmax"], context["mmin"], context["mdiff"], context["mratio"] = blocks(latest, last_latest, ["soil_moisture_0", "soil_moisture_10", "soil_moisture_20"], 2)
            context["phmax"], context["phmin"], context["phdiff"], context["phratio"] = blocks(latest, last_latest, ["ph_0", "ph_10", "ph_20"], 2)
            context["limax"], context["limin"], context["lidiff"], context["liratio"] = blocks(latest, last_latest, ["light_intensity_0"], -2)

            html_template = loader.get_template('home/dashboardmoisture.html')
            return HttpResponse(html_template.render(context, request))
        
        elif load_template == 'dashboardph.html':
            context = {'segment': 'dashboardph'}
            hu = HistoryUpdate.objects.filter().order_by('-id')[:6]
            hu = reversed(hu)
            ni = NodeInfo.objects.all()
            context['hu'] = hu
            context['ni'] = ni
            # three node
            node1 = HistoryUpdate.objects.filter(node_id=1).order_by('id')
            node2 = HistoryUpdate.objects.filter(node_id=2).order_by('id')
            node3 = HistoryUpdate.objects.filter(node_id=3).order_by('id')
            # update_time
            update_time = list(node1.values_list('update_time', flat=True))
            update_time = [str(y.month)+'-'+str(y.day)+' '+str(y.hour)+":00" for y in update_time]

            # soil_temp
            soil_temp_0 = get_average(node1, node2, node3, "ph_0")
            soil_temp_10 = get_average(node1, node2, node3, "ph_10")
            soil_temp_20 = get_average(node1, node2, node3, "ph_20")
            context["c1"] = get_graph_data(soil_temp_0, soil_temp_10, soil_temp_20, update_time)
            
            # the upper four blocks
            latest = HistoryUpdate.objects.filter().order_by('-id')[:3]
            last_latest = HistoryUpdate.objects.filter().order_by('-id')[3:6]
            context["tmax"], context["tmin"], context["tdiff"] ,context["tratio"] = blocks(latest, last_latest, ["soil_temp_0", "soil_temp_10", "soil_temp_20"], 2)
            context["mmax"], context["mmin"], context["mdiff"], context["mratio"] = blocks(latest, last_latest, ["soil_moisture_0", "soil_moisture_10", "soil_moisture_20"], 2)
            context["phmax"], context["phmin"], context["phdiff"], context["phratio"] = blocks(latest, last_latest, ["ph_0", "ph_10", "ph_20"], 2)
            context["limax"], context["limin"], context["lidiff"], context["liratio"] = blocks(latest, last_latest, ["light_intensity_0"], -2)

            html_template = loader.get_template('home/dashboardph.html')
            return HttpResponse(html_template.render(context, request))

        elif load_template == 'dashboardli.html':
            context = {'segment': 'dashboardli'}
            hu = HistoryUpdate.objects.filter().order_by('-id')[:6]
            hu = reversed(hu)
            ni = NodeInfo.objects.all()
            context['hu'] = hu
            context['ni'] = ni
            # three node
            node1 = HistoryUpdate.objects.filter(node_id=1).order_by('id')
            node2 = HistoryUpdate.objects.filter(node_id=2).order_by('id')
            node3 = HistoryUpdate.objects.filter(node_id=3).order_by('id')
            # update_time
            update_time = list(node1.values_list('update_time', flat=True))
            update_time = [str(y.month)+'-'+str(y.day)+' '+str(y.hour)+":00" for y in update_time]

            # soil_temp
            soil_temp_0 = get_average(node1, node2, node3, "light_intensity_0")
            context["c1"] = get_graph_data(soil_temp_0, [], [], update_time)
            
            # the upper four blocks
            latest = HistoryUpdate.objects.filter().order_by('-id')[:3]
            last_latest = HistoryUpdate.objects.filter().order_by('-id')[3:6]
            context["tmax"], context["tmin"], context["tdiff"] ,context["tratio"] = blocks(latest, last_latest, ["soil_temp_0", "soil_temp_10", "soil_temp_20"], 2)
            context["mmax"], context["mmin"], context["mdiff"], context["mratio"] = blocks(latest, last_latest, ["soil_moisture_0", "soil_moisture_10", "soil_moisture_20"], 2)
            context["phmax"], context["phmin"], context["phdiff"], context["phratio"] = blocks(latest, last_latest, ["ph_0", "ph_10", "ph_20"], 2)
            context["limax"], context["limin"], context["lidiff"], context["liratio"] = blocks(latest, last_latest, ["light_intensity_0"], -2)

            html_template = loader.get_template('home/dashboardli.html')
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
        
        elif load_template == "node1analysis-temp.html":
            node1 = HistoryUpdate.objects.filter(node_id=1)
            date = list(node1.objects.values_list('update_time', flat=True))
            temp0 = list(node1.objects.values_list('soil_temp_0', flat=True))
            
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
