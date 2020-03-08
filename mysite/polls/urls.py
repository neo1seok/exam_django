from django.urls import path
from rest_framework import routers
from django.urls import include, path
from . import views
app_name = 'polls'

router = routers.DefaultRouter()
router.register(r'question', views.QuestionViewSet)
router.register(r'choice', views.ChoiceViewSet)


urlpatterns = [
    #path('', include(router.urls)),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('post/', include(router.urls)),
]