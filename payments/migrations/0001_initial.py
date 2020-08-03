# Generated by Django 3.0.4 on 2020-08-02 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('college', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donation_id', models.CharField(help_text='Donation ID for the type of donation same as the stripe dashboard', max_length=100)),
                ('donation_name', models.CharField(help_text='Formal Name of the donation', max_length=100, null=True)),
                ('description', models.TextField(default='ABC', help_text='What the donation is for')),
                ('image', models.ImageField(blank=True, null=True, upload_to='donation_images/')),
                ('date_time', models.DateTimeField(auto_now=True)),
                ('days_remaining', models.IntegerField(blank=True, null=True)),
                ('college', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='college.College')),
            ],
        ),
        migrations.CreateModel(
            name='DonationAmount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(help_text='The chosen amount of Donation')),
                ('donation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payments.DonationType')),
            ],
        ),
    ]