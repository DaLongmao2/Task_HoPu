# Generated by Django 3.0.3 on 2021-03-15 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserTab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UName', models.CharField(max_length=64)),
                ('LoginName', models.CharField(max_length=64)),
                ('LoginPassword', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='TaskTab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TName', models.CharField(max_length=64)),
                ('TState', models.IntegerField()),
                ('TPlanFinishTimestamp', models.DateField()),
                ('TDescription', models.TextField()),
                ('TGrade', models.IntegerField()),
                ('TCreate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tc', to='APP.UserTab')),
                ('TManager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tm', to='APP.UserTab')),
            ],
        ),
        migrations.CreateModel(
            name='TaskPartnerTab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TaskID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tid', to='APP.TaskTab')),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uid', to='APP.UserTab')),
            ],
        ),
    ]