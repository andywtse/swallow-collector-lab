# Generated by Django 4.1 on 2022-08-07 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Migration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.TextField()),
                ('rating', models.CharField(choices=[('1', 'Very Bad'), ('2', 'Somewhat Bad'), ('3', 'Okay'), ('4', 'Pretty Good'), ('5', 'Very Good')], default='1', max_length=1)),
                ('swallow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.swallow')),
            ],
        ),
    ]
