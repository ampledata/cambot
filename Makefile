# Makefile for Cambot.
#
# Author:: Greg Albrecht <gba@orionlabs.io>
# Copyright:: Copyright 2016 Orion Labs, Inc.
# License:: All rights reserved. Do not redistribute.
#


.DEFAULT_GOAL := all


all: install_requirements develop

develop: install_requirements
	python setup.py develop

install: install_requirements
	python setup.py install

install_requirements:
	pip install --upgrade -r requirements.txt

uninstall:
	pip uninstall -y cambot

clean:
	rm -rf *.egg* build dist *.py[oc] */*.py[co] cover doctest_pypi.cfg \
		nosetests.xml pylint.log *.egg output.xml flake8.log tests.log \
		test-result.xml htmlcov fab.log *.deb *.eggs

nosetests:
	python setup.py nosetests

pep8:
	flake8

flake8: 
	flake8 --max-complexity 12 --exit-zero cambot/*.py *.py

lint:
	pylint --msg-template="{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}" \
	-r n cambot/*.py *.py || exit 0

test: lint flake8 nosetests
