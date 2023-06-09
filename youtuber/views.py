from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Youtuber, Comment
from .serializers import YoutuberSerializer, CommentSerializer
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

        # name은 contain으로 검색
        name = self.request.query_params.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)

        # 구독자는 이상으로 get
        subscribers = self.request.query_params.get('subscribers')
        if subscribers:
            queryset = queryset.filter(subscribers__gte=subscribers)

        return queryset
    
class YoutuberView(TemplateView):
    template_name = 'list.vue'

# 프론트 작업 추후 예정
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = Comment.objects.all()

        # name은 contain으로 검색
        name = self.request.query_params.get('name')
        if name:
            queryset = queryset.filter(name__exact=name)

        return queryset
