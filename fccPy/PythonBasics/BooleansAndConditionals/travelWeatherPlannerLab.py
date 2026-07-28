
def determiningTravel(distance_mi, is_raining, has_bike, has_car, has_ride_share_app):
  if not distance_mi:
    return False
  elif distance_mi <= 1:
    if not is_raining:
      return True
    else:
      return False
  elif distance_mi >1 and distance_mi <= 6:
    if not is_raining and has_bike:
      return True
    else:
      return False
  elif distance_mi > 6:
    if has_car or has_ride_share_app:
      return True
    else:
      return False

travelParameters = determiningTravel(23, False, True, False, True)
if travelParameters:
  print("Yes, it is possible to travel")
else:
  print("You can't travel now")
