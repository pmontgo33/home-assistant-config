operation_mode = hass.states.get('climate.living_room').attributes['operation_mode']

logger.warning("Current Operation Mode: {}".format(operation_mode))