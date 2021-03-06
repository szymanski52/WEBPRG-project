# Generated by Django 4.0 on 2021-12-11 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(default='Empty message', max_length=200)),
                ('content_dir', models.CharField(max_length=200, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_author', to='auth.user')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_recipient', to='auth.user')),
            ],
        ),
    ]
