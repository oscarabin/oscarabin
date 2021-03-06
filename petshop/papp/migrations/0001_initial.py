# Generated by Django 2.1.1 on 2022-01-24 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pet_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=100)),
                ('pet_des', models.CharField(max_length=200)),
                ('p_image', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='pet_usereg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=100)),
                ('l_name', models.CharField(max_length=100)),
                ('uname', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('dob', models.DateField(max_length=8)),
                ('gender', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=30)),
                ('ph_no', models.CharField(max_length=50)),
            ],
        ),
    ]
