from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def current_time(request):
    now = datetime.now()
    return HttpResponse(f"Current time: {now}")
def mupltiplication_table(request):
    table = "<h1>Multiplication Table from 1 to 10</h1><table border ='1'>"
    for i in range (1,11):
        table += "<tr>"
        for j in range(1,11):
            table += f"<td>{i*j}</td>"
        table += "</tr>"
    table += "</table>"
    return HttpResponse(table)
def show_user(request, first_name, last_name, age):
    return HttpResponse(f"<h1>User: {first_name} {last_name}, age: {age}")
