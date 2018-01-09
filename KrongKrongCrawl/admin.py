from django.contrib import admin

from .models import CauData
from .models import ElectricData
from .models import SocialData
from .models import BisData
from .models import CmpengData


admin.site.register(CauData)

admin.site.register(ElectricData)

admin.site.register(SocialData)
admin.site.register(BisData)
admin.site.register(CmpengData)
