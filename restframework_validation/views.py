from django.shortcuts import render
from django.views import View
import json
import io
from restframework_validation.serializers import NumberSerializer
from restframework_validation.models import Number,validate_even
from django.utils.decorators import method_decorator
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@method_decorator(csrf_exempt, name="dispatch")
class NumberAPI(View):
    """Simple get or post request"""
    def get(self,request):
        if request.method == "GET":
            re = Number.objects.all()
            serializer = NumberSerializer(re, many=True)
            res = {
                    "status_code: ":"200 OK",
                    "msg":"Data fetch successfully!",
                    "Data":serializer.data
                  }
            return JsonResponse(res,safe=False)
        return JsonResponse(
                        {
                            "Error":"Please check your request once!",
                             "status_code":"400 Bad request"
                        })

    def post(self,request):
        if request.method == "POST":
            json_obj = request.body
            stream = io.BytesIO(json_obj)
            py_obj = JSONParser().parse(stream)
            try:
                validate_even(py_obj['even_field'])
            except Exception as e:
                return JsonResponse(
                        {
                            "msg":"Validation Error Occurs Please Check Your Input: ",
                            "Error":f'{e}'
                        })
            try:
                serializer = NumberSerializer(data = py_obj, many=True)
                if serializer.is_valid():
                    serializer.save()
                    res = {
                            "status_code":"201 Created",
                            "msg":"Daata store successfully!",
                            "Data":serializer.data
                         }
                    res
                    return JsonReponse(res)
    
            except Exception as e:
                return JsonResponse(
                                {
                                    "Error":e,
                                    "status_code":"400 Bad request"
                                })
        return JsonResponse(py_obj['even_field'],safe=False)




