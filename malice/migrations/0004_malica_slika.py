from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("malice", "0003_alter_malica_options_alter_profiluporabnika_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="malica",
            name="slika",
            field=models.ImageField(blank=True, null=True, upload_to="malice/"),
        ),
    ]