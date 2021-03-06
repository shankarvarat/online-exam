# Generated by Django 2.1 on 2019-07-06 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('pid', models.IntegerField(auto_created=True, default=101, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=100)),
                ('mob', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='questios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=300)),
                ('a1', models.CharField(max_length=100)),
                ('a2', models.CharField(max_length=100)),
                ('a3', models.CharField(max_length=100)),
                ('a4', models.CharField(max_length=100)),
                ('ta', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='subject',
            fields=[
                ('subid', models.IntegerField(auto_created=True, default=3000, primary_key=True, serialize=False)),
                ('subname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tname', models.CharField(max_length=200)),
                ('subid', models.ForeignKey(on_delete='CASCADE', to='examapp.subject')),
            ],
        ),
        migrations.CreateModel(
            name='ua',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=300)),
                ('a1', models.CharField(max_length=100)),
                ('a2', models.CharField(max_length=100)),
                ('a3', models.CharField(max_length=100)),
                ('a4', models.CharField(max_length=100)),
                ('ta', models.CharField(max_length=100)),
                ('ua', models.CharField(max_length=100)),
                ('name', models.ForeignKey(on_delete='CASCADE', to='examapp.profile')),
                ('tname', models.ForeignKey(on_delete='CASCADE', to='examapp.test')),
            ],
        ),
        migrations.AddField(
            model_name='questios',
            name='tname',
            field=models.ForeignKey(on_delete='CASCADE', to='examapp.test'),
        ),
    ]
