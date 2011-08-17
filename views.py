from django.http import HttpResponse

def index(request):
    return HttpResponse('you sent %r' % (request.raw_post_data,))
