#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'JJ'
SITENAME = u'*JJ'
SITESUBTITLE = ""
SITEURL = ''
EMAIL = "JJ@jdotjdot.com"
LOCALE = 'en_US'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

PATH = "content"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# FEED_RSS = 'feeds/all.rss.xml'
# CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (("Github", "https://github.com/jdotjdot", "fa-github"),
          ("Stack Overflow", "http://stackoverflow.com/users/1351335/jdotjdot", "fa-stack-overflow"),
          ("Twitter", "https://twitter.com/JdotJdotF", "fa-twitter"),
          # ("LinkedIn", "https://www.linkedin.com/profile/view?id=33291459", "fa-linkedin-square")
          )

MENUITEMS = (("Archives", SITEURL + '/archives/'),)

GOOGLE_ANALYTICS_ID = "UA-47960248-1"
GOOGLE_ANALYTICS_SITENAME = 'blog.jdotjdot.com'

DEFAULT_PAGINATION = 20
DISPLAY_PAGES_ON_MENU = True

ARTICLE_URL = "{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{slug}/index.html"

YEAR_ARCHIVE_SAVE_AS = "posts/{date:%Y}/index.html"
MONTH_ARCHIVE_SAVE_AS = "posts/{date:%Y}/{date:%b}/index.html"
ARCHIVES_SAVE_AS = "archives/index.html"

TAG_URL = "tags/{slug}"
TAG_SAVE_AS = "tags/{slug}/index.html"

CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

TAG_CLOUD_STEPS = 6
# TAG_CLOUD_MAX_ITEMS = 25

THEME = '../Gum-JJ'
# Themes I like:
# BT3-Flat
# Just-Read's archive feature
# gum is ok
# html5-dopetrope's date display
#pelican-cait (lacking tags?)
#pelican-mocking bird as a design base
# plumage - nice setup
# really like sundown



# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATH = r'/Users/JJ/Coding/pelican-plugins/'
PLUGINS = ['assets', 'sitemap', 'gravatar',
            'multi_part', # allows for multipart posts
            'share_post', #https://github.com/getpelican/pelican-plugins/tree/master/share_post
            'simple_footnotes', #https://github.com/getpelican/pelican-plugins/tree/master/simple_footnotes
            ]

TYPOGRIFY = True
WITH_FUTURE_DATES = False

STATIC_PATHS = ['images', ]

# things required for deploy:
# gum-jj repo
# pelican-plugins repo
