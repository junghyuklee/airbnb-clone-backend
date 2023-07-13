# Generated by Django 4.2.1 on 2023-07-12 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0005_alter_experience_perks'),
        ('wishlists', '0004_alter_wishlist_experiences_alter_wishlist_rooms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='experiences',
            field=models.ManyToManyField(blank=True, related_name='wishlists', to='experiences.experience'),
        ),
    ]