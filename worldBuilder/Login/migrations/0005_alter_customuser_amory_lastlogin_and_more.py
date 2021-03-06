# Generated by Django 4.0.3 on 2022-03-23 13:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0004_alter_customuser_amory_lastlogin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='Amory_lastLogin',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Business_lastLogin',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Cornwall_lastLogin',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Forum_lastLogin',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Geoffrey_lastLogin',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='GreatHall_lastLogin',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Harrison_lastLogin',
            field=models.DateField(default=datetime.datetime(2022, 3, 24, 13, 34, 44, 61109)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Hatherly_lastLogin',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Health_lastLogin',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Henry_lastLogin',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Iais_lastLogin',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Laver_lastLogin',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Library_lastLogin',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Living_lastLogin',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Mary_lastLogin',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Mood_lastLogin',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Northcott_lastLogin',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Old_Library_lastLogin',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Peter_lastLogin',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Physics_lastLogin',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Queen_lastLogin',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Reed_lastLogin',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Sports_lastLogin',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Streatham_lastLogin',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Washington_lastLogin',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Wellbeing_lastLogin',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Xfi_lastLogin',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='into_lastLogin',
            field=models.DateField(),
        ),
    ]
