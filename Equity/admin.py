from django.contrib import admin
from .models import Futures,Options,Sectors
from .models import perform_metric
from .models import Future_Sectors,option_Sectors
from .models import Most_Volatile_Futures,Most_Volatile_Options
# Register your models here.

admin.site.register(Futures)
admin.site.register(Options)
admin.site.register(Sectors)
admin.site.register(perform_metric)
admin.site.register(Future_Sectors)
admin.site.register(option_Sectors)
admin.site.register(Most_Volatile_Futures)
admin.site.register(Most_Volatile_Options)
#admin.site.register(UserFutures)



