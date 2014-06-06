#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://blog.jdotjdot.com'
# SITEURL = 'https://jdotjdot.github.io'
RELATIVE_URLS = False
OUTPUTDIR = 'jdotjdot.github.io'

if os.getenv('HEROKU') == 'True':
    PATH = '/app/content' #'/app/content'
    PLUGIN_PATH = '../pelican-plugins'
    THEME = '../Gum-JJ'
    ASSET_CONFIG = (('directory', '/app/{}/theme'.format(OUTPUTDIR)),
                    #('SASS_BIN', '/app/.heroku/python/lib/python2.7/site-packages/sass.so')
                    )
    # DELETE_OUTPUT_DIRECTORY = True


FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/category/%s.atom.xml'
TAG_FEED_ATOM = 'feeds/tag/%s.atom.xml'



# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""

