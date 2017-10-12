from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget
from .models import carriers
from .models import truck_stop
from .models import mp_Load

class CarriersResource(resources.ModelResource):

    class Meta:
        model = carriers
        ski_unchanged = True
        import_id_fields = ('carrier_id',)
        fields = ('carrier_id', 'scac_mc', 'carrier_name')
        import_order = ('carrier_id', 'scac_mc', 'carrier_name')

class Mp_LoadResource(resources.ModelResource):
    # Use the ForeignKeyWidget to lookup a related model using “natural keys”, i.e., lookup without using the Primary Key (“id”).
    # https://django-import-export.readthedocs.io/en/latest/api_widgets.html

#    carrier_name = fields.Field(column_name='carrier_name', attribute='carrier_name', widget=ForeignKeyWidget(carriers, 'carrier_name'))
#    carrier_id = fields.Field(column_name='carrier_id', attribute='carrier_id', widget=ForeignKeyWidget(carriers, 'carrier_id'))
#    stop_name = fields.Field(column_name='stop_name', attribute='stop_name', widget=ForeignKeyWidget(truck_stop, 'stop_name'))

    class Meta:
        model = mp_Load
        skip_unchanged = True
        import_id_fields = (
            'id_number', # Our load identifier
        )

        fields = (
#            'number', # GPS/Cell number to track by
#            'track_start_date_time', # When to start tracking in format YYYY-MM-DD HH:MM
#            'track_start_date_time_TZ', # Timezone for track_start_date_time
#            'track_duration_hours', # How long to track for
#            'track_interval_minutes', #Frequency for locatio update
#            'partner_id', # My MPID, used for notification
            'id_number', # Our load identifier
#            'carrier_name', # Carrier name
#            'carrier_id', # Our internal name for the carrier
#            'last_stop_event_completed', # Allows to report "Arrived" oir "Departed"
#            'stop_id', # Unique ID within trip sheet assigned to the stop
#            'stop_name', # ID of the stop with the name resolved
#            'stop_type', # Pickup or Drop off
#            'start_date_time', # ETA in ISO8601
#            'start_date_time_TZ', # Timezone for StartDateTime, user defined
#            'end_date_time', # ETD in ISO8601
#            'end_date_time_TZ', # Timezone for EndDateTime, user defined
#            'stop_notes', # Notes on the Stop
#            'email_updates_to',
#            'load_notes'
        )

        import_order = (
#            'number', # GPS/Cell number to track by
#            'track_start_date_time', # When to start tracking in format YYYY-MM-DD HH:MM
#            'track_start_date_time_TZ', # Timezone for track_start_date_time
#            'track_duration_hours', # How long to track for
#            'track_interval_minutes', #Frequency for locatio update
#            'partner_id', # My MPID, used for notification
            'id_number', # Our load identifier
#            'carrier_name', # Carrier name
#            'carrier_id', # Our internal name for the carrier
#            'last_stop_event_completed', # Allows to report "Arrived" oir "Departed"
#            'stop_id', # Unique ID within trip sheet assigned to the stop
#            'stop_name', # ID of the stop with the name resolved
#            'stop_type', # Pickup or Drop off
#            'start_date_time', # ETA in ISO8601
#            'start_date_time_TZ', # Timezone for StartDateTime, user defined
#            'end_date_time', # ETD in ISO8601
#            'end_date_time_TZ', # Timezone for EndDateTime, user defined
#            'stop_notes', # Notes on the Stop
#            'email_updates_to',
#            'load_notes'
        )
