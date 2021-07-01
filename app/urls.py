from django.urls import path

from . import views


app_name = 'app'
urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.VoteView.as_view(), name='vote'),
    path('end/', views.EndView.as_view(), name='end')
]
