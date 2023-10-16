from django.db import models

class VisaApplication(models.Model):
    CASE_NUMBER = models.CharField(max_length=255)
    DECISION_DATE = models.CharField(max_length=255)
    EMPLOYER_NAME = models.CharField(max_length=255)
    VISA_CLASS = models.CharField(max_length=50)
    NAIC_CODE = models.CharField(max_length=20)
    WAGE_UNIT_OF_PAY = models.CharField(max_length=20)
    PREVAILING_WAGE = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.CASE_NUMBER
