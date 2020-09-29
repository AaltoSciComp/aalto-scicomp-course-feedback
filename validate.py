#!/usr/bin/env python

import datetime
import dateutil.parser
import json
import sys

from jsonschema import validate
import yaml

schema = yaml.safe_load(open(sys.argv[1]))
data = yaml.safe_load(open(sys.argv[2]))

if dateutil.parser.parse(data['date']).date() > datetime.date.today():
    schema['required'] += schema['required_post']


validate(data, schema)

