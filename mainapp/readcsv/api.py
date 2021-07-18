from itertools import islice
import csv

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . models import Deals
from . serializers import DealsSerializer
from collections import OrderedDict


@api_view(['POST'])
def post_deals(request):
    try:
        file = request.FILES['file']
        decoded_file = file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)
        file_data = []
        for row in reader:
            print(row)
            file_data.append(row)
        serializer = DealsSerializer(data=file_data, many=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"status": "OK", "desc": "файл был обработан без ошибок"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"status": "Error", "desc": f"в процессе обработки файла произошла ошибка: {e}"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_deals(request):
    try:
        deals_instances = Deals.objects.all()
        serializer = DealsSerializer(deals_instances, many=True)
        response = generate_response(serializer.data)
        return Response({"response": response}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(f"{e}", status=status.HTTP_400_BAD_REQUEST)


def generate_response(customers_data):

    customers = {}
    for customer_data in customers_data:
        customers[customer_data['customer']] = {
            "username": customer_data['customer'],
            "spent_money": 0,
            "gems": set()
        }

    for customer_data in customers_data:
        customers[customer_data['customer']]['spent_money'] += customer_data['total']
        customers[customer_data['customer']]['gems'].add(customer_data['item'])

    customers = OrderedDict(sorted(customers.items(), key=lambda i: i[1]['spent_money'], reverse=True))

    return take(5, customers.items())


def take(n, iterable):
    return dict(islice(iterable, n))
