# Generated by Django 2.2.17 on 2023-07-23 15:31

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('auto_test', '0006_configuration'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestCaseExecuteRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.IntegerField(help_text='0：表示未执行，1：表示已执行', null=True)),
                ('exception_info', models.CharField(blank=True, max_length=500, null=True)),
                ('request_data', models.CharField(max_length=1024, null=True, verbose_name='请求体')),
                ('response_data', models.CharField(max_length=1024, null=True, verbose_name='响应字符串')),
                ('execute_result', models.CharField(max_length=1024, null=True, verbose_name='执行结果')),
                ('last_time_response_data', models.CharField(max_length=1024, null=True, verbose_name='上一次响应字符串')),
                ('execute_total_time', models.CharField(max_length=1024, null=True, verbose_name='执行耗时')),
                ('execute_start_time', models.CharField(blank=True, max_length=300, null=True, verbose_name='执行开始时间')),
                ('execute_end_time', models.CharField(blank=True, max_length=300, null=True, verbose_name='执行结束时间')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('belong_test_case', smart_selects.db_fields.GroupedForeignKey(group_field='belong_test_case', on_delete=django.db.models.deletion.CASCADE, to='auto_test.TestCase', verbose_name='所属用例')),
            ],
            options={
                'verbose_name': '用例执行结果记录表',
                'verbose_name_plural': '用例执行结果记录表',
            },
        ),
    ]
