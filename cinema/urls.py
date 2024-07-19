from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallList,
    CinemaHallDetail, MovieViewSet,
)

cinema_hall_list = CinemaHallList.as_view(
    actions={"get": "list", "post": "create"}
)
cinema_hall_detail = CinemaHallDetail.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy"
    }
)
router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("halls/", cinema_hall_list, name="cinema-hall-list"),
    path("halls/<int:pk>/", cinema_hall_detail, name="cinema-hall-detail"),
    path("", include(router.urls)),
]

app_name = "cinema"
