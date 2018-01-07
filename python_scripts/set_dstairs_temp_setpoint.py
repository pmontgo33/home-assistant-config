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

# downstairs_op_mode = hass.states.get('climate.downstairs_cooling_1').attributes.get('operation_mode')
# logger.warning("Downstairs operation mode: {}".format(downstairs_op_mode))

# if downstairs_op_mode == 'Heat':
if house_mode == 'Away':
  heat_setpoint = float(hass.states.get('input_number.dstairs_away_heat_temp').state)
  cool_setpoint = float(hass.states.get('input_number.dstairs_away_cool_temp').state)
  
elif house_mode == 'Sleep':
  heat_setpoint = float(hass.states.get('input_number.dstairs_sleep_heat_temp').state)
  cool_setpoint = float(hass.states.get('input_number.dstairs_sleep_cool_temp').state)
  
elif house_mode == 'Home':
  heat_setpoint = float(hass.states.get('input_number.dstairs_home_heat_temp').state)
  cool_setpoint = float(hass.states.get('input_number.dstairs_home_cool_temp').state)

logger.warning("Heat Setpoint: {}, Cool Setpoint: {}".format(heat_setpoint, cool_setpoint))
hass.services.call('climate', 'set_temperature', {'entity_id': 'climate.downstairs_heating_1', 'temperature': heat_setpoint})
hass.services.call('climate', 'set_temperature', {'entity_id': 'climate.downstairs_cooling_1', 'temperature': cool_setpoint})

# elif downstairs_op_mode == 'Cool':
#   if house_mode == 'Away':
#     new_setpoint = float(hass.states.get('input_number.dstairs_away_cool_temp').state)
    
#   elif house_mode == 'Sleep':
#     new_setpoint = float(hass.states.get('input_number.dstairs_sleep_cool_temp').state)
    
#   elif house_mode == 'Home':
#     new_setpoint = float(hass.states.get('input_number.dstairs_home_cool_temp').state)
  
#   hass.services.call('climate', 'set_temperature', {'entity_id': 'climate.downstairs_cooling_1', 'temperature': new_setpoint})