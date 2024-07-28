from django.urls import path
from . import views

urlpatterns = [
    path("",views.index , name="index"),
    # path("loanPrediction",views.LoanPrediction , name="loanPrediction"),
    path('loanPrediction/', views.loan_prediction, name='loan_prediction'),
    path("craditPrediction",views.CraditPrediction , name="craditPrediction"),
    path("test",views.test , name="test"),
    path("about", views.about , name="about")
]
