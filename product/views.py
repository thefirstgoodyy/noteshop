from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from product.models import Label, Good


@csrf_protect
def index(request):
    label_list = Label.objects.all()
    context = RequestContext(request, {
        'Labels': label_list
    })
    return render_to_response('index.html', context)


def show_notebooks(request, label):
    notebooks_list = Good.objects.filter(label_id=label)
    label_id = Label.objects.get(id=label)
    label_name = label_id.name
    context = RequestContext(request, {
        'Notebooks': notebooks_list,
        'Label': label_name
    })
    return render_to_response('show.html', context)
