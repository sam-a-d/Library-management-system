# Generated by Django 3.2.7 on 2021-10-07 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_member_national_id_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='library_card_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]