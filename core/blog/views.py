from django.shortcuts import render
from django.views.generic import view

# Create your views here.
class bloglistview(view):
   def get (self,request,*arg,**kwargs):
            context={
                           

		}
            return render (request, 'blog_list.html'.context);
          