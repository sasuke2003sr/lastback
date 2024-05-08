# Generated by Django 4.2.3 on 2024-05-08 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delhi', '0002_alter_delhi_options_delhi_address_delhi_age_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
                ('TenderId', models.CharField(max_length=100)),
                ('Title', models.CharField(max_length=100)),
                ('Date', models.DateField()),
                ('Deadline', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Tender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tender_id', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('published_date', models.DateField()),
                ('deadline', models.DateField()),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Delhi',
        ),
    ]
