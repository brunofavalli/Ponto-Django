#-*- encoding: utf-8 -*-
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext
from models import Crud
from forms import FormCrud



# Create your views here.

# Página inicial
def lista(request):
	lista_itens = Crud.objects.all()
	return render_to_response("lista.html",{"lista_itens":lista_itens},context_instance=RequestContext(request))

# Método POST para inclusão de dados
def adiciona(request):
	if request.method == 'POST':
		form = FormCrud(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return render_to_response("salvo.html",{})
	else:
		form = FormCrud() 

	return render_to_response("adiciona.html",{'form':form},context_instance=RequestContext(request))


def item(request, nr_item):
	item = get_object_or_404(Crud, pk=nr_item)
	if request.method == 'POST':
		form = FormCrud(request.POST, request.FILES, instance=item)
		if form.is_valid():
			form.save()
			return render_to_response("salvo.html",{})
	else:
		form = FormCrud(instance=item)
	return render_to_response('item.html',{'form':form},context_instance=RequestContext(request))

def remove(request, nr_item):
	item = get_object_or_404(Crud, pk=nr_item)
	if request.method == "POST":
		item.delete()
		return render_to_response("removido.html",{})
	return render_to_response('remover.html',{'item':item})
	

