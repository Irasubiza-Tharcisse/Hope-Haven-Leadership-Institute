# Generated by Django 5.0.2 on 2024-11-21 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leadership', '0006_contactform_alter_activities_assigned'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activities',
            name='supervisor',
        ),
        migrations.DeleteModel(
            name='testimonial',
        ),
        migrations.DeleteModel(
            name='activities',
        ),
    ]
