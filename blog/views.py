from django.shortcuts import render

# Create your views here.
from django.views import View

class HomeView(View):
    def get(self,request):
        return render(request,'blog/index.html',{})

class AboutView(View):
    pass