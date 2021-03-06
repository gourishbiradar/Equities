# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 01:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Future_Sectors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Futures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=30)),
                ('exp_dt', models.DateField()),
                ('Open', models.DecimalField(decimal_places=2, max_digits=7)),
                ('high', models.DecimalField(decimal_places=2, max_digits=7)),
                ('low', models.DecimalField(decimal_places=2, max_digits=7)),
                ('close', models.DecimalField(decimal_places=2, max_digits=7)),
                ('settlePrice', models.DecimalField(decimal_places=2, max_digits=7)),
                ('Contract', models.IntegerField()),
                ('valnInLakhs', models.IntegerField()),
                ('openI', models.IntegerField()),
                ('deltaOI', models.IntegerField()),
                ('TimeS', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Most_Volatile_Futures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality', models.CharField(max_length=15)),
                ('change', models.IntegerField()),
                ('symbol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='futures', to='Equity.Futures')),
            ],
        ),
        migrations.CreateModel(
            name='Most_Volatile_Options',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality', models.CharField(max_length=15)),
                ('change', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='option_Sectors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=30)),
                ('exp_dt', models.DateField()),
                ('strikePrice', models.IntegerField()),
                ('otype', models.CharField(max_length=15)),
                ('Open', models.DecimalField(decimal_places=2, max_digits=7)),
                ('high', models.DecimalField(decimal_places=2, max_digits=7)),
                ('low', models.DecimalField(decimal_places=2, max_digits=7)),
                ('close', models.DecimalField(decimal_places=2, max_digits=7)),
                ('settlePrice', models.DecimalField(decimal_places=2, max_digits=7)),
                ('openI', models.IntegerField()),
                ('deltaOI', models.IntegerField()),
                ('TimeS', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='perform_metric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sharpeRatio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sectors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=60)),
                ('DClose', models.DecimalField(decimal_places=2, max_digits=7)),
                ('WClose', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='User_Investment_Futures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('buy_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('symbol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='currentFutures', to='Equity.Futures')),
            ],
        ),
        migrations.CreateModel(
            name='User_Investment_Options',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('buy_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('symbol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='currentOptions', to='Equity.Options')),
            ],
        ),
        migrations.CreateModel(
            name='User_Investment_Record_Futures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('buy_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('sold_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('symbol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='investedFutures', to='Equity.Futures')),
            ],
        ),
        migrations.CreateModel(
            name='User_Investment_Record_Options',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('buy_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('sold_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('symbol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='investedOptions', to='Equity.Options')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField()),
                ('mobile', models.DecimalField(decimal_places=0, max_digits=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='user_investment_record_options',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='Equity.UserInfo'),
        ),
        migrations.AddField(
            model_name='user_investment_record_futures',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Users', to='Equity.UserInfo'),
        ),
        migrations.AddField(
            model_name='user_investment_options',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userName', to='Equity.UserInfo'),
        ),
        migrations.AddField(
            model_name='user_investment_futures',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='username', to='Equity.UserInfo'),
        ),
        migrations.AddField(
            model_name='perform_metric',
            name='sname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sectors', to='Equity.Sectors'),
        ),
        migrations.AddField(
            model_name='option_sectors',
            name='sname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tosector', to='Equity.Sectors'),
        ),
        migrations.AddField(
            model_name='option_sectors',
            name='symbol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='option', to='Equity.Options'),
        ),
        migrations.AddField(
            model_name='most_volatile_options',
            name='symbol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='Equity.Options'),
        ),
        migrations.AddField(
            model_name='future_sectors',
            name='sname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sector', to='Equity.Sectors'),
        ),
        migrations.AddField(
            model_name='future_sectors',
            name='symbol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='future', to='Equity.Futures'),
        ),
    ]
