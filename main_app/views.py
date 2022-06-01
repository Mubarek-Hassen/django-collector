from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
#...
from django.views.generic.base import TemplateView
# This will import the class we are extending 
from django.views.generic.edit import CreateView
# after our other imports 
from .models import onechibi
from django.views.generic import DetailView
# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = "home.html"


#...
class About(TemplateView):
    template_name = "about.html"

# class onechibi:
#     def __init__(self, name, image):
#         self.name = name
#         self.image = image

# chibi = [
#     onechibi('groot','https://i.pinimg.com/564x/31/d7/33/31d733469baa6e4912a587615896fdd6.jpg'),
#     onechibi('Ghost','https://cdn11.bigcommerce.com/s-2qk6gvu0p8/products/168/images/431/GhostRiley1pc__47989.1635880685.386.513.jpg?c=1')
# ]

class collections(TemplateView):
    template_name = 'collections.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["chibi"] = onechibi.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context['chibi'] = onechibi.objects.all()
            context["header"] = 'Trending Chibi'
        return context

class AddChibi(CreateView):
    model = onechibi
    fields = ['name','img','bio','verified_chibi']
    template_name = "chibi_add.html"
    success_url = "/collections/"

class ChibiDetail(DetailView):
    model = onechibi
    template_name = "chibi_detail.html"