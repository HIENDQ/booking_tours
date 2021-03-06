

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('files', '0001_initial'),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tours',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('views', models.IntegerField(blank=True, default=0, null=True)),
                ('address', models.CharField(max_length=300)),
                ('amount', models.IntegerField()),
                ('duration', models.DateTimeField()),
                ('quantity_members', models.IntegerField()),
                ('policy', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='categories.Categories')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('images', models.ManyToManyField(blank=True, null=True, related_name='image_tour', to='files.File')),
                ('video_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='files.File')),
            ],
        ),
    ]
