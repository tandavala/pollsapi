from django.urls import path
from rest_framework.routers import DefaultRouter

from .apiviews import PollList, PollDetail, ChoiceList, CreateVote, PollViewSet

router = DefaultRouter()
router.register('', PollViewSet, basename='polls')

urlpatterns = [
    #path("", PollList.as_view(), name='polls_list'),
    #path('<int:pk>/', PollDetail.as_view(), name='polls_details'),
    path("<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
]

urlpatterns += router.urls
