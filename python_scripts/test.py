operation_mode = hass.states.get('climate.foyer').attributes

logger.warning("Current Operation Mode: {}".format(operation_mode))