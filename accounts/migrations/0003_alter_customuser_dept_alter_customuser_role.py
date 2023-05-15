# Generated by Django 4.2.1 on 2023-05-14 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20230514_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='dept',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.department'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.role'),
        ),
    ]
