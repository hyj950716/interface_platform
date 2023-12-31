# Generated by Django 2.2.17 on 2023-07-23 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auto_test', '0007_testcaseexecuterecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestSuitExecuteRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('run_time_interval', models.IntegerField(default=0, null=True, verbose_name='延迟时间')),
                ('status', models.IntegerField(default=0, null=True, verbose_name='执行状态')),
                ('test_result', models.CharField(blank=True, max_length=50, null=True)),
                ('creator', models.CharField(blank=True, max_length=50, null=True)),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('execute_start_time', models.CharField(blank=True, max_length=300, null=True, verbose_name='执行开始时间')),
                ('test_suit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto_test.TestSuit', verbose_name='测试集合')),
            ],
        ),
    ]
