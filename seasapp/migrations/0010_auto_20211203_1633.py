# Generated by Django 3.2.9 on 2021-12-03 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seasapp', '0009_auto_20211203_0607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coofferedcourse_t',
            name='COFFERED_WITH',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='COFFERED_WITH', to='seasapp.course_t'),
        ),
        migrations.AlterField(
            model_name='coofferedcourse_t',
            name='OfferedCourseID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='OfferedCourseID', to='seasapp.course_t'),
        ),
        migrations.AlterUniqueTogether(
            name='coofferedcourse_t',
            unique_together={('OfferedCourseID', 'COFFERED_WITH')},
        ),
    ]