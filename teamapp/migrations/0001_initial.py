# Generated by Django 4.2.6 on 2023-10-27 10:56

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название проекта')),
                ('description', models.TextField(max_length=200, verbose_name='Описание проекта')),
                ('student_count', models.IntegerField(verbose_name='Размер группы')),
                ('week', models.JSONField(blank=True, default=list, verbose_name='Недели')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.CreateModel(
            name='ProjectManager',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('start_time', models.TimeField(verbose_name='Время начала рабочего дня')),
                ('end_time', models.TimeField(verbose_name='Время конца рабочего дня')),
                ('telegram', models.CharField(blank=True, max_length=70, verbose_name='Телеграм')),
            ],
            options={
                'verbose_name': 'Менеджер',
                'verbose_name_plural': 'Менеджеры',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Уровень ученика')),
            ],
            options={
                'verbose_name': 'Уровень знания',
                'verbose_name_plural': 'Уровни знаний',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('telegram', models.CharField(blank=True, max_length=70, verbose_name='Телеграм')),
                ('rank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_ranks', to='teamapp.rank', verbose_name='Уровень ученика')),
            ],
            options={
                'verbose_name': 'Ученик',
                'verbose_name_plural': 'Ученики',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting_time', models.TimeField(verbose_name='Время ежедневных созвонов')),
                ('start_date', models.DateField(verbose_name='День начала проекта')),
                ('info', models.TextField(max_length=200, verbose_name='Описание проекта')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teamapp.project')),
                ('project_manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_managers', to='teamapp.projectmanager', verbose_name='Менеджер')),
                ('students', models.ManyToManyField(to='teamapp.student')),
            ],
            options={
                'verbose_name': 'Команда',
                'verbose_name_plural': 'Команды',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='project_manager',
            field=models.ManyToManyField(to='teamapp.projectmanager', verbose_name='Менеджер'),
        ),
        migrations.AddField(
            model_name='project',
            name='rank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_ranks', to='teamapp.rank', verbose_name='Уровень ученика'),
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invitation_date', models.DateField(verbose_name='Дата последнего уведомления')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teamapp.project', verbose_name='Проект')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invite_students', to='teamapp.student', verbose_name='Ученик')),
            ],
            options={
                'verbose_name': 'Приглашение',
                'verbose_name_plural': 'Приглашения',
            },
        ),
        migrations.CreateModel(
            name='StudentProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teamapp.project')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teamapp.student')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teamapp.team')),
            ],
            options={
                'unique_together': {('student', 'project')},
            },
        ),
        migrations.CreateModel(
            name='StudentAvailability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teamapp.project')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teamapp.student')),
                ('time_slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teamapp.timeslot')),
            ],
            options={
                'unique_together': {('student', 'time_slot', 'project')},
            },
        ),
    ]
