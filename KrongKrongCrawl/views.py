from django.shortcuts import render
from django.http import HttpResponse

from .models import CauData
from .models import ElectricData
from .models import SocialData
from .models import BisData
from .models import CmpengData


def index(request):
    #CAU
    cauDatas = CauData.objects.all()
    str = ""
    for cauData in cauDatas:
        str += cauData.title
        str += cauData.link
    
    #Electric
    electricDatas = ElectricData.objects.all()
    str = ""
    for electricData in electricDatas:
        str += electricData.title
        str += electricData.link
        
    #Social    
    socialDatas = SocialData.objects.all()
    str = ""
    for socialData in socialDatas:
        str += socialData.title
        str += socialData.link
        
    #Bis    
    bisDatas = BisData.objects.all()
    str = ""
    for bisData in bisDatas:
        str += bisData.title
        str += bisData.link
    
    #cmpeng
    cmpengDatas = CmpengData.objects.all()
    str = ""
    for cmpengData in cmpengDatas:
        str += cmpengData.title
        str += cmpengData.link        
        
        
        
    return render(request, 'KrongKrongCrawl/index.html', {'cauDatas' : cauDatas, 'electricDatas' : electricDatas, 'socialDatas' : socialDatas, 'bisDatas' : bisDatas, 'cmpengDatas' : cmpengDatas})
