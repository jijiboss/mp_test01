# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-25 02:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mp_test_app', '0013_auto_20170924_2254'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notify_on_schedule_alert',
            old_name='postal_code',
            new_name='postal',
        ),
        migrations.RenameField(
            model_name='notify_on_schedule_alert',
            old_name='state_or_province',
            new_name='state',
        ),
        migrations.AlterField(
            model_name='notify_on_event_update',
            name='order_id_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mp_test_app.mp_Load'),
        ),
        migrations.AlterField(
            model_name='notify_on_location',
            name='order_id_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mp_test_app.mp_Load'),
        ),
        migrations.AlterField(
            model_name='notify_on_order_status_change',
            name='order_id_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mp_test_app.mp_Load'),
        ),
        migrations.AlterField(
            model_name='notify_on_schedule_alert',
            name='order_id_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mp_test_app.mp_Load'),
        ),
    ]