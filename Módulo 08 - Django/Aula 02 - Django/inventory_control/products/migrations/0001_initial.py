# Generated by Django 5.0.1 on 2024-01-31 00:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('suppliers', '0002_alter_supplier_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('description', models.TextField(max_length=255)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='ProductInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=5)),
                ('local', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Inventário do Produto',
                'verbose_name_plural': 'Inventários dos Produtos',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(max_length=255)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_perishable', models.BooleanField()),
                ('explation_date', models.DateField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='products')),
                ('thumbnail', models.ImageField(blank=True, upload_to='thumbnails')),
                ('enabled', models.BooleanField(default=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='products.category')),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.productinventory')),
            ],
        ),
        migrations.CreateModel(
            name='SupplierProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suppliers.supplier')),
            ],
            options={
                'verbose_name': 'Fornecedor do Produto',
                'verbose_name_plural': 'Fornecedores dos Produtos',
                'unique_together': {('supplier', 'product')},
            },
        ),
        migrations.AddField(
            model_name='product',
            name='suppliers',
            field=models.ManyToManyField(blank=True, through='products.SupplierProduct', to='suppliers.supplier'),
        ),
    ]
