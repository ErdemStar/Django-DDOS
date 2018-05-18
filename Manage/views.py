# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from Scripts.Hello import *
from django.http import HttpResponseRedirect


def redirect(request):
    return HttpResponseRedirect("index")

def index(request):
    return render( request , "index.html" , {})

def Http_Flood(request):
    if request.method == "POST":
        dst     = request.POST["dst"]
        port    = request.POST["dport"]
        flag    = request.POST["flag"]
        count   = request.POST["count"]
        print dst,port,flag,count

    return render(request, "Http_Flood.html", {})
