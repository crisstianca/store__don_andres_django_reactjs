
from rest_framework import viewsets
from .serializers import ProductsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Products

# Create your views here.
class ProductsView(viewsets.ModelViewSet):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category=category)
        return queryset

@api_view(['GET'])
def categories(request):
    choices = [{"value": c[0], "label": c[1]} for c in Products.CATEGORY_CHOICES]
    return Response(choices)