#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import pathlib

root_path = pathlib.Path(__file__).parent

AUTHOR = 'Mcko'
SITENAME = "Mcko's blog"
SITEURL = 'https://mcko.me'

PLUGINS = ['i18n_subsites', 'cjk-auto-spacing']
PLUGIN_PATHS = [str(root_path.joinpath('plugins'))]

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

THEME = str(root_path.joinpath('blog-theme/elegant/').absolute())

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

# i18n
I18N_SUBSITES = {
    'en': {'THEME': THEME}
    }

# Google Analytics
GOOGLE_ANALYTICS = 'UA-68128263-2'

# Disqus
DISQUS_SITENAME = 'mckos-blog'

# Feed Items
FEED_MAX_ITEMS = 15
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

# Landing page
LANDING_PAGE_TITLE = 'Learning to learn'
