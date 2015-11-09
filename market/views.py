from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic.list import ListView
from market.models import Product, Label

#zdes nahodyatsya kontrolleri
#lable poluchenie vseh obektov iz modelei lable
def index(request):
    label_list=Label.objects.all()
    # dannie kotorie peredaiutsya na html
    context=RequestContext(request,{
        'Labels':label_list
    })
    return render_to_response('index.html', context)

# class LabelsList(ListView):
#     model = Label
#     template_name = 'index.html'

#polu4aet label.id i otobrajaet vse noutbuki dannogo label
def show_notebooks(request, label):
#poluchaet vse modeli noutbukov kotorie imeet label_id poluchennomu label
    notebooks_list = Product.objects.filter(label_id=label)
#poluchaet odnu model label gde label.id = label
    label_id=Label.objects.get(id=label)
#poluchaem imya label cherez obekt
    label_name=label_id.name
    context = RequestContext(request, {
        'Notebooks': notebooks_list,
        'Label':label_name
    })
    return render_to_response('show.html', context)


