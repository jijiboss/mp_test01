from django.contrib import admin
from .resources import Mp_LoadResource #for import-export
from .resources import CarriersResource #for import-export
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import mp_Load
from .models import truck_stop
from .models import carriers
from .models import notify_on_order_status_change
from .models import notify_on_location
from .models import notify_on_event_update
from .models import notify_on_schedule_alert

#Add this model to the admin panel
#admin.site.register(mp_Load)
admin.site.register(truck_stop)
#admin.site.register(carriers)
admin.site.register(notify_on_order_status_change)
admin.site.register(notify_on_location)
admin.site.register(notify_on_event_update)
admin.site.register(notify_on_schedule_alert)

@admin.register(carriers)
class carriersAdmin(ImportExportModelAdmin):
#    list_display = ('number', 'carrier_name', 'stop_name')
    list_display = ('carrier_id', 'scac_mc', 'carrier_name')
    resource_class = CarriersResource #Used for import-export

@admin.register(mp_Load)
class mp_LoadAdmin(ImportExportModelAdmin):
#    list_display = ('number', 'carrier_name', 'stop_name')
#    list_display = ('number', 'carrier_id', 'stop_name')
    resource_class = Mp_LoadResource #Used for import-export
