from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('content', models.TextField()),
                ('image', models.FileField(blank=True, null=True, upload_to='img/')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('hit_cnt', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'board',
            },
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('content', models.CharField(max_length=400)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('username', models.CharField(default='관리자', max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.Board', verbose_name='cmtboard_id')),
            ],
            options={
                'db_table': 'comment',
            },
        ),
    ]
