#!/usr/bin/env python3

#Paul Croft
#October 8, 2020

from bottle import get, run, static_file, template


@get("/static/<sfile>")
def get_static_asset(sfile):
	return static_file(sfile, root="static")


@get("/")
@get("/index")
def mainpage():
	return template("templates/index.html")


def main():
	run(host="0.0.0.0", port=32114, server="eventlet")

	return 0

if __name__ == '__main__':
	exit(main())