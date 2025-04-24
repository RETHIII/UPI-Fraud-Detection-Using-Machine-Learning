from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)


class UserPredictModel(models.Model):
    AverageAmountTransactionDay = models.FloatField()  # Assuming it's a decimal value
    TransactionAmount = models.FloatField()  # Assuming it's a decimal value
    Is_declined = models.CharField(max_length=100)  # Assuming this is a True/False field
    TotalNumberOfDeclinesDay = models.IntegerField()
    isForeignTransaction = models.CharField(max_length=100) # Assuming this is a True/False field
    isHighRiskCountry = models.CharField(max_length=100)  # Assuming this is a True/False field
    DailyChargebackAvgAmt = models.FloatField()  # Assuming it's a decimal value
    Six_MonthAvgChbkAmt = models.FloatField()  # Assuming it's a decimal value
    Six_MonthChbkFreq = models.IntegerField()  # Assuming it's an integer
    isFradulent = models.CharField(max_length=100) # Assuming this is a True/False field

    def __str__(self):
        return f"Prediction: {self.isFradulent}"
    


