# Generated by Django 3.0.4 on 2020-03-15 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrimonial', '0003_auto_20200314_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='person',
            name='about_me_answer',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='OK', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='about_my_ideal_spouse_answer',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='OK', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='children_from_previous_marriage_answer',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='OK', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='children_gender_age_answer',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='OK', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='city_of_residence_answer',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='OK', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='countries_of_citizenship_answer',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='OK', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='country_of_birth_answer',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='OK', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='country_of_residence_answer',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='OK', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='custody_of_children',
            field=models.CharField(blank=True, choices=[('MYSELF', 'Myself'), ('EX-SPOUSE', 'Ex-Spouse'), ('SHARED CUSTODY', 'Shared Custody'), ('NOT APPLICABLE', 'Not Applicable')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='custody_of_children_answer',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='OK', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='drink_alcohol_answer',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='OK', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='education_answer',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='OK', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='email_address_answer',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='OK', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='facebook_link_answer',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='OK', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='fast_ramadan_answer',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='OK', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='father_country_answer',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='OK', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name_answer',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='OK', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='height_answer',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='OK', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='instagram_link_answer',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='OK', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='language_spoken_answer',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='OK', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name_answer',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='OK', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='looking_for_in_spouse_age_answer',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='OK', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='looking_for_in_spouse_marital',
            field=models.CharField(blank=True, choices=[('SINGLE', 'Single & Never Married'), ('DIVORCED', 'Divorced'), ('WIDOW(ER)', 'Widow(er)'), ('NO PREFERENCE', 'No Preference')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='looking_for_in_spouse_marital_answer',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='OK', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='marital_status_answer',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='OK', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='mother_country_answer',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='OK', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='muslim_origin',
            field=models.CharField(blank=True, choices=[('MUSLIM BY BIRTH', 'Muslim by Birth'), ('MUSLIM BY CONVERSION', 'Reverted / Converted')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='muslim_origin_answer',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='OK', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='occupation_answer',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='OK', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone_number_answer',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='OK', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='prays_answer',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='OK', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='race_ethnicity_answer',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='OK', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='references_answer',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='OK', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='relationship_of_person_completing_form',
            field=models.CharField(blank=True, choices=[('MYSELF', 'Self'), ('PARENT', 'Parent'), ('SIBLING', 'Sibling'), ('OTHER', 'Other')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='relationship_of_person_completing_form_answer',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='OK', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='religious_sect',
            field=models.CharField(blank=True, choices=[('SUNNI', 'Sunni'), ('SHIA', 'Shia'), ('OTHER', 'Other')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='religious_sect_answer',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='OK', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='significant_health_issues_answer',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='OK', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='smoke_answer',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='OK', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='spouse_education_answer',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='OK', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='spouse_ethnicity_answer',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='OK', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='spouse_height_answer',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='OK', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='spouse_profession_answer',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='OK', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='spouse_relocation_answer',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='OK', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='spouse_visa_status_answer',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='OK', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='state_of_residence_answer',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='OK', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='time_frame_marriage',
            field=models.CharField(blank=True, choices=[('AS SOON AS POSSIBLE', 'As soon as possible'), ('WITHIN A YEAR', 'Within a Year'), ('ONE TO TWO YEARS', 'One to Two Years'), ('TWO OR MORE YEARS', 'Two or more Years'), ('FLEXIBLE', 'Flexible')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='time_frame_marriage_answer',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='OK', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='travel_for_job_answer',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='OK', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='us_visa_status',
            field=models.CharField(blank=True, choices=[('US CITIZEN', 'US Citizen'), ('GREEN CARD', 'Permanent Resident / Green Card'), ('STUDENT VISA', 'Student Visa'), ('WORK VISA', 'Work / Business Visa'), ('OTHER', 'Other')], max_length=50, null=True, verbose_name='US Visa Status'),
        ),
        migrations.AlterField(
            model_name='person',
            name='us_visa_status_answer',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='OK', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='visit_shrine_answer',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='OK', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='wear_hijab_answer',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='OK', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='weight_answer',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='OK', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='willing_to_relocate',
            field=models.CharField(blank=True, choices=[('NO', 'No'), ('YES', 'Yes'), ('PREFER NOT', 'Yes, but prefer not to')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='willing_to_relocate_answer',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='OK', max_length=100),
        ),
    ]
