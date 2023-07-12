from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ScannersSerializer
from .models import Scanners

class ScannersViews(APIView):
    def get(self, request):
        sn = self.request.query_params.get('scanner')
        if sn:
            item = Scanners.objects.filter(sn=sn)
            print(item, item.count())
            serializer = ScannersSerializer(item, many=True)
            return Response({"total": item.count(), "items": serializer.data}, status=status.HTTP_200_OK)

        items = Scanners.objects.all()
        serializer = ScannersSerializer(items, many=True)
        return Response({"total": item.count(), "items": serializer.data}, status=status.HTTP_200_OK)
