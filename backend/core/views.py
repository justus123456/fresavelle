from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category, Product


def product_data(p):
    return {'id': p.id, 'name': p.name, 'description': p.description, 'unit': p.unit, 'price_kobo': p.price_kobo, 'in_stock': p.stock > 0, 'category': p.category.slug, 'image': p.image_path, 'is_basket': p.is_basket}


@api_view(['GET'])
def health(request):
    return Response({'status': 'ok', 'service': 'fresavelle-api', 'mode': 'local-preview'})


@api_view(['GET'])
def products(request):
    query = request.GET.get('search', '').strip()[:100]
    category = request.GET.get('category', '').strip()[:100]
    sort = request.GET.get('sort', 'default')
    ordering = {'default': 'id', 'name': 'name', 'price-asc': 'price_kobo', 'price-desc': '-price_kobo'}
    if sort not in ordering:
        return Response({'detail': 'Invalid sort option.'}, status=400)
    items = Product.objects.filter(active=True).select_related('category')
    if query:
        items = items.filter(name__icontains=query)
    if category:
        items = items.filter(category__slug=category)
    items = items.order_by(ordering[sort], 'id')
    return Response({'categories': list(Category.objects.order_by('name').values('name', 'slug')[:200]), 'products': [product_data(p) for p in items[:200]], 'count': items.count(), 'limited': items.count() > 200})


@api_view(['GET'])
def product_detail(request, product_id):
    product = get_object_or_404(Product.objects.select_related('category'), pk=product_id, active=True)
    return Response(product_data(product))
