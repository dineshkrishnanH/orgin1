# Generated by Django 5.1.4 on 2024-12-20 16:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IndexModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('indexmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='store.indexmodel')),
                ('name', models.CharField(max_length=200)),
            ],
            bases=('store.indexmodel',),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('indexmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='store.indexmodel')),
                ('name', models.CharField(max_length=200)),
            ],
            bases=('store.indexmodel',),
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('indexmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='store.indexmodel')),
                ('name', models.CharField(max_length=200)),
            ],
            bases=('store.indexmodel',),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('indexmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='store.indexmodel')),
                ('name', models.CharField(max_length=200)),
            ],
            bases=('store.indexmodel',),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('indexmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='store.indexmodel')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.PositiveIntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images')),
                ('stock', models.IntegerField()),
                ('brand_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.brand')),
                ('category_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category')),
                ('size_objects', models.ManyToManyField(to='store.size')),
                ('tag_objects', models.ManyToManyField(to='store.tag')),
            ],
            bases=('store.indexmodel',),
        ),
    ]
