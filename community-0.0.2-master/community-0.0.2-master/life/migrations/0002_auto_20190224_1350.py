# Generated by Django 2.1.7 on 2019-02-24 13:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LifeComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('depth', models.IntegerField(default=0)),
                ('parent', models.IntegerField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='lifepost',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='lifepost',
            name='notice',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='lifepost',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='lifecomment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='life.LifePost'),
        ),
    ]