from rest_framework.routers import DefaultRouter

from bills.views import BillViewSet
from client.views import ClientViewSet
from products.views import ProductViewSet
from storage.views import StorageViewSet
from sells.views import SellViewSet
from cart.views import CartViewSet
from users.views import CreateUserView

router = DefaultRouter()


router.register(r'clients', ClientViewSet, base_name="client")
router.register(r'products', ProductViewSet, base_name="product")
router.register(r'storages', StorageViewSet, base_name="storage")
router.register(r'sells', SellViewSet, base_name="buy")
router.register(r'carts', CartViewSet, base_name="cart")
router.register(r'bills', BillViewSet, base_name="bill")