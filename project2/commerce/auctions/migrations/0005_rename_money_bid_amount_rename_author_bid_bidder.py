# Generated by Django 4.2.7 on 2023-12-28 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_listing_image_user_watched_listings'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bid',
            old_name='money',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='bid',
            old_name='author',
            new_name='bidder',
        ),
    ]
