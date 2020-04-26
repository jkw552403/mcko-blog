#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import pathlib

AUTHOR = 'Mcko'
SITENAME = 'Writing for Writing'
SITEURL = 'https://mcko.me'

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

THEME = str(pathlib.Path(__file__).parent.joinpath('blog-theme/elegant/').absolute())

DEFAULT_LANG = 'zh-tw'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         )

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
