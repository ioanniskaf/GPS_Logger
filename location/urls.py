from django.urls import path
from . import views

urlpatterns = [
    path("i<int:interviewer>_r<int:respodent>/", views.gps_info, name="gps_info"),
]

# http://localhost:7512/location/i65461_r46151
# http://localhost:7512/location/i65468_r88951
# http://localhost:7512/location/i98451_r77512
# http://localhost:7512/location/i13456_r65413
# http://localhost:7512/location/i13456_r13469
# http://localhost:7512/location/i98451_r98744
# http://localhost:7512/location/i65468_r86218
# http://localhost:7512/location/i65468_r89401
# http://localhost:7512/location/i65461_r40235
# http://localhost:7512/location/i65461_r63214
