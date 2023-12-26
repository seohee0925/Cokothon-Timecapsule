from django.db import models
# from .models import User

class Capsule(models.Model):
    content = models.TextField(verbose_name='내용')
    picture = models.ImageField(verbose_name='사진')
    
    DESTINATION_CHOICES = [
        ("unknown", "익명"),
        ("tome", "나")
    ]

    OPEN_DATE_CHOICES = [
        ("minute", "1분 후"),
        ("month", "1개월 후"),
        ("3month", "3개월 후"),
        ("6month", "6개월 후"),
        ("1year", "1년 후")
    ]
    
    destination = models.CharField(max_length=7, choices=DESTINATION_CHOICES)
    write_date = models.DateTimeField(auto_now=True)
    open_date = models.CharField(max_length=6, choices=OPEN_DATE_CHOICES)