#!/usr/bin/env python3

import argparse
import os.path
from os import environ as env
import mapproxy.script.util
import mapproxy.wsgiapp
import mapproxy.util.ext.serving
import logging

def main():
	config_dir="/opt/mapproxy/config"
	config="%s/mapproxy.yaml"%config_dir

	if not os.path.exists(config):
		print("Creating initial mapproxy configuration")
		try:
			mapproxy.script.util.create_command(["","-t","base-config",config_dir])
		except SystemExit as e:
			if e.code!=0:
				quit(e.code)

	app = mapproxy.wsgiapp.make_wsgi_app(config)
	if 'DEBUG' in env and bool(env['DEBUG']):
		mapproxy.script.util.setup_logging(level=logging.DEBUG)
	else:
		mapproxy.script.util.setup_logging()
	mapproxy.util.ext.serving.run_simple("0.0.0.0", 8080, app, use_reloader=True, processes=1,
        threaded=True, passthrough_errors=True,
        extra_files=app.config_files.keys())


if __name__ == "__main__":
	main()

