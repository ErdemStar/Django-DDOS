# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from Scripts.httpFlood import HTTPFlood
from django.http import HttpResponseRedirect


def redirect(request):
    return HttpResponseRedirect("index")

def index(request):
    return render( request , "index.html" , {})

def Http_Flood(request):
    if request.method == "POST":
        dst     = request.POST["dst"]
        port    = 80
        flag    = "S"
        payload = request.POST["payload"]
        count   = request.POST["count"]


        attack = HTTPFlood(dst,port,flag,payload,count)
        attack.Start()
        return render(request, "Http_Flood.html", {})
    elif request.method == "GET":
        return render(request, "Http_Flood.html", {})
