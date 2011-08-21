from django.shortcuts import render_to_response
from django.template import RequestContext

def homepage(request):
	from django.conf import settings
	context = RequestContext(request)
	return render_to_response('index.html', context)
