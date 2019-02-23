from rest_framework.routers import DefaultRouter
from products.views import ProductViewSet, StorageViewSet, SellViewSet, ClientViewSet, CartViewSet

router = DefaultRouter()

router.register(r'clients', ClientViewSet, base_name="client")
router.register(r'products', ProductViewSet, base_name="product")
router.register(r'storages', StorageViewSet, base_name="storage")
router.register(r'sells', SellViewSet, base_name="buy")
router.register(r'carts', CartViewSet, base_name="cart")