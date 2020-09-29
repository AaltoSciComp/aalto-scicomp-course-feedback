#!/usr/bin/env python

import argparse
import datetime
import glob
import json
from os.path import dirname, join
import sys

import dateutil.parser
from jsonschema import validate
import yaml

SCHEMA = join(dirname(__file__), 'schema.yaml')
ALL_COURSES = glob.glob(join(dirname(__file__), 'courses/*.yaml'))

parser = argparse.ArgumentParser()
parser.add_argument('schema', nargs='?', help="schema file",
                    default=SCHEMA)
parser.add_argument('course', nargs='*', help="course files to process",
                    default=ALL_COURSES)
args = parser.parse_args()

schema = yaml.safe_load(open(args.schema))


for coursefile in args.course:
    print
    print(coursefile)
    data = yaml.safe_load(open(coursefile))

    if dateutil.parser.parse(data['date']).date() > datetime.date.today():
        schema['required'] += schema['required_post']

    validate(data, schema)
