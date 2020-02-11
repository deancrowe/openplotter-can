#!/usr/bin/env python3

# This file is part of Openplotter.
# Copyright (C) 2015 by Sailoog <https://github.com/openplotter/openplotter-can>
#
# Openplotter is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# any later version.
# Openplotter is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Openplotter. If not, see <http://www.gnu.org/licenses/>.
import os, subprocess, time
from openplotterSettings import conf
from openplotterSettings import language

def main():
	conf2 = conf.Conf()
	currentdir = os.path.dirname(__file__)
	currentLanguage = conf2.get('GENERAL', 'lang')
	language.Language(currentdir,'openplotter-can',currentLanguage)
	error = False

	print(_('Removing openplotter-can-read service...'))
	try:
		subprocess.call(['systemctl', 'disable', 'openplotter-can-read'])
		subprocess.call(['systemctl', 'stop', 'openplotter-can-read'])
		subprocess.call(['rm', '-f', '/etc/systemd/system/openplotter-can-read.service'])
		subprocess.call(['systemctl', 'daemon-reload'])
		print(_('DONE'))
	except Exception as e:
		print(_('FAILED: ')+str(e))
		error = True

	print(_('Removing version...'))
	try:
		conf2.set('APPS', 'can', '')
		print(_('DONE'))
	except Exception as e: 
		print(_('FAILED: ')+str(e))
		error = True

	if error: time.sleep(10)
	else: time.sleep(2)

if __name__ == '__main__':
	main()