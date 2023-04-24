from django.contrib.sites import requests
from django.http import HttpResponse
from django.shortcuts import render
import subprocess, sys
import json
import csv
import pandas as pd
import numpy as np

# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
def index(request):
    return render(request, 'index.html')


def calc(request):
    #p = subprocess.Popen(["powershell.exe",
     #                    "D:\powershell_Script\\functest.ps1"],
    #                    stdout=sys.stdout)
    #p.communicate()

    p = subprocess.Popen(["powershell.exe",
                         "static\securityLog.ps1"],
                      stdout=sys.stdout)
    return render(request, 'index.html')

def dashboardPage(request):

    return render(request, 'dashboardPage.html')
def securityPage(request):
    p = subprocess.check_output(["powershell.exe", "static\securityLog.ps1"])
    securitylog= json.loads(p)
    securitylog_asdict={'securitylog':securitylog}
    print("security output is: ")
    print(securitylog_asdict)
    #print("NAme of machine is: "+output_asdict[output[0]]['MachineName'])
    return render(request, 'securityPage.html',securitylog_asdict)

def systemPage(request):
    p = subprocess.check_output(["powershell.exe", "static\systemLog.ps1"])
    systemlog = json.loads(p)
    systemlog_asdict = {'systemlog': systemlog}
    #print("part of output is: ")
    # print(output_asdict[output])
    # print("NAme of machine is: "+output_asdict[output[0]]['MachineName'])
    return render(request, 'systemPage.html',systemlog_asdict)

def applicationPage(request):
    p = subprocess.check_output(["powershell.exe", "static\\applicationLog.ps1"])
    applicationlog = json.loads(p)
    applicationlog_asdict = {'applicationlog': applicationlog}
    return render(request, 'applicationPage.html',applicationlog_asdict)