from django.db import models

class conference(models.Model):
    journal_conf_name = models.CharField(max_length=500)
    place = models.CharField(max_length=500)
    Start_date = models.DateField()
    End_date = models.DateField()
    calendar = models.IntegerField()

class individual_pub(models.Model):
    number_pub = models.IntegerField()
    pub_THname = models.CharField(max_length=500)
    pub_ENGname = models.CharField(max_length=500)
    journal_DB = models.CharField(max_length=255)
    journal_conf_name = models.CharField(max_length=500)
    Imple_organ = models.CharField(max_length=500)
    release_type = models.CharField(max_length=255)

class progress_master(models.Model):
    number_Master = models.IntegerField()
    Master_no = models.CharField(max_length=50)
    Master_course = models.CharField(max_length=50)
    Master_name = models.CharField(max_length=255)
    study_plan = models.CharField(max_length=50)
    stu_status = models.CharField(max_length=100)
    graduation_y = models.IntegerField()
    pub_THname = models.CharField(max_length=500)
    Advisor_1 = models.CharField(max_length=255)
    Advisor_2 = models.CharField(max_length=255)

class progress_phd(models.Model):
    number_PhD = models.IntegerField()
    PhD_no = models.CharField(max_length=50)
    PhD_course = models.CharField(max_length=50)
    PhD_name = models.CharField(max_length=255)
    study_plan = models.CharField(max_length=50)
    stu_status = models.CharField(max_length=100)
    graduation_y = models.IntegerField()
    pub_THname = models.CharField(max_length=500)
    Advisor_1 = models.CharField(max_length=255)
    Advisor_2 = models.CharField(max_length=255)