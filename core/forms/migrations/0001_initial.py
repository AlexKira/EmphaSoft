# Generated by Django 3.1.3 on 2020-11-17 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=200)),
                ('age', models.IntegerField(verbose_name='Age')),
                ('gender', models.CharField(max_length=200, verbose_name='Gender')),
                ('about_me', models.TextField(blank=True, null=True, verbose_name='About me')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('date_added', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
            options={
                'ordering': ['date_added'],
            },
        ),
    ]
