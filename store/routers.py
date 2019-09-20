from rest_framework.routers import DefaultRouter
from products.views import ProductViewSet
from order.views import OrderViewSet
from order_details.views import OrderDetailViewSet
from category.views import CategoryViewSet
from payment.views import PaymentViewSet
from users.views import CreateUserView, UserLoginView, UserViewSet


router = DefaultRouter()
router.register(r'products', ProductViewSet, base_name="product")
router.register(r'orders', OrderViewSet, base_name="order")
router.register(r'order-details', OrderDetailViewSet, base_name="order-details")
router.register(r'category', CategoryViewSet, base_name="category")
router.register(r'payment', PaymentViewSet, base_name="payment")
router.register(r'users', UserViewSet, base_name='users')
