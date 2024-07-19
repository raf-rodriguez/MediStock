from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# Definir el enrutador para manejar las vistas basadas en ViewSets
router = DefaultRouter()
router.register(r'appuser', AppUserViewSet)
router.register(r'storage', StorageViewSet)
router.register(r'medication', MedicationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserCreate.as_view(), name='register'),
    path('login/', LoginAuthorization.as_view(), name='login'), 
    path('logout/', Logout.as_view(), name='logout'),
    path('medication/user/<int:user_id>/', UserMedicationView.as_view(), name='user_medication'),
    path('medication/latest/<int:user_id>/', LatestUserMedicationListView.as_view(), name='latest-user-medication-list'),
    path('storage/user/<int:user_id>/', UserStorageListView.as_view(), name='user_storage'),
    path('storage/latest/<int:user_id>/', LatestUserStorageListView.as_view(), name='latest-user-storage-list'),
]
