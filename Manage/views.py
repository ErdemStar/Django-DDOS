# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponseRedirect

from Scripts.HTTP.httpFlood import HTTPFlood
from Scripts.TCP.tcpFlood import TCPFlood
from Scripts.PDF.createPDF import CreatePDF
from Scripts.LIVE.isAlive import isAlive
from Scripts.UDP.udpFlood import UDPFlood
from Scripts.RESOLVE.DomainResolve import Resolve



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

def Tcp_Flood(request):
    if request.method == "POST":
        dst = request.POST["dst"]
        dport = request.POST["dport"]
        flag = request.POST["flag"]
        count = request.POST["count"]

        if "http" in dst:
            tut = Resolve(dst)
            dst = tut.Get()
            print dst

        tmp = TCPFlood(dst,dport,flag,count)
        tmp.ThreadStart()

        gecici = isAlive(dst,dport)
        CreatePDF("TCP Flood",gecici)

        return render(request,"Tcp_Flood.html" , {})
    elif request.method == "GET":
        return render(request,"Tcp_Flood.html" , {})

def Udp_Flood(request):
    if request.method == "POST":
        dst = request.POST["dst"]
        dport = request.POST["dport"]
        count = request.POST["count"]

        if "http" in dst:
            tut = Resolve(dst)
            dst = tut.Get()
            print dst

        tmp = UDPFlood(dst,dport,count)
        tmp.ThreadStart()

        gecici = isAlive(dst,dport)
        CreatePDF("UDP Flood",gecici)

        return render(request, "Udp_Flood.html", {})

    if request.method == "GET":
        return render(request, "Udp_Flood.html", {})
