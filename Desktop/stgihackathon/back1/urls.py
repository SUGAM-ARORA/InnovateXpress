from django.urls import include, path
# from django.urls import path
from . import views
# from views import mean_salary

urlpatterns = [
    path('hello/', views.say_hello),
    path('insert/',views.import_data,name="insert_data"),

    # path('playground/hello', views.say_hello)
    path('results/',views.no_results),
    # path('mean/', mean_salary, name='mean_salary'),
    # path('median/',views.median),
    path('mean/',views.calculate_mean_salary),
    path('median/',views.calculate_median_salary),
    path('percentile/',views.calculate_25th_percentile_salary),
    path('percentilebig/',views.calculate_percentile_salary),

    path('select_all_with_condition/', views.select_all_with_condition, name='select_all_with_condition'),
    path('select_with_salary_gt_50000/', views.select_with_salary_gt_50000, name='select_with_salary_gt_50000'),

]
