from django.contrib import admin
from .models import conference,individual_pub,progress_master,progress_phd

class conferenceAdmin(admin.ModelAdmin):
    list_display = ('journal_conf_name','place','Start_date','End_date','calendar')

class individual_pubAdmin(admin.ModelAdmin):
    list_display = ('number_pub','pub_THname','pub_ENGname','journal_DB','journal_conf_name','Imple_organ','release_type')

class progress_masterAdmin(admin.ModelAdmin):
    list_display = ('number_Master','Master_no','Master_course','Master_name','study_plan','stu_status','graduation_y','pub_THname','Advisor_1','Advisor_2')

class progress_phdAdmin(admin.ModelAdmin):
    list_display = ('number_PhD','PhD_no','PhD_course','PhD_name','study_plan','stu_status','graduation_y','pub_THname','Advisor_1','Advisor_2')

admin.site.register(conference,conferenceAdmin)
admin.site.register(individual_pub,individual_pubAdmin)
admin.site.register(progress_master,progress_masterAdmin)
admin.site.register(progress_phd,progress_phdAdmin)
