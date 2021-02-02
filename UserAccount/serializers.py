from rest_framework import serializers
from .models import User, Account

class AccountSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Account
		fields = [
			'account_no', 
			'amount_overdue', 
			'current_balance', 
			'date_opened', 
			'date_reported', 
			'lender', 
			'sanction_amount',
			'type'
		]


class UserSerializer(serializers.ModelSerializer):
	accounts = AccountSerializer(many=True) 
	
	class Meta:
		model = User
		fields = [
			'name', 
			'email', 
			'mobile', 
			'pan', 
			'total_number_of_accounts', 
			'credit_score', 
			'address', 
			'accounts'
		]
		depth = 1

	def create(self, validated_data):
		accounts_data = validated_data.pop('accounts')
		user_new = User.objects.create(**validated_data)
		if user_new:
			for account_data in accounts_data:
				account_new = Account.objects.create(user=user_new, **account_data)
		return user_new


