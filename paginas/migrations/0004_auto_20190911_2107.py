# Generated by Django 2.2.4 on 2019-09-12 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0003_auto_20190911_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(decimal_places=5, max_digits=10, null=True),
        ),
    ]
