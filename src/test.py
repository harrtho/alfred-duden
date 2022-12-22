#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2022 Thomas Harr <xDevThomas@gmail.com>
# Copyright (c) 2014 Dean Jackson <deanishe@deanishe.net>
#
# MIT Licence. See http://opensource.org/licenses/MIT
#
# Created on 2014-08-03
#

"""Simple tests for Duden parser."""


import duden
from workflow import Workflow

wf = Workflow()
duden.log = wf.logger

terms = [
    'Untergang',
    'Lageru',
    'Eröffnung',
    'skandieren',
    'Pumps',
    'in puncto',
]


for t in terms:

    results = duden.lookup(t)
    print('{} results for `{}`'.format(len(results), t))

    for d in results:
        print(d['term'])
        print(d['description'])
        print(d['url'])
        print()
