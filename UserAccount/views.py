from django.shortcuts import render
import requests
import datetime
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, Account
from .serializers import *

class FetchUserData(APIView):
	def get(self, request):
		try:
			data = requests.get('https://arkneofinance.com/api/sample_credit_report')
			user_info = data.json()
			user_info = user_info['data']
			account_infos = user_info['accounts']
			for account_info in account_infos:
				account_info['date_opened'] = datetime.datetime.strptime(account_info['date_opened'], "%d-%m-%Y").strftime("%Y-%m-%d")
				account_info['date_reported'] = datetime.datetime.strptime(account_info['date_reported'], "%d-%m-%Y").strftime("%Y-%m-%d")
			
		except Exception as e:
			return Response(
					{
						"Message":e
					},
					status = status.HTTP_400_BAD_REQUEST
			)
		serializer = UserSerializer(data=user_info)
		if serializer.is_valid(raise_exception=ValueError):
			serializer.create(validated_data=user_info)
			return Response(
					{
						"Message":"User details saved successfully!!"
					},
					status = status.HTTP_201_CREATED
			)
		return Response(
						serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST
                    )