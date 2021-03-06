# Generated by Django 4.0.3 on 2022-03-23 14:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0007_alter_customuser_amory_lastlogin_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='UserRewards',
            field=models.CharField(default='', max_length=1024),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Amory_lastLogin',
            field=models.DateField(default=datetime.datetime(2022, 3, 22, 14, 33, 19, 481983)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Business_lastLogin',
            field=models.DateField(default=datetime.datetime(2022, 3, 22, 14, 33, 19, 482070)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Cornwall_lastLogin',
            field=models.DateField(default=datetime.datetime(2022, 3, 22, 14, 33, 19, 482100)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Forum_lastLogin',
            field=models.DateField(default=datetime.datetime(2022, 3, 22, 14, 33, 19, 482030)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Geoffrey_lastLogin',
            field=models.DateField(default=datetime.datetime(2022, 3, 22, 14, 33, 19, 482155)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='GreatHall_lastLogin',
            field=models.DateField(default=datetime.datetime(2022, 3, 22, 14, 33, 19, 482187)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Harrison_lastLogin',
            field=models.DateField(default=datetime.datetime(2022, 3, 22, 14, 33, 19, 481880)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Hatherly_lastLogin',
            field=models.DateField(default=datetime.datetime(2022, 3, 22, 14, 33, 19, 482221)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Health_lastLogin',
            field=models.DateField(default=datetime.datetime(2022, 3, 22, 14, 33, 19, 482764)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Henry_lastLogin',
            field=models.DateField(default=datetime.datetime(2022, 3, 22, 14, 33, 19, 482251)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Iais_lastLogin',
            field=models.DateField(default=datetime.datetime(2022, 3, 22, 14, 33, 19, 482314)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Innovation_One_lastLogin',
            field=models.DateField(default=datetime.datetime(2022, 3, 22, 14, 33, 19, 482286)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Laver_lastLogin',
            field=models.DateField(default=datetime.datetime(2022, 3, 22, 14, 33, 19, 482373)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Library_lastLogin',
            field=models.DateField(default=datetime.datetime(2022, 3, 22, 14, 33, 19, 482405)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Living_lastLogin',
            field=models.DateField(default=datetime.datetime(2022, 3, 22, 14, 33, 19, 482433)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Mary_lastLogin',
            field=models.DateField(default=datetime.datetime(2022, 3, 22, 14, 33, 19, 482460)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Mood_lastLogin',
            field=models.DateField(default=datetime.datetime(2022, 3, 22, 14, 33, 19, 482677)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Northcott_lastLogin',
            field=models.DateField(default=datetime.datetime(2022, 3, 22, 14, 33, 19, 482128)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Old_Library_lastLogin',
            field=models.DateField(default=datetime.datetime(2022, 3, 22, 14, 33, 19, 482491)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Peter_lastLogin',
            field=models.DateField(default=datetime.datetime(2022, 3, 22, 14, 33, 19, 482522)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Physics_lastLogin',
            field=models.DateField(default=datetime.datetime(2022, 3, 22, 14, 33, 19, 482556)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Queen_lastLogin',
            field=models.DateField(default=datetime.datetime(2022, 3, 22, 14, 33, 19, 482588)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Reed_lastLogin',
            field=models.DateField(default=datetime.datetime(2022, 3, 22, 14, 33, 19, 482615)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Sports_lastLogin',
            field=models.DateField(default=datetime.datetime(2022, 3, 22, 14, 33, 19, 482705)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Streatham_lastLogin',
            field=models.DateField(default=datetime.datetime(2022, 3, 22, 14, 33, 19, 482732)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Washington_lastLogin',
            field=models.DateField(default=datetime.datetime(2022, 3, 22, 14, 33, 19, 482792)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Wellbeing_lastLogin',
            field=models.DateField(default=datetime.datetime(2022, 3, 22, 14, 33, 19, 482642)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Xfi_lastLogin',
            field=models.DateField(default=datetime.datetime(2022, 3, 22, 14, 33, 19, 482819)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='into_lastLogin',
            field=models.DateField(default=datetime.datetime(2022, 3, 22, 14, 33, 19, 482341)),
        ),
    ]
