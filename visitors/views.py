from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from .models import Visitor
from .serializers import VisitorSerializer

# Create your views here.

@api_view(['POST'])
def check_in(request):
    serializer = VisitorSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def check_out(request):
    phone = request.data.get('phone')
    
    if not phone:
        return Response({"error": "phone number is required"}, status=status.HTTP_400_BAD_REQUEST)
    

    try:
        visitor = Visitor.objects.get(
            phone = phone,
            check_out_time__isnull = True
        )

    except Visitor.DoesNotExist:
        return Response({'error': 'no active visits found for this phone number'}, status=status.HTTP_404_NOT_FOUND)
    

    visitor.check_out_time = timezone.now()
    visitor.save()

    serializer = VisitorSerializer(visitor)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def visitors_inside(request):
    visitors = Visitor.objects.filter(check_out_time__isnull=True)
    serializer = VisitorSerializer(visitors, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def visitors_by_date(request):
    date = request.query_params.get('date')

    if not date:
        return Response({'error': 'date is required'}, status=status.HTTP_400_BAD_REQUEST)
    visitors = Visitor.objects.filter(check_in_time__date=date)
    serializer = VisitorSerializer(visitors, many = True)
    return Response(serializer.data, status=status.HTTP_200_OK)