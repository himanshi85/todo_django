from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
    template = loader.get_template('first.html')
    return HttpResponse(template.render())


def allmembers(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))


def namedetails(request, name):
  mymember = Member.objects.get(firstname=name)
  print(f"->>>>>>> {mymember}")
  template = loader.get_template('first.html')
  context = {
    'members': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())