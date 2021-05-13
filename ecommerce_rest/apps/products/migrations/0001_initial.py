# Generated by Django 3.2 on 2021-05-13 14:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryProduct',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='fecha de creacion')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='fecha de modificacino')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='fecha de Eliminacion')),
                ('description', models.CharField(max_length=50, unique=True, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'CategoryProduct',
                'verbose_name_plural': 'CategoryProducts',
            },
        ),
        migrations.CreateModel(
            name='MeasureUnit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='fecha de creacion')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='fecha de modificacino')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='fecha de Eliminacion')),
                ('description', models.CharField(max_length=50, unique=True, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'MeasureUnit',
                'verbose_name_plural': 'MeasureUnits',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='fecha de creacion')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='fecha de modificacino')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='fecha de Eliminacion')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Nombre de producto')),
                ('description', models.TextField(verbose_name='Descripcion del producto')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Imagen del producto')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='fecha de creacion')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='fecha de modificacino')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='fecha de Eliminacion')),
                ('descount_value', models.PositiveSmallIntegerField(default=0)),
                ('category_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.categoryproduct', verbose_name='Indicador de Oferta')),
            ],
            options={
                'verbose_name': 'Indicator',
                'verbose_name_plural': 'Indicators',
            },
        ),
        migrations.CreateModel(
            name='HistoricalProduct',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, editable=False, verbose_name='fecha de creacion')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='fecha de modificacino')),
                ('deleted_date', models.DateField(blank=True, editable=False, verbose_name='fecha de Eliminacion')),
                ('name', models.CharField(db_index=True, max_length=150, verbose_name='Nombre de producto')),
                ('description', models.TextField(verbose_name='Descripcion del producto')),
                ('imagen', models.TextField(blank=True, max_length=100, null=True, verbose_name='Imagen del producto')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Product',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalMeasureUnit',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, editable=False, verbose_name='fecha de creacion')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='fecha de modificacino')),
                ('deleted_date', models.DateField(blank=True, editable=False, verbose_name='fecha de Eliminacion')),
                ('description', models.CharField(db_index=True, max_length=50, verbose_name='Descripcion')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical MeasureUnit',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalIndicator',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, editable=False, verbose_name='fecha de creacion')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='fecha de modificacino')),
                ('deleted_date', models.DateField(blank=True, editable=False, verbose_name='fecha de Eliminacion')),
                ('descount_value', models.PositiveSmallIntegerField(default=0)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('category_product', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='products.categoryproduct', verbose_name='Indicador de Oferta')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Indicator',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalCategoryProduct',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, editable=False, verbose_name='fecha de creacion')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='fecha de modificacino')),
                ('deleted_date', models.DateField(blank=True, editable=False, verbose_name='fecha de Eliminacion')),
                ('description', models.CharField(db_index=True, max_length=50, verbose_name='Descripcion')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('measure_unit', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='products.measureunit', verbose_name='Unidad de Medida')),
            ],
            options={
                'verbose_name': 'historical CategoryProduct',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.AddField(
            model_name='categoryproduct',
            name='measure_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.measureunit', verbose_name='Unidad de Medida'),
        ),
    ]