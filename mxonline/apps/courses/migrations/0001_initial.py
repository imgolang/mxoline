# Generated by Django 2.2.4 on 2019-08-12 15:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
                ('name', models.CharField(max_length=50, verbose_name='课程名称')),
                ('desc', models.CharField(max_length=300, verbose_name='课程描述')),
                ('learn_times', models.IntegerField(default=0, verbose_name='学习市场(分钟)')),
                ('degree', models.CharField(choices=[('primary', '初级'), ('intermediate', '中级'), ('advanced ', '高级')], max_length=20, verbose_name='难度')),
                ('students', models.IntegerField(default=0, verbose_name='学习人数')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='收藏人数')),
                ('click_nums', models.IntegerField(default=0, verbose_name='点击数')),
                ('category', models.CharField(default='后端开发', max_length=20, verbose_name='课程类别')),
                ('tag', models.CharField(default='', max_length=20, verbose_name='课程标签')),
                ('youneed_know', models.CharField(default='', max_length=300, verbose_name='课程须知')),
                ('teacher_tell', models.CharField(default='', max_length=300, verbose_name='老师告诉你')),
                ('detail', models.TextField(verbose_name='课程详情')),
                ('image', models.ImageField(upload_to='courses/%Y/%m', verbose_name='封面图')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.Teacher', verbose_name='课程讲师')),
            ],
            options={
                'verbose_name': '课程信息',
                'verbose_name_plural': '课程信息',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
                ('name', models.CharField(max_length=100, verbose_name='章节名称')),
                ('learn_times', models.IntegerField(default=0, verbose_name='学习时长(分钟)')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='课程')),
            ],
            options={
                'verbose_name': '章节信息',
                'verbose_name_plural': '章节信息',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
                ('name', models.CharField(max_length=50, verbose_name='视频名称')),
                ('learn_times', models.IntegerField(default=0, verbose_name='学习时长(分钟)')),
                ('url', models.CharField(max_length=200, verbose_name='访问地址')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Lesson')),
            ],
            options={
                'verbose_name': '视频信息',
                'verbose_name_plural': '视频信息',
            },
        ),
        migrations.CreateModel(
            name='CourseResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
                ('name', models.CharField(max_length=100, verbose_name='资源名称')),
                ('file', models.FileField(upload_to='course/resource/%Y/%m')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
            ],
            options={
                'verbose_name': '资源名称',
                'verbose_name_plural': '资源名称',
            },
        ),
    ]
