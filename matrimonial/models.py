from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# from django.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# Create your models here.
class Person(models.Model):

    YES = 'YES' # Value in quote is saved in database
    NO = 'NO'
    OCC = 'OCCASIONALLY'
    MALE = 'MALE'
    FEMALE = 'FEMALE'


    YES_NO_OPTIONS = [
        (NO, 'No'),
        (YES, 'Yes'),
    ]
    GENDER_OPTIONS = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    # CONTACT_OPTIONS = [
    #     (0, 'Email'),
    #     (1, 'Phone'),
    #     (2, 'Text'),
    #     (3, 'WhatsApp'),
    # ]

    MYSELF = 'MYSELF'
    PARENT = 'PARENT'
    SIBLING = 'SIBLING'
    OTHER = 'OTHER'
    RELATIONSHIP_OPTIONS = [
        (MYSELF, 'Self'),
        (PARENT, 'Parent'),
        (SIBLING, 'Sibling'),
        (OTHER, 'Other'),
    ]
    SINGLE = 'SINGLE'
    DIVORCED = 'DIVORCED'
    WIDOWED = 'WIDOW(ER)'
    MARITAL_STATUS_OPTIONS = [
        (SINGLE, 'Single & Never Married'),
        (DIVORCED, 'Divorced'),
        (WIDOWED, 'Widow(er)'),
    ]
    NP = 'NO PREFERENCE'
    SPOUSE_MARITAL_STATUS_OPTIONS = [
        (SINGLE, 'Single & Never Married'),
        (DIVORCED, 'Divorced'),
        (WIDOWED, 'Widow(er)'),
        (NP, 'No Preference'),
    ]
    NA = 'NOT APPLICABLE'
    EX_SPOUSE = 'EX-SPOUSE'
    SHARED_CUSTODY = 'SHARED CUSTODY'
    CUSTODY_OPTIONS = [
        (MYSELF, 'Myself'),
        (EX_SPOUSE, 'Ex-Spouse'),
        (SHARED_CUSTODY, 'Shared Custody'),
        (NA, 'Not Applicable'),
    ]
    PREFER_NOT = 'PREFER NOT'
    RELOCATING_OPTIONS = [
        (NO, 'No'),
        (YES, 'Yes'),
        (PREFER_NOT, 'Yes, but prefer not to'),
    ]
    US_CITIZEN = 'US CITIZEN'
    GREEN_CARD = 'GREEN CARD'
    STUDENT_VISA = 'STUDENT VISA'
    WORK_VISA = 'WORK VISA'
    VISA_STATUS_OPTIONS = [
        (US_CITIZEN, 'US Citizen'),
        (GREEN_CARD, 'Permanent Resident / Green Card'),
        (STUDENT_VISA, 'Student Visa'),
        (WORK_VISA, 'Work / Business Visa'),
        (OTHER, 'Other'),
    ]
    MUSLIM_BIRTH = 'MUSLIM BY BIRTH'
    MUSLIM_CONVERTED = 'MUSLIM BY CONVERSION'
    MUSLIM_ORIGIN_OPTIONS = [
        (MUSLIM_BIRTH, 'Muslim by Birth'),
        (MUSLIM_CONVERTED, 'Reverted / Converted'),
    ]
    SUNNI = 'SUNNI'
    SHIA = 'SHIA'
    MUSLIM_KIND_OPTIONS = [
        (SUNNI, 'Sunni'),
        (SHIA, 'Shia'),
        (OTHER, 'Other'),
    ]
    EDU_LEVEL_OPTIONS = [
        (0, 'Less than High School or 12 Grade'),
        (1, 'High School'),
        (2, 'Technical / Vocational Program'),
        (3, 'Associates Degree'),
        (4, 'Bachelors Degree'),
        (5, 'Master Degree'),
        (6, 'Professional School Degree'),
        (7, 'Doctoral Degree'),
        (8, 'Other'),
    ]
    JOB_TRAVELING_OPTIONS = [
        (0, 'I do not travel'),
        (1, 'Yes, I travel some'),
        (2, 'Yes, I travel mostly'),
        (3, 'Yes, I travel all the time'),
    ]
    ALCOHOL_OPTIONS = [
        (0, 'No'),
        (1, 'Yes'),
        (2, 'Occasionally'),
    ]

    SMOKE_OPTIONS = [
        (0, 'No'),
        (1, 'Smoke Cigarettes'),
        (2, 'Vape / E-cigarettes'),
        (3, 'Smoke Hookah'),
        (4, 'Chew Tobacco'),
        (5, 'Paan (Indian Betel Leaf)'),
    ]
    PRAYER_OPTIONS = [
        (0, 'Yes'),
        (1, 'Mostly'),
        (2, 'Sometimes'),
        (3, 'No'),
    ]
    FASTING_OPTIONS = [
        (0, 'Yes'),
        (1, 'Mostly'),
        (2, 'Sometimes'),
        (3, 'No'),
        (4, 'No, due to medical reason'),
    ]
    SHRINE_OPTIONS = [
        (0, 'No'),
        (1, 'Yes'),
        (2, 'I do not know anything about “Dargah or Mazar or Shrines”'),
        (3, 'I prefer NOT to answer or make this public'),
    ]
    HIJAB_OPTIONS = [
        (0, 'Not applicable (I am a Male)'),
        (1, 'I wear Hijab'),
        (2, 'I do not wear Hijab'),
        (3, 'I do not wear Hijab, but open to it in future'),
        (4, 'I do not wear Hijab, and do not intend to in future'),
    ]
    ASAP = 'AS SOON AS POSSIBLE'
    ONE_YEAR = 'WITHIN A YEAR'
    TWO_YEARS = 'ONE TO TWO YEARS'
    TWO_PLUS = 'TWO OR MORE YEARS'
    FLEXIBLE = 'FLEXIBLE'
    MARRIAGE_TIME_OPTIONS = [
        (ASAP, 'As soon as possible'),
        (ONE_YEAR, 'Within a Year'),
        (TWO_YEARS, 'One to Two Years'),
        (TWO_PLUS, 'Two or more Years'),
        (FLEXIBLE, 'Flexible'),
    ]
    MARITAL_STATUS_OPTIONS = [
        (0, 'Single & Never Married, and no children'),
        (1, 'Divorced with no children maximum'),
        (2, 'Divorced with 1 children maximum'),
        (3, 'Divorced with 2 children maximum'),
        (4, 'Divorced with 3 children maximum'),
        (5, 'Divorced with any number of children'),
    ]
    SPOUSE_RELOCATION_OPTIONS = [
        (0, 'Yes'),
        (1, 'Yes, but prefer to within same state'),
        (2, 'Yes, but prefer not to'),
        (3, 'No'),
    ]
    PUBLIC_DATA = 'PUBLIC' # Value in quote is saved in database
    PRIVATE_DATA = 'PRIVATE'
    ANSWER_OPTIONS = [
        (PUBLIC_DATA, 'Public'),# Value in quote is displayed on form
        (PRIVATE_DATA, 'Private'),
    ]

    the_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, unique=True)
    inactive = models.BooleanField(default=False)
    published = models.BooleanField(default=False)
    last_name = models.CharField(max_length=50,verbose_name="Last Name", null=True, blank=True)
    about_me = models.TextField(verbose_name='About Me', null=True, blank=True)
    about_my_ideal_spouse = models.TextField(verbose_name='About my Ideal Spouse', null=True, blank=True)
    bypass_admin_contact_directly = models.CharField(max_length=50, choices=YES_NO_OPTIONS, null=True, blank=True)
    children_from_previous_marriage = models.CharField(max_length=50, choices=YES_NO_OPTIONS, null=True, blank=True)
    permission_share = models.CharField(max_length=50, choices=YES_NO_OPTIONS, null=True, blank=True)
    significant_health_issues = models.CharField(max_length=50, choices=YES_NO_OPTIONS, null=True, blank=True)
    father_country = models.CharField(max_length=50, verbose_name="My father's Country of Origin", null=True, blank=True)
    mother_country = models.CharField(max_length=50, verbose_name="My Mother's Coutry of Origin", null=True, blank=True)
    spouse_ethnicity = models.CharField(max_length=50, verbose_name="Preferred Spouse's Ethnicity", null=True, blank=True)
    spouse_height = models.CharField(max_length=50, verbose_name="Preferred Spouse's Height", null=True, blank=True)
    spouse_education = models.CharField(max_length=50, verbose_name="Spouse's Highest Education", null=True, blank=True)
    spouse_profession = models.CharField(max_length=50, verbose_name="Spouse's Preferred Profession", null=True, blank=True)
    spouse_visa_status = models.CharField(max_length=50, verbose_name="Spouse's Visa Status", null=True, blank=True)
    city_of_residence = models.CharField(max_length=50, verbose_name='City of Residence', null=True, blank=True)
    country_of_birth = models.CharField(max_length=50, verbose_name='Country of Birth', null=True, blank=True)
    countries_of_citizenship = models.CharField(max_length=50, verbose_name='Country of Citizenship', null=True, blank=True)
    email_address = models.CharField(max_length=50, verbose_name='Email Address', null=True, blank=True)
    facebook_link = models.CharField(max_length=50, verbose_name='Facebook Profile Link', null=True, blank=True)
    children_gender_age = models.TextField(blank=True, null=True, verbose_name='If any Children, then how many, Genders, and Ages')
    instagram_link = models.CharField(max_length=50, verbose_name='Instagram Profile Link', null=True, blank=True)
    language_spoken = models.CharField(max_length=50, verbose_name='Languages Spoken', null=True, blank=True)
    first_name = models.CharField(max_length=50, verbose_name='First Name', null=True, blank=True)
    looking_for_in_spouse_age = models.CharField(max_length=50, verbose_name='Desired Age Range of Spouse', null=True, blank=True)
    occupation = models.CharField(max_length=50, verbose_name='Occupation', null=True, blank=True)
    phone_number = models.CharField(max_length=50, verbose_name='Phone Number', null=True, blank=True)
    #provide_contact_if_yes = models.CharField(blank=True, null=True, max_length=220, verbose_name='Provide CONTACT, if you answered "YES" to the previous question')
    race_ethnicity = models.CharField(max_length=50, verbose_name='Race / Ethnicity', null=True, blank=True)
    state_of_residence = models.CharField(max_length=50, verbose_name='State of Residence', null=True, blank=True)
    country_of_residence = models.CharField(max_length=50, verbose_name='Country of Residence', null=True, blank=True)
    references = models.CharField(max_length=50, verbose_name='Will you be willing to provide references upon request?', null=True, blank=True)
    #preferred_method_of_contact_by_admin = models.CharField(max_length=50, choices=CONTACT_OPTIONS, null=True, blank=True)
    relationship_of_person_completing_form = models.CharField(max_length=50, choices=RELATIONSHIP_OPTIONS, null=True, blank=True)
    year_of_birth = models.CharField(max_length=50, verbose_name='Year of Birth')
    gender = models.CharField(max_length=50, choices=GENDER_OPTIONS)
    marital_status = models.CharField(max_length=50, choices=MARITAL_STATUS_OPTIONS, null=True, blank=True)
    custody_of_children = models.CharField(max_length=50, choices=CUSTODY_OPTIONS, null=True, blank=True)
    willing_to_relocate = models.CharField(max_length=50, choices=RELOCATING_OPTIONS, null=True, blank=True)
    us_visa_status = models.CharField(max_length=50, verbose_name='US Visa Status', choices=VISA_STATUS_OPTIONS, null=True, blank=True)
    muslim_origin = models.CharField(max_length=50, choices=MUSLIM_ORIGIN_OPTIONS, null=True, blank=True)
    religious_sect = models.CharField(max_length=50, choices=MUSLIM_KIND_OPTIONS, null=True, blank=True)
    education = models.CharField(max_length=50, choices=EDU_LEVEL_OPTIONS, null=True, blank=True)
    travel_for_job = models.CharField(max_length=50, choices=JOB_TRAVELING_OPTIONS, null=True, blank=True)
    height = models.CharField(max_length=50, verbose_name='Height', null=True, blank=True)
    weight = models.CharField(max_length=50, verbose_name='Weight', null=True, blank=True)
    drink_alcohol = models.CharField(max_length=50, choices=ALCOHOL_OPTIONS, null=True, blank=True)
    smoke = models.CharField(max_length=50, choices=SMOKE_OPTIONS, null=True, blank=True)
    prays = models.CharField(max_length=50, choices=PRAYER_OPTIONS, null=True, blank=True)
    fast_ramadan = models.CharField(max_length=50, choices=FASTING_OPTIONS, null=True, blank=True)
    visit_shrine = models.CharField(max_length=50, choices=SHRINE_OPTIONS, null=True, blank=True)
    wear_hijab = models.CharField(max_length=50, choices=HIJAB_OPTIONS, null=True, blank=True)
    time_frame_marriage = models.CharField(max_length=50, choices=MARRIAGE_TIME_OPTIONS, null=True, blank=True)
    looking_for_in_spouse_marital = models.CharField(max_length=50, choices=SPOUSE_MARITAL_STATUS_OPTIONS, null=True, blank=True)
    spouse_relocation = models.CharField(max_length=50, choices=SPOUSE_RELOCATION_OPTIONS, null=True, blank=True)

    last_name_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    about_me_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    about_my_ideal_spouse_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    #bypass_admin_contact_directly_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    children_from_previous_marriage_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    #permission_share_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    significant_health_issues_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    father_country_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    mother_country_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    spouse_ethnicity_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    spouse_height_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    spouse_education_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    spouse_profession_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    spouse_visa_status_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    city_of_residence_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    country_of_birth_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    countries_of_citizenship_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    email_address_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    facebook_link_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    children_gender_age_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    instagram_link_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    language_spoken_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    first_name_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    looking_for_in_spouse_age_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    occupation_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    phone_number_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    #provide_contact_if_yes_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    race_ethnicity_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    state_of_residence_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    country_of_residence_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    references_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    #preferred_method_of_contact_by_admin_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    relationship_of_person_completing_form_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    #year_of_birth_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    marital_status_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    custody_of_children_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    willing_to_relocate_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    us_visa_status_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    muslim_origin_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    religious_sect_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    education_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    travel_for_job_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    height_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    weight_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    drink_alcohol_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    smoke_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    prays_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    fast_ramadan_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    visit_shrine_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    wear_hijab_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    time_frame_marriage_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    looking_for_in_spouse_marital_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')
    spouse_relocation_answer = models.CharField(max_length=100, choices=ANSWER_OPTIONS, default='OK')

    def __str__(self):
        return self.last_name

    def get_absolute_url(self):
        return reverse('person-detail', kwargs={'pk': self.pk})

    # @receiver(post_save, sender=User)
    # def create_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Person.objects.create(user=instance)

