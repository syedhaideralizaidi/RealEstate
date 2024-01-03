from django.urls import path
from realtors.views import RealtorListView, RealtorDetailView, TopSellerListView

app_name = "realtors"

urlpatterns = [
    path("", RealtorListView.as_view()),
    path("topsellers/", TopSellerListView.as_view()),
    path("<int:pk>/", RealtorDetailView.as_view()),
]
