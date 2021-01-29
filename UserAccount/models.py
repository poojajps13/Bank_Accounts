from django.db import models

class User(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField(max_length = 50)
	mobile = models.CharField(max_length = 10)
	pan = models.CharField(max_length=10, unique=True)
	total_number_of_accounts = models.IntegerField()
	credit_score = models.IntegerField()
	address = models.CharField(max_length=100)
	def __str__(self):
		return self.email
		
class Account(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	account_no = models.CharField(max_length=50)
	amount_overdue = models.FloatField()
	current_balance = models.FloatField()
	date_opened = models.DateField()
	date_reported = models.DateField()
	lender = models.CharField(max_length=50)
	sanction_amount = models.FloatField()
	type = models.CharField(max_length=50)
	def __str__(self):
		return self.account_no
