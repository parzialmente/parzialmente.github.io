#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Giacomo Ritucci'
SITENAME = u'parzialmente.it'
SITEURL = 'http://parzialmente.it'

TIMEZONE = 'Europe/Rome'

DEFAULT_DATE = u'fs'

DEFAULT_LANG = u'it'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Il Bibliotecarbaro', 'http://bibliotecarbaro.wordpress.com/'),)

# Social widget
SOCIAL = (('github', 'https://github.com/rjack/'),
          ('twitter', 'https://twitter.com/giacomoritucci'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['img', 'js']

# GitHub Pages
FILES_TO_COPY = (('CNAME', 'CNAME'),
                 ('README.md', 'README.md'),)

TYPOGRIFY = True
