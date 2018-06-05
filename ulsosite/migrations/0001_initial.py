# Generated by Django 2.0.5 on 2018-06-05 15:46

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommitteeMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False, null=True)),
                ('modified', models.DateTimeField(blank=True, null=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('alias', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=30)),
                ('instrument', models.CharField(choices=[('Flute', 'Flute'), ('Clarinet', 'Clarinet'), ('Oboe', 'Oboe'), ('Bassoon', 'Bassoon'), ('Horn', 'Horn'), ('Trumpet', 'Trumpet'), ('Trombone (Tenor)', 'Trombone (Tenor)'), ('Trombone (Bass)', 'Trombone (Bass)'), ('Tuba', 'Tuba'), ('Violin', 'Violin'), ('Viola', 'Viola'), ('Cello', 'Cello'), ('Bass', 'Bass'), ('TimpaniPercussion', 'Timpani & Percussion'), ('Harp', 'Harp')], max_length=20)),
                ('uni', models.CharField(choices=[('RCM', 'Royal College of Music'), ('RAM', 'Royal Academy of Music'), ('Trinity', 'Trinity Laban Conservatoire'), ('GSMD', 'Guildhall School of Music and Drama'), ('KCL', "King's College London"), ('UCL', 'University College London'), ('ICL', 'Imperial College London'), ('LSE', 'London School of Economics'), ('RVC', 'Royal Veterinary College'), ('SOAS', 'SOAS'), ('RH', 'Royal Holloway'), ('City', 'City, University of London'), ('Goldsmiths', 'Goldsmiths, University of London'), ('LSHTM', 'London School of Hygiene and Tropical Medicine'), ('BK', 'Birkbeck'), ('QMUL', 'Queen Mary University of London'), ('Graduate', 'Graduate'), ('Other', 'Other')], max_length=50)),
                ('role', models.CharField(max_length=100)),
                ('season', models.CharField(default='2017/18', help_text='Format yyyy/yy', max_length=10)),
                ('role_description', models.TextField(help_text='Introduce yourself and tell people a bit about your role in ULSO.', max_length=1000)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='committee')),
            ],
            options={
                'ordering': ['role'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current', models.BooleanField(default=False)),
                ('project_term', models.CharField(help_text='e.g. Autumn, Winter, Spring, Summer 1, Summer 2', max_length=30)),
                ('start_time', models.TimeField(default='19:00:00', help_text='Start time of concert')),
                ('concert_date', models.DateField(verbose_name='concert date')),
                ('soloist', models.CharField(blank=True, max_length=100)),
                ('soloist_website', models.CharField(blank=True, max_length=200)),
                ('concert_venue', models.CharField(default="St. Stephen's Church, Gloucester Road, SW7 4RL", max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='ConcertoApplicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False, null=True)),
                ('modified', models.DateTimeField(blank=True, null=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('alias', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=30)),
                ('instrument', models.CharField(choices=[('Flute', 'Flute'), ('Clarinet', 'Clarinet'), ('Oboe', 'Oboe'), ('Bassoon', 'Bassoon'), ('Horn', 'Horn'), ('Trumpet', 'Trumpet'), ('Trombone (Tenor)', 'Trombone (Tenor)'), ('Trombone (Bass)', 'Trombone (Bass)'), ('Tuba', 'Tuba'), ('Violin', 'Violin'), ('Viola', 'Viola'), ('Cello', 'Cello'), ('Bass', 'Bass'), ('TimpaniPercussion', 'Timpani & Percussion'), ('Harp', 'Harp')], max_length=20)),
                ('piece', models.TextField()),
                ('years_ulso_member', models.CharField(help_text='e.g. 2015-2017', max_length=50)),
                ('notes', models.TextField(blank=True)),
                ('second_round', models.BooleanField(default=False, help_text='Admitted to 2nd round')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('no_shortlist', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='ConcertoWinner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False, null=True)),
                ('modified', models.DateTimeField(blank=True, null=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('alias', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=30)),
                ('website', models.URLField(blank=True, null=True)),
                ('biography', models.TextField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='concertowinners/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Conductor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False, null=True)),
                ('modified', models.DateTimeField(blank=True, null=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('alias', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(blank=True, help_text='Although this field is not marked as required, it is strongly recommended that you have a record of this.', max_length=30)),
                ('website', models.URLField(blank=True)),
                ('rate_per_rehearsal', models.IntegerField(default=125, help_text='Fee charged per 3 hour rehearsal.')),
                ('rate_concert_day', models.IntegerField(default=500, help_text='If only the price of the entire project was agreed, put zero per rehearsal and enter the entire fee here')),
                ('notes', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False, null=True)),
                ('modified', models.DateTimeField(blank=True, null=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('alias', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=30)),
                ('instrument', models.CharField(choices=[('Flute', 'Flute'), ('Clarinet', 'Clarinet'), ('Oboe', 'Oboe'), ('Bassoon', 'Bassoon'), ('Horn', 'Horn'), ('Trumpet', 'Trumpet'), ('Trombone (Tenor)', 'Trombone (Tenor)'), ('Trombone (Bass)', 'Trombone (Bass)'), ('Tuba', 'Tuba'), ('Violin', 'Violin'), ('Viola', 'Viola'), ('Cello', 'Cello'), ('Bass', 'Bass'), ('TimpaniPercussion', 'Timpani & Percussion'), ('Harp', 'Harp')], max_length=20)),
                ('doubling', models.CharField(blank=True, default=None, max_length=50)),
                ('uni', models.CharField(choices=[('RCM', 'Royal College of Music'), ('RAM', 'Royal Academy of Music'), ('Trinity', 'Trinity Laban Conservatoire'), ('GSMD', 'Guildhall School of Music and Drama'), ('KCL', "King's College London"), ('UCL', 'University College London'), ('ICL', 'Imperial College London'), ('LSE', 'London School of Economics'), ('RVC', 'Royal Veterinary College'), ('SOAS', 'SOAS'), ('RH', 'Royal Holloway'), ('City', 'City, University of London'), ('Goldsmiths', 'Goldsmiths, University of London'), ('LSHTM', 'London School of Hygiene and Tropical Medicine'), ('BK', 'Birkbeck'), ('QMUL', 'Queen Mary University of London'), ('Graduate', 'Graduate'), ('Other', 'Other')], max_length=50)),
                ('other_uni', models.CharField(blank=True, default=None, help_text="If you selected 'Other', please enter your university here", max_length=50)),
                ('status', models.CharField(choices=[('Candidate', 'Candidate'), ('Member', 'Member'), ('Reserve', 'Reserve'), ('Contact', 'Contact List'), ('Rejected', 'Rejected'), ('Other', 'Other')], default='Candidate', max_length=30)),
                ('year', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('N/A', 'N/A')], max_length=20)),
                ('experience', models.TextField(default='Briefly summarise your recent orchestral experience')),
                ('returning_member', models.BooleanField(default=False)),
                ('subs_paid', models.BooleanField(default=False)),
                ('depping_policy', models.BooleanField(default=False, help_text='Tick here to agree to abide to our depping policy.')),
                ('privacy_policy', models.BooleanField(default=False, help_text='Tick her to inicate that you have read and agreed to our privacy policy.')),
                ('season', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('composer', models.CharField(help_text='Surname only', max_length=20)),
                ('piece', models.CharField(max_length=200)),
                ('order', models.IntegerField(blank=True, help_text='The order of the piece in the concert e.g. 1')),
                ('duration', models.IntegerField(blank=True, default=0, help_text='Length in minutes', null=True)),
                ('flutes', models.IntegerField(blank=True, null=True)),
                ('clarinets', models.IntegerField(blank=True, null=True)),
                ('oboes', models.IntegerField(blank=True, null=True)),
                ('bassoons', models.IntegerField(blank=True, null=True)),
                ('wind_notes', models.CharField(blank=True, help_text='e.g. alto, picc, contra requirements', max_length=200)),
                ('horns', models.IntegerField(blank=True, null=True)),
                ('trumpets', models.IntegerField(blank=True, null=True)),
                ('trombones', models.IntegerField(blank=True, null=True)),
                ('tubas', models.IntegerField(blank=True, null=True)),
                ('brass_notes', models.CharField(blank=True, max_length=200)),
                ('violin_1', models.IntegerField(blank=True, null=True, verbose_name='First violins')),
                ('violin_2', models.IntegerField(blank=True, null=True, verbose_name='Second violins')),
                ('violas', models.IntegerField(blank=True, null=True)),
                ('cellos', models.IntegerField(blank=True, null=True)),
                ('basses', models.IntegerField(blank=True, null=True, verbose_name='Double basses')),
                ('strings_notes', models.CharField(blank=True, max_length=200)),
                ('harps', models.IntegerField(blank=True, help_text='Number of harps', null=True)),
                ('timps', models.BooleanField(default=True)),
                ('percussionists', models.IntegerField(blank=True, default=3, help_text='Number of percussionists requried', null=True)),
                ('other', models.TextField(blank=True, help_text='Equipment notes')),
                ('concert', models.ManyToManyField(blank=True, to='ulsosite.Concert')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerPerProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('musician', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ulsosite.Musician')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ulsosite.Concert')),
            ],
        ),
        migrations.CreateModel(
            name='Rehearsal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rehearsal_date', models.DateField(verbose_name='rehearsal date')),
                ('start_time', models.TimeField(default='19:00:00')),
                ('end_time', models.TimeField(default='22:00:00')),
                ('rehearsal_venue', models.CharField(default="St. Stephen's Church, Gloucester Road, SW7 4RL", max_length=300)),
                ('notes', models.CharField(blank=True, max_length=400)),
                ('concert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ulsosite.Concert')),
            ],
        ),
        migrations.CreateModel(
            name='UsefulContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False, null=True)),
                ('modified', models.DateTimeField(blank=True, null=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('alias', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(blank=True, max_length=30, null=True)),
                ('role', models.CharField(blank=True, help_text='What do they do? e.g. poster artist, percussion hire', max_length=30)),
                ('website', models.URLField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, help_text='Insert fee structures here, e.g. £30 per poster', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Official name e.g. 'St Stephen's Church'", max_length=40)),
                ('address_1', models.CharField(help_text='First line of address', max_length=200)),
                ('address_2', models.CharField(blank=True, help_text='Second line of address', max_length=200, null=True)),
                ('email', models.EmailField(max_length=200)),
                ('contact_number', models.CharField(blank=True, max_length=10, null=True)),
                ('rate_per_rehearsal', models.IntegerField(blank=True, default=90, help_text='Fee charged per 3 hour rehearsal.', null=True)),
                ('rate_concert_day', models.IntegerField(blank=True, default=140, help_text='If only the price of the entire project was agreed, put zero per rehearsal and enter the entire fee here.', null=True)),
                ('rate_per_hour', models.IntegerField(blank=True, default=90, help_text='Alternative to the above fee structures', null=True)),
                ('concert', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ulsosite.Concert')),
            ],
        ),
        migrations.AddField(
            model_name='playerperproject',
            name='rehearsal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ulsosite.Rehearsal'),
        ),
        migrations.AddField(
            model_name='concert',
            name='conductor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ulsosite.Conductor'),
        ),
    ]
