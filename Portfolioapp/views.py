
from asyncio import sleep
from asyncio.windows_events import NULL
from email import message
from importlib.resources import path
from pyexpat.errors import messages
import time
import django
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import redirect, render

from Portfolioapp.models import MessegeDb
from django.contrib import messages
# Create your views here.
def  firstPage(request):
    return render(request,'index.html')


def MessegeData(request):

    if request.method=='POST':
        m_name=request.POST.get('name')
        m_email=request.POST.get('email')
        m_subject=request.POST.get('subject')    
        m_message=request.POST.get('message')

        m_data=MessegeDb(name=m_name,email=m_email,subject=m_subject,message=m_message)
        m_data.save()

        messages.success(request,'Thanks for share your Message.i will replay back when i see :) ')
        
    time.sleep(5)      
    return redirect(firstPage)