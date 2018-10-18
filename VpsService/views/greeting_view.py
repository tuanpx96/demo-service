# -*- coding: utf-8 -*-
#
# @author N307
# @create 10/3/2018
#
from django.http import HttpResponse
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_demo(request):
    return HttpResponse("Demo GET method")


@api_view(['PUT'])
def put_demo(request):
    body_utf8 = request.body.decode('utf-8')
    return HttpResponse('Demo PUT method.\nYou say "' + body_utf8 + '\"')




