from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Youtuber
from .serializers import YoutuberSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from django.views.generic import TemplateView

# Create your views here.

def index(request):
    return render(request, 'index.html')

# 함수형
@api_view(['GET', 'POST'])
def youtuber_list(request):

    if request.method == 'GET':

        subscribers = request.query_params.get('subscribers')
        if subscribers:
            youtubers = Youtuber.objects.filter(subscribers=subscribers) # subscribers가 입력한 값 이상인 쿼리셋
        else:
            youtubers = Youtuber.objects.all() # 쿼리셋
        serializer = YoutuberSerializer(youtubers, many=True) # 쿼리셋을 json 형태로 변경
        return Response(serializer.data)

# post는 애초에 request가 json형태로 들어오기 때문에 '
# request.data를 serializer를 통해서 instance형식으로 바꾸어준다. 
# 그리고 is_valid()로 instance의 유효성을 판단한 후에, database에 데이터를 저장해주는 방식으로 진행한다.
    elif request.method == 'POST':
        serializer = YoutuberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 함수형
@api_view(['GET', 'PUT', 'DELETE'])
def youtuber_detail(request, pk):

    try:
        youtuber = Youtuber.objects.get(pk=pk)
    except Youtuber.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = YoutuberSerializer(youtuber)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = YoutuberSerializer(youtuber, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        youtuber.delete()

class YoutuberViewSet(viewsets.ModelViewSet):
    queryset = Youtuber.objects.all()
    serializer_class = YoutuberSerializer

    def get_queryset(self):
        queryset = Youtuber.objects.all()
        name = self.request.query_params.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class YoutuberView(TemplateView):
    template_name = 'list.vue'
