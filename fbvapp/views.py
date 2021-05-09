from django.shortcuts import render
from fbvapp . serializers import StudentSerializer
from  fbvapp . models import Student
from rest_framework.response import Response
from rest_framework import status
from  rest_framework .decorators import api_view

# Create your views here.
@api_view(['GET','POST']) # it tell which request it will handlec
def student_list(request):


    if request.method=='GET':
        student=Student.objects.all()                           #it will brinl all the data from data bse
        serializer=StudentSerializer(student,many=True)           # selizer=variable,and made a object of S.s,it tell many=true there is lot of stufent that is list of student
        return Response(serializer.data)                           # it will selize data and give response to http/data is attribute


    elif request.method == 'POST':
        serializer=StudentSerializer(data=request.data)             #seliazer,data is variable/converting data into python objects
        if serializer.is_valid():                                     # it willchake dta charfiled or id field is correct
            serializer.save()                                        # it wil save data
            return Response(serializer.data,status=status.HTTP_201_CREATED)  # data send
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) # error msg


    # working with single student i.e primary key.
@api_view(['GET','PUT','DELETE'])
def student_detail(request,pk):
    try:
        student=Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method== 'GET':
        serializer=StudentSerializer(student)
        return Response(serializer.data)

    elif request.method=='PUT':
        serializer=StudentSerializer(student,data=request.data)     # data comung from user data=request.data/
        if serializer.is_valid():    # check data
          serializer.save()
          return Response(serializer.data)                              # return dta responsr
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)   # if data is  not valid

    elif request.method=='DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
