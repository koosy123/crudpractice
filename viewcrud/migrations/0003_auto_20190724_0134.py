# Generated by Django 2.2 on 2019-07-23 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewcrud', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='blog',
            field=models.ForeignKey(null=True, on_delete=True, related_name='comments', to='viewcrud.Blog'),
        ),
    ]
