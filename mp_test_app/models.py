#https://docs.djangoproject.com/en/1.11/ref/models/fields/
from django.db import models

time_zones = (
    ('ET', 'Eastern Standard Time'),
    ('CT', 'Central Standard Time'),
    ('AZ', 'Arizona'),
    ('MT', 'Mountain Time'),
    ('PT', 'Pacific Standard Time'),
    ('AK', 'Alaska'),
    ('HI', 'Hawaii'),
)

types = (
    ('PU', 'Pick Up'),
    ('DO', 'Drop Off'),
)


class carriers(models.Model):
    carrier_id = models.CharField(primary_key = True, max_length = 24)
    scac_mc = models.CharField(max_length = 12)
    carrier_name = models.CharField(max_length = 128)

    def __str__(self):
        return '(' + str(self.carrier_id) + ')' + str(self.scac_mc)


class truck_stop(models.Model):
    stop_name = models.CharField(primary_key = True, max_length = 64)
    stop_latitude = models.FloatField()
    stop_longitude = models.FloatField()
    stop_address_line1 = models.CharField(max_length = 64)
    stop_address_line2 = models.CharField(max_length = 64, blank=True, default='')
    stop_city = models.CharField(max_length = 64)
    stop_state_or_province = models.CharField(max_length = 64)
    stop_postal_code = models.CharField(max_length = 16)

    def __str__(self):
        return self.stop_name



#class MP_Load(models.Model):
class mp_Load(models.Model):

    number = models.CharField(max_length = 24, blank = True, default = '') #GPS/Cell num to track by
    #not sure how to allow users to enter timzezone
    #https://stackoverflow.com/questions/14074696/django-datetimefield-with-utc-offset
    #https://stackoverflow.com/questions/35084164/django-datetimefield-timezone-aware-cet
    track_start_date_time = models.DateTimeField()
    track_start_date_time_TZ = models.CharField(choices = time_zones, max_length = 2, blank = True, default = '')
    track_duration_hours = models.IntegerField()
    track_interval_minutes = models.IntegerField()
    partner_id = models.IntegerField() #my MPID for notifications and stuff
    id_number = models.IntegerField(primary_key = True) #load ID
#    carrier_name = models.TextField() #may not need this instead use te foreign key carrier_id
#    carrier_name = models.ForeignKey(carriers) #over ID because users would not know the ID
#    carrier_id = models.ForeignKey(carriers) #carrier ID to looku pagainst the carriers table
#    last_stop_event_completed = models.CharField(max_length = 64, blank=True, default='')
#    last_stop_event_completed = models.CharField(max_length = 64, blank=True)
#    stop_id = models.CharField(max_length = 12) #this is not part of the truck_stop table
#    stop_name = models.ForeignKey(truck_stop) #Name of the stop
#    stop_type = models.CharField(choices = types, max_length = 2)
#    start_date_time = models.DateTimeField()
#    start_date_time_TZ = models.CharField(choices = time_zones, max_length = 2)
#    end_date_time = models.DateTimeField()
#    end_date_time_TZ = models.CharField(choices = time_zones, max_length = 2)
#    stop_notes = models.TextField(blank=True, default='')
#    email_updates_to = models.CharField(max_length = 64, blank=True, default='')
#    load_notes = models.TextField(blank=True, default='')

    #Following are response on the load from MP. Identified by the field names ending with "_MP".
#    order_id_MP = models.CharField(unique = True, max_length = 32, blank=True, default='') #returned from MP
#    order_status_MP = models.CharField(max_length = 64, blank=True, default='') #returned from MP
#    order_error_code_MP = models.IntegerField(blank=True, default='') #returned from MP
#    order_error_message_MP = models.TextField(blank=True, default='') #returned from MP
#    order_rev_num = models.IntegerField(default=0) #Revisionnumber, my code need to update

    def __str__(self):
        return str(self.id_number)

class notify_on_order_status_change(models.Model):
#class foo (models.Model):
    #order_id_MP = models.ForeignKey(MP_Load)
    order_id_number = models.ForeignKey(mp_Load) #this will be used to retireve both order_id_MP and id_number
    status_code = models.IntegerField()
    status_message = models.TextField()
    status_time_stamp = models.DateTimeField()

    def __str__(self):
        return self.order_id_number

class notify_on_location(models.Model):
    order_id_number = models.ForeignKey(mp_Load) #this will be used to retireve both order_id_MP and id_number
    latitude = models.FloatField()
    longitude = models.FloatField()
    uncertainty = models.IntegerField()
    street1 = models.CharField(max_length = 64)
    street2 = models.CharField(max_length = 64)
    neighborhood = models.CharField(max_length = 128)
    city = models.CharField(max_length = 128)
    state = models.CharField(max_length = 128)
    postal = models.IntegerField()
    country = models.CharField(max_length = 128)
    location_time_utc = models.DateTimeField()
    location_time_local = models.DateTimeField()

    def __str__(self):
        return self.order_id_number

class notify_on_event_update(models.Model):
    order_id_number = models.ForeignKey(mp_Load) #this will be used to retireve both order_id_MP and id_number
    stop_name = models.ForeignKey(truck_stop) #Name of the stop
    stop_id = models.CharField(max_length = 12)
    event_code = models.CharField(max_length = 6)
    event_time_utc = models.DateTimeField()
    event_time_local = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    street1 = models.CharField(max_length = 64)
    street2 = models.CharField(max_length = 64)
    neighborhood = models.CharField(max_length = 128)
    city = models.CharField(max_length = 128)
    state = models.CharField(max_length = 128)
    postal = models.IntegerField()
    country = models.CharField(max_length = 128)

    def __str__(self):
        return self.order_id_number

class notify_on_schedule_alert(models.Model):
    order_id_number = models.ForeignKey(mp_Load) #this will be used to retireve both order_id_MP and id_number
    stop_type = models.CharField(choices = types, max_length = 2)
    stop_id = models.CharField(max_length = 12)
    stop_name = models.ForeignKey(truck_stop) #Name of the stop
    address_line1 = models.CharField(max_length = 64)
    city = models.CharField(max_length = 64)
    state = models.CharField(max_length = 64)
    postal = models.CharField(max_length = 16)
    alert_code = models.IntegerField()
    schedule_time_begin_local = models.DateTimeField()
    schedule_time_end_local = models.DateTimeField()
    location_time_utc = models.DateTimeField()
    schedule_alert_text = models.TextField()

    def __str__(self):
        return self.order_id_number
