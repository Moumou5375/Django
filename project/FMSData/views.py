from django.shortcuts import render
from django.http import HttpResponse
from .models import individual_pub
from .models import conference
from .models import progress_master
from .models import progress_phd

def Bar(request):
  individual = individual_pub.objects.all()

  vara = individual_pub.objects.filter(release_type='วารสาร').count()
  chatt = individual_pub.objects.filter(release_type='การประชุมวิชาการระดับชาติ').count()
  nana = individual_pub.objects.filter(release_type='การประชุมวิชาการระดับนานาชาติ').count()
  nuang = individual_pub.objects.filter(release_type='ตีพิมพ์ลักษณะใดลักษณะหนึ่ง').count()
 
  vara = int(vara)
  chatt = int(chatt)
  nana = int(nana)
  nuang = int(nuang)
 
  Release_type_list = ['วารสาร','การประชุมวิชาการระดับชาติ','การประชุมวิชาการระดับนานาชาติ','ตีพิมพ์ลักษณะใดลักษณะหนึ่ง']
  number_list = [vara, chatt, nana, nuang]
  context = {'Release_type_list':Release_type_list,'number_list':number_list,'individual':individual}

 
  return render(request, 'Bar.html', context)

def Home(request):
    return render(request,'Home.html')

def donut(request):
  Conference = conference.objects.all()

  song = conference.objects.filter(calendar=2012).count()
  sam = conference.objects.filter(calendar=2013).count()
  see = conference.objects.filter(calendar=2014).count()
  ha = conference.objects.filter(calendar=2015).count()
  hog = conference.objects.filter(calendar=2016).count()
  jed = conference.objects.filter(calendar=2017).count()
  pad = conference.objects.filter(calendar=2018).count()
 
  song = int(song)
  sam = int(sam)
  see = int(see)
  ha = int(ha)
  hog = int(hog)
  jed = int(jed)
  pad = int(pad)

  Calendar_list = [2012,2013,2014,2015,2016,2017,2018]
  number_list = [song, sam, see, ha,hog,jed,pad]
  context = {'Calendar_list':Calendar_list,'number_list':number_list,'conference':Conference}

 
  return render(request, 'donut.html', context)

def graph1(request):
  Progress_Master = progress_master.objects.all()
  Progress_PhD = progress_phd.objects.all()

  song = progress_master.objects.filter(Master_course='MBA').count()
  sam = progress_master.objects.filter(Master_course='MBA.Mkt').count()
  see = progress_master.objects.filter(Master_course='IMBA').count()
  ha = progress_master.objects.filter(Master_course='M.Acc').count()
  hog = progress_master.objects.filter(Master_course='MPA').count()
  jed = progress_phd.objects.filter(PhD_course='Ph.D').count()

  song = int(song)
  sam = int(sam)
  see = int(see)
  ha = int(ha)
  hog = int(hog)
  jed = int(jed)

  Progress_list = ['MBA','MBA.Mkt','IMBA','M.Acc','MPA','Ph.D']
  number_list = [song, sam, see, ha,hog,jed]
  context = {'Progress_list':Progress_list,'number_list':number_list,'progress_Master':Progress_Master,'progress_PhD':Progress_PhD}
  return render(request, 'graph1.html', context)

def graph2(request):
  individual = individual_pub.objects.all()

  song = individual_pub.objects.filter(journal_DB='ฐานข้อมูลระดับนานาชาติอื่นๆ').count()
  sam = individual_pub.objects.filter(journal_DB='TCI กลุ่ม 1').count()
  see = individual_pub.objects.filter(journal_DB='Scopus').count()
  ha = individual_pub.objects.filter(journal_DB='WoS').count()
  hog = individual_pub.objects.filter(journal_DB='TCI กลุ่ม 2').count()
  jed = individual_pub.objects.filter(journal_DB='SSRN').count()
  pad = individual_pub.objects.filter(journal_DB='EBSCO').count()
  kaw = individual_pub.objects.filter(journal_DB='ไม่อยู่ในฐานข้อมูล').count()

  song = int(song)
  sam = int(sam)
  see = int(see)
  ha = int(ha)
  hog = int(hog)
  jed = int(jed)
  pad = int(pad)
  kaw = int(kaw)

  individual_list = ['ฐานข้อมูลระดับนานาชาติอื่นๆ','TCI กลุ่ม 1','Scopus','WoS','TCI กลุ่ม 2','SSRN','EBSCO','ไม่อยู่ในฐานข้อมูล']
  number_list = [song, sam, see, ha,hog,jed,pad,kaw]
  context = {'individual_list':individual_list,'number_list':number_list,'individual':individual}
  return render(request, 'graph2.html', context)
