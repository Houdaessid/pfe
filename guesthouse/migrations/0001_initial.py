# Generated by Django 4.2.7 on 2024-06-01 15:32

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
            name='Client',
            fields=[
                ('idclient', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(db_collation='utf8mb4_0900_ai_ci', max_length=45)),
                ('prenom', models.CharField(db_collation='utf8mb4_0900_ai_ci', max_length=45)),
                ('numtel', models.CharField(db_collation='utf8mb4_0900_ai_ci', max_length=45)),
                ('email', models.CharField(db_collation='utf8mb4_0900_ai_ci', max_length=45)),
                ('adresse', models.CharField(db_collation='utf8mb4_0900_ai_ci', max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='GuestHouseEvent',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Hebergement',
            fields=[
                ('idchambre', models.IntegerField(primary_key=True, serialize=False)),
                ('numero', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=45)),
                ('prix', models.CharField(db_collation='utf8mb4_0900_ai_ci', max_length=45)),
                ('maison', models.CharField(db_collation='utf8mb4_0900_ai_ci', max_length=45)),
                ('chambre', models.CharField(db_collation='utf8mb4_0900_ai_ci', max_length=45)),
                ('etage', models.CharField(db_collation='utf8mb4_0900_ai_ci', max_length=45)),
                ('local', models.CharField(db_collation='utf8mb4_0900_ai_ci', max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Historique',
            fields=[
                ('idhistorique', models.IntegerField(primary_key=True, serialize=False)),
                ('adressip', models.CharField(db_column='adressIP', max_length=45)),
                ('date', models.DateField()),
                ('tache', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('idnotification', models.IntegerField(primary_key=True, serialize=False)),
                ('consulte', models.IntegerField()),
                ('email', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
            ],
        ),
      
        migrations.CreateModel(
            name='Salle',
            fields=[
                ('idsalle', models.IntegerField(primary_key=True, serialize=False)),
                ('type', models.CharField(db_collation='utf8mb4_0900_ai_ci', max_length=45)),
                ('prix', models.CharField(db_collation='utf8mb4_0900_ai_ci', max_length=45)),
                ('local', models.CharField(db_collation='utf8mb4_0900_ai_ci', max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Tracabilite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_action', models.CharField(choices=[('ajout', 'Ajout'), ('modification', 'Modification'), ('suppression', 'Suppression')], max_length=12)),
                ('date_action', models.DateTimeField(default=django.utils.timezone.now)),
                ('adresse_ip', models.GenericIPAddressField()),
                ('adresse_mac', models.CharField(max_length=17)),
                ('details_modification', models.TextField(blank=True, null=True)),
                ('id_reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guesthouse.reservation')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_directeur', models.BooleanField(default=False)),
                ('is_chefreception', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_financier', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ressalle',
            fields=[
                ('idressalle', models.AutoField(primary_key=True, serialize=False)),
                ('etablissement', models.CharField(db_collation='utf8mb4_0900_ai_ci', max_length=45)),
                ('demandeur', models.CharField(db_collation='utf8mb4_0900_ai_ci', max_length=45)),
                ('dateEntrée', models.DateField(db_column='dateEntre')),
                ('dateSortie', models.DateField(db_column='dateSorti')),
                ('nombrePersonne', models.PositiveIntegerField(db_column='nombrePersonne')),
                ('sujet', models.CharField(db_collation='utf8mb4_0900_ai_ci', db_column='sujet', max_length=45)),
                ('dejeuner', models.IntegerField()),
                ('pauseCafe', models.IntegerField()),
                ('courrier', models.PositiveIntegerField(db_column='Courrier')),
                ('moyen', models.CharField(db_collation='utf8mb4_0900_ai_ci', max_length=100)),
                ('priseEnCharge', models.CharField(db_collation='utf8mb4_0900_ai_ci', max_length=100)),
                ('statut', models.CharField(db_collation='utf8mb4_0900_ai_ci', max_length=100)),
                ('commentaire', models.CharField(blank=True, db_collation='utf8mb4_0900_ai_ci', max_length=100)),
                ('Salle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guesthouse.salle')),
            ],
        ),
        migrations.CreateModel(
            name='Reshebergement',
            fields=[
                ('idhebergement', models.AutoField(primary_key=True, serialize=False)),
                ('Courrier', models.PositiveIntegerField()),
                ('etablissement', models.CharField(db_collation='utf8mb4_0900_ai_ci', max_length=45)),
                ('Demandeur', models.CharField(db_collation='utf8mb4_0900_ai_ci', max_length=45)),
                ('Capacite', models.PositiveIntegerField()),
                ('DateEntre', models.DateField(db_column='DateEntre')),
                ('DateSortie', models.DateField(db_column='DateSortie')),
                ('PriseenCharge', models.CharField(db_collation='utf8mb4_0900_ai_ci', max_length=100)),
                ('Moyen', models.CharField(db_collation='utf8mb4_0900_ai_ci', max_length=100)),
                ('Statut', models.CharField(db_collation='utf8mb4_0900_ai_ci', max_length=100)),
                ('Type', models.CharField(db_collation='utf8mb4_0900_ai_ci', max_length=100)),
                ('hebergement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='guesthouse.hebergement')),
            ],
        ),
    ]
