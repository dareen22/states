#!/usr/bin/env python
import csv
import os
import sys

sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from app.models import State

import django
django.setup()


# states = State.objects.all().order_by('capital')

# states = State.objects.all().exclude(name__startswith="C").order_by('name')

# states = State.objects.all().filter(name__startswith="C").order_by('name')

# states = State.objects.all().values('name', 'population')

states = State.objects.all().values_list('name', 'abbreviation', 'population')

# for a, b, c in states:
#	print a
#	print b
#	print c

for state in states:
	print state


#for state in states:
#		print "%s | %s | %s" % (state.name, state.capital, state.population)