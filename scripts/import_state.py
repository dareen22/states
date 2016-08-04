#!/usr/bin/env python

import csv
import os
import sys

sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from main.models import State

states = State.objects.all()

print states