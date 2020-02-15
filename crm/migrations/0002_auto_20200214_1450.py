# Generated by Django 2.2.6 on 2020-02-14 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classlist',
            name='class_type',
            field=models.SmallIntegerField(choices=[(0, '面授(脱产)'), (1, '面授(周末)'), (2, '网络班')], default=None, verbose_name='班级类型'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='source',
            field=models.SmallIntegerField(choices=[(0, '转介绍'), (1, 'QQ群'), (2, '官网'), (3, '百度推广'), (4, '51CTO'), (5, '知乎'), (6, '市场推广'), (7, '未知来源')], default=7),
        ),
        migrations.AlterField(
            model_name='customer',
            name='status',
            field=models.SmallIntegerField(choices=[(0, '已报名'), (1, '未报名')], default=1),
        ),
        migrations.AlterField(
            model_name='customerfollowup',
            name='intention',
            field=models.SmallIntegerField(choices=[(0, '2周内报名'), (1, '1个月内报名'), (2, '近期无报名计划'), (3, '已在其它机构报名'), (4, '已报名'), (5, '未报名')], default=5),
        ),
    ]
