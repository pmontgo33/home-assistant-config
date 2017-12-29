"""
test_app.py
Test App
"""

import appdaemon.appapi as appapi
import datetime

class TestApp(appapi.AppDaemon):

	def initialize(self):
		time = datetime.time(20, 25)
		self.log("Time: " + time)
		self.run_daily(self.run_daily_callback, time)
		
	def run_daily_callback(self, kwargs):
		self.turn_off("switch.living_room_ligh_switch")