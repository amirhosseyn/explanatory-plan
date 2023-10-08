from django.urls import path
from . import views

app_name = "plan"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path('create/', views.PlanCreateView.as_view(), name='plan_create'),  
    # path("list_view/", views.PlanListView.as_view(), name="plan_list_view"),
    # path("<int:pk>/delete/", views.PlanDeleteView.as_view(), name="plan_delete"),
    # path("<int:pk>/update/", views.PlanUpdateView.as_view(), name="plan_update"),
    # path('<int:pk>/detail/', views.PlanDetailView.as_view(), name='plan_detail'),
]