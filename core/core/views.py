from django.views.generic import views;
from django.shortcuts import render;

class HomeView(views):
        def get (self,request,*arg,**kwargs):
            context={
                           

		}
            return render (request, 'index.html'.context);
          