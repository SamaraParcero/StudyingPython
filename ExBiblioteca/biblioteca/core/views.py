from typing import Any
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from .models import Livro
from .serializers import LivroSerializer

class JSONResponse(HttpResponse):
  def __init__(self, data,  **kwargs):
    content = JSONRenderer().render(data)
    kwargs['content_type'] = 'application/json'
    super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def livro_list_create(request):
    if request.method == "GET":
        livros = Livro.objects.all()
        serializer = LivroSerializer(livros, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = LivroSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
      return JSONResponse(status = status.HTTP_406_NOT_ACCEPTABLE)  


@csrf_exempt
def livro_detail(request, pk):

    livro = Livro.objects.get(pk=pk)

    if request.method == "GET":
        serializer = LivroSerializer(livro)
        return JSONResponse(serializer.data)

    elif request.method == "PUT":
        serializer = LivroSerializer(livro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        livro.delete()
        return JSONResponse(status=status.HTTP_204_NO_CONTENT)
      
    else:
      return JSONResponse(status = status.HTTP_406_NOT_ACCEPTABLE)
