# Generated by Django 4.0.5 on 2022-07-13 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_remove_task_task_executor_task_task_executor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('NA', 'NOT ASSIGNED'), ('INP', 'IN PROGRESS'), ('DONE', 'DONE')], default='NA', max_length=4),
        ),
    ]
