# Generated by Django 3.1.4 on 2021-06-24 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocerystore', '0004_auto_20210622_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='loyaltycard',
            name='code',
            field=models.CharField(default='000000000', max_length=150),
        ),
    ]
