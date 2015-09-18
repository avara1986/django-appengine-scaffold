#!/bin/sh
coverage erase
tox
coverage combine
coverage report -m --omit=sitepackages/*,.tox/*
coverage html --omit=sitepackages/*,.tox/*
#python functional_tests.py