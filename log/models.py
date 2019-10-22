from django.db import models

class Article(models.Model):#走行ログ
    Mileage = models.CharField(max_length=255)
    Rantime = models.CharField(max_length=255)
    calory = models.CharField(max_length=255)
    author = models.ForeignKey(
        'auth.User', 
        on_delete=models.CASCADE, 
    )
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Mileage