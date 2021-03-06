# Generated by Django 2.1.1 on 2018-09-19 15:11

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=255, verbose_name='Street address')),
                ('street2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Second line')),
                ('city', models.CharField(max_length=100, verbose_name='City')),
                ('postal_code', models.CharField(blank=True, max_length=10, null=True, verbose_name='postal_code')),
                ('country', django_countries.fields.CountryField(max_length=2, verbose_name='Country')),
                ('longitude', models.FloatField(blank=True, null=True, verbose_name='Longitude')),
                ('latitude', models.FloatField(blank=True, null=True, verbose_name='Latitude')),
            ],
            options={
                'verbose_name_plural': 'addresses',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Category name')),
                ('slug', models.SlugField(max_length=100, verbose_name='Slug')),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('phone', 'Phone'), ('email', 'E-Mail'), ('other', 'Other')], max_length=5, verbose_name='Type')),
                ('value', models.CharField(max_length=400, verbose_name='Value')),
            ],
        ),
        migrations.CreateModel(
            name='Directory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_provider', models.CharField(max_length=255, verbose_name='Service provider name')),
                ('slug', models.SlugField(max_length=255, verbose_name='slug')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Link')),
                ('service_category', models.ManyToManyField(to='transtech_directory.Category', verbose_name='Categories')),
            ],
            options={
                'verbose_name_plural': 'directories',
            },
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='directory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='transtech_directory.Directory', verbose_name='Service provider'),
        ),
        migrations.AddField(
            model_name='address',
            name='directory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='transtech_directory.Directory', verbose_name='Service provider'),
        ),
    ]
