"""
outside_lights.py
Outside Lights App
"""

import appdaemon.appapi as appapi

class OutsideLights(appapi.AppDaemon):

	def initialize(self):
		self.run_at_sunset(self.sunset_cb)
		self.run_at_sunrise(self.sunrise_cb)
	
	def sunset_cb(self, kwargs):
		self.turn_on("switch.front_lights_switch")
	
	def sunrise_cd(self, kwargs):
		self.turn_off("switch.front_lights_switch")