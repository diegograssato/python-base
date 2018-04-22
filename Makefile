#Defines the default behaviour for make and make all

.PHONY: all install init dependencies venv deb run

SHELL := /bin/bash

all: run

init: dependencies

install:
	@echo "-- Performing the OS packages installation"
	sudo apt-get install python3-venv python3-pip build-essential python3-setuptools
	sudo pip install --upgrade pip
	sudo pip install --upgrade virtualenv

dependencies:
	@echo "-- Performing the project dependencies installation"
	 ( \
       source venv/bin/activate; \
       pip install -r requirements.txt; \
    )

env:
	@echo "-- Creating the virtual env for this project"
	cd venv 2> /dev/null || python3 -m venv venv
	@echo "-- Run to load virtual env" \
	    source venv/bin/activate

deb:
	@echo "-- Creating debian package"
	debuild clean
	dpkg-buildpackage -us -uc -b
	debuild clean
	rm -rfv *.egg-info
	rm -rfv dist

run: env init