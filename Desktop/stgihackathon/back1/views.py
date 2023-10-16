from multiprocessing import connection
from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponse
from .models import VisaApplication
import csv
# from .models import VisaApplication 
def say_hello(request):
    return HttpResponse ('Hello World')



def say_hello(request):
    # return HttpResponse ('Hello World')
    return render(request,'hello.html',{'name':'akshit'})


def import_data(request):
    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']

        if not csv_file.name.endswith('csv'):
            return HttpResponse('Wrong file type')

        with csv_file as file:
            reader = csv.DictReader(file)
            for row in reader:
                data = VisaApplication(
                    CASE_NUMBER=row['CASE_NUMBER'],
                    DECISION_DATE=row['DECISION_DATE'],
                    EMPLOYER_NAME=row['EMPLOYER_NAME'],
                    VISA_CLASS=row['VISA_CLASS'],
                    NAIC_CODE=row['NAIC_CODE'],
                    WAGE_UNIT_OF_PAY=row['WAGE_UNIT_OF_PAY'],
                    PREVAILING_WAGE=row['PREVAILING_WAGE']
                )
                data.save()

        return HttpResponse('Data imported successfully')
    else:
        return HttpResponse('No file uploaded or invalid request method')


def no_results(request):
     row_count = VisaApplication.objects.count() 
     return render(request, 'results.html', {'row_count': row_count})
   

def calculate_mean_salary(request):
    mean_salary = VisaApplication.objects.aggregate(Avg('salary'))['salary__avg']
    return render(request, 'mean_salary.html', {'mean_salary': mean_salary})


def calculate_median_salary(request):
    salaries = list(VisaApplication.objects.values_list('salary', flat=True))
    
    salaries.sort()
    
    n = len(salaries)
    if n % 2 == 0:
        median_salary = (salaries[n // 2 - 1] + salaries[n // 2]) / 2
    else:

        median_salary = salaries[n // 2]

    return render(request, 'median_salary.html', {'median_salary': median_salary})


def calculate_25th_percentile_salary(request):
    salaries = list(VisaApplication.objects.values_list('salary', flat=True))
    salaries.sort()
    n = len(salaries)
    index = int(n * 0.25)

    # Get the 25th percentile salary
    percentile_salary = salaries[index]

    return render(request, 'percentile_salary.html', {'percentile_salary': percentile_salary})


def calculate_percentile_salary(request):
    salaries = list(VisaApplication.objects.values_list('salary', flat=True))

    salaries.sort()

    n = len(salaries)
    index = int(0.75 * n)
    percentile_salary = salaries[index]
    return render(request, 'percentile_salary_two.html', {'percentile_salary': percentile_salary})

# additional sql queries
def execute_sql_query(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        data = cursor.fetchall()
    return columns, data

def export_to_csv(response, columns, data, filename):
    response['Content-Disposition'] = f'attachment; filename="{filename}.csv"'
    response['Content-Type'] = 'text/csv'
    
    writer = csv.writer(response)
    writer.writerow(columns)
    for row in data:
        writer.writerow(row)

def select_all_with_condition(request):
    query = "SELECT * FROM your_table_name WHERE your_condition_here;"
    columns, data = execute_sql_query(query)
    
    response = HttpResponse(content_type='text/csv')
    export_to_csv(response, columns, data, 'all_data_with_condition')
    
    return response

def select_with_salary_gt_50000(request):
    query = "SELECT * FROM your_table_name WHERE salary > 50000;"
    columns, data = execute_sql_query(query)
    
    response = HttpResponse(content_type='text/csv')
    export_to_csv(response, columns, data, 'salary_gt_50000')
    
    return response