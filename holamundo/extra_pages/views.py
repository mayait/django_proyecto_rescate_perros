from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin



class StarterPageView(LoginRequiredMixin,View):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Starter Page"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Extra Pages"
        return render (request,'extra_pages/extra_pages-starterpage.html',greeting)  

class ErrorView(LoginRequiredMixin,View):
    def get(self, request):
        return render (request,'extra_pages/extra_pages-404error.html')  

class ErrorsView(LoginRequiredMixin,View):
    def get(self, request):
        return render (request,'extra_pages/extra_pages-500error.html')                                      

class MaintenanceView(LoginRequiredMixin,View):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Maintenance"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Extra Pages"
        return render (request,'extra_pages/extra_pages-maintenance.html',greeting)   

class ComingSoonView(LoginRequiredMixin,View):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Coming Soon"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Extra Pages"
        return render (request,'extra_pages/extra_pages-comingsoon.html',greeting)                  


