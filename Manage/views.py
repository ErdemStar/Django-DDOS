# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from Scripts.Hello import *



def index(request):
    Hi()
    return render( request , "index.html" , {})