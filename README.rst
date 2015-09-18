.. contents::

# django-appengine-scaffold

Information
===========


Installation
============

::

    virtualenv vapp
    vapp/bin/activate
    pip installl -r requirements-dev.txt

Run project
===========

::

    ./run_project.sh


Executing the test 
==================

::

    ./tests.sh
    python functional_tests.py


Upload to GAE
=============

::

    python install_deps.py
    appcfg.py update ./
