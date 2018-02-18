"""
if cooling:
  if away:
    get cooling away temp
  if sleep:
    get cooling sleep temp
  else:
    get cooling home temp
if heating:
  if away:
    get heating away temp
    ...
  
"""


house_mode = hass.states.get('sensor.house_mode').state
logger.warning("Current House Mode is: {}".format(house_mode))
operation_mode = hass.states.get('climate.living_room').attributes['operation_mode']
logger.warning("Current Operation Mode: {}".format(operation_mode))

if house_mode == 'Away':
  dstairs_heat_setpoint = 68
  upstairs_radiant_heat_setpoint = 61
  
  dstairs_cool_setpoint = 84
  
elif house_mode == 'Sleep':
  dstairs_heat_setpoint = 68
  upstairs_radiant_heat_setpoint = 61
  
  dstairs_cool_setpoint = 84
  
elif house_mode == 'Home':
  dstairs_heat_setpoint = 70
  upstairs_radiant_heat_setpoint = 69
  
  dstairs_cool_setpoint = 79

if operation_mode == 'heat':
  hass.services.call('climate', 'set_temperature', {'entity_id': 'climate.living_room', 'temperature': dstairs_heat_setpoint})
  hass.services.call('climate', 'set_temperature', {'entity_id': 'climate.dining_room', 'temperature': dstairs_heat_setpoint})
  logger.warning("Downstairs Heat Setpoint: {}".format(dstairs_heat_setpoint))
  
  hass.services.call('climate', 'set_temperature', {'entity_id': 'climate.master_bath', 'temperature': upstairs_radiant_heat_setpoint})
  hass.services.call('climate', 'set_temperature', {'entity_id': 'climate.hall_bath', 'temperature': upstairs_radiant_heat_setpoint})
  logger.warning("Upstairs Radiant Heat Setpoint: {}".format(upstairs_radiant_heat_setpoint))
  
elif operation_mode == 'cool':
  hass.services.call('climate', 'set_temperature', {'entity_id': 'climate.living_room', 'temperature': dstairs_cool_setpoint})
  logger.warning("Downstairs Cool Setpoint: {}".format(dstairs_cool_setpoint))