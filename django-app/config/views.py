from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView


class Index(APIView):
    def get(self, request):
        return Response({
            'snippets': reverse('snippet-list', request=request)
        })
