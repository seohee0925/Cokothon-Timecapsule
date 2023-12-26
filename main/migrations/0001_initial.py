# Generated by Django 5.0 on 2023-12-26 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Capsule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='내용')),
                ('picture', models.ImageField(upload_to='', verbose_name='사진')),
                ('destination', models.CharField(choices=[('unknown', '익명'), ('tome', '나')], max_length=7)),
                ('write_date', models.DateTimeField(auto_now=True)),
                ('open_date', models.CharField(choices=[('minute', '1분 후'), ('month', '1개월 후'), ('3month', '3개월 후'), ('6month', '6개월 후'), ('1year', '1년 후')], max_length=6)),
            ],
        ),
    ]
