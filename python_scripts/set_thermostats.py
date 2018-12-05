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
operation_mode = hass.states.get('input_select.home_climate_mode').state
logger.warning("Current Operation Mode: {}".format(operation_mode))

if house_mode == 'Away':
  dstairs_heat_setpoint = 68
  upstairs_radiant_heat_setpoint = 65
  
  dstairs_cool_setpoint = 84
  
elif house_mode == 'Sleep':
  # hass.services.call('climate', 'set_away_mode', {'entity_id': 'climate.downstairs', 'away_mode': 'off'})
  
  dstairs_heat_setpoint = 68
  upstairs_radiant_heat_setpoint = 65
  
  dstairs_cool_setpoint = 84
  
elif house_mode == 'Home':
  # hass.services.call('climate', 'set_away_mode', {'entity_id': 'climate.downstairs', 'away_mode': 'off'})
  
  dstairs_heat_setpoint = 70
  upstairs_radiant_heat_setpoint = 70
  
  dstairs_cool_setpoint = 75

if operation_mode == 'Heat':
  # hass.services.call('climate', 'set_temperature', {'entity_id': 'climate.downstairs', 'temperature': dstairs_heat_setpoint})
  # hass.services.call('climate', 'set_temperature', {'entity_id': 'climate.dining_room', 'temperature': dstairs_heat_setpoint})
  hass.services.call('climate', 'set_temperature', {'entity_id': 'group.downstairs_climate', 'temperature': dstairs_heat_setpoint})
  logger.warning("Downstairs Heat Setpoint: {}".format(dstairs_heat_setpoint))
  
  hass.services.call('climate', 'set_temperature', {'entity_id': 'climate.master_bath', 'temperature': upstairs_radiant_heat_setpoint})
  hass.services.call('climate', 'set_temperature', {'entity_id': 'climate.hall_bath', 'temperature': upstairs_radiant_heat_setpoint})
  logger.warning("Upstairs Radiant Heat Setpoint: {}".format(upstairs_radiant_heat_setpoint))
  
# elif operation_mode == 'cool':
#   hass.services.call('climate', 'set_temperature', {'entity_id': 'climate.living_room', 'temperature': dstairs_cool_setpoint})
#   logger.warning("Downstairs Cool Setpoint: {}".format(dstairs_cool_setpoint))