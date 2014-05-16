Title: Static site generators and choices
Date: 2014-03-26
Slug: static-site-generators-and-choices
Category: Programming
Tags: hackerschool, pelican, jekyll, scriptogr.am, dropbox, zapier, markdown, static-site-generators
Status: published


###TL;DR
I'm undecided on exactly where to settle on hosting my site.  The main things I'm looking for are:

* Code syntax highlighting
* Nicely formatted list of categories and full archive on the sidebar
* Editing from anywhere
* Ease of publishing/deployment

###Intro

As of this writing, my Hacker School blog is hosted on [Ghost](http://ghost.org), and as much as it's nice and easy to use with a great online writing platform, my ultimate goal is to be able to write anything from anywhere, and unfortunately Ghost isn't going to fit the bill there, by nature of having an online text editor that I have to use.

I've heard quite a bit about static site generators like [Pelican][pelican] and [Jekyll][jekyll], and I went in to go take a look.  

###What is a static site generator, you ask?

Fair question.  Most blogging platforms (like Wordpress, for example) are *dynamically generated* sites--meaning that the page is being generated from underlying data in a database every time you load it.  This sounds more complicated than it is.  Think about a site like Craigslist--every time you view the same URL, the actual listings are actually always changing and being updated.  This is a dynamically generated site, because the page is changing every time.  And how is it changing?  Even though we're loading the same formatting and styling every time, the actual content of the posts to be presented to you on each load is being pulled from a database that lives elsewhere.

A while ago, someone smart noticed that your blog posts are not really going to be changing--once it's published, it's unlikely to change.  Even if you edit it, it certainly won't be changing every day (hopefully).  As a result, you don't need to dynamically create each page each time a user loads it.

The answer is a **static site generator**, which is a program that lets you build all of the HTML and CSS ahead of time and then post only the static, unchanging files.  Using something like this, you can actually serve your blog right out of something like Dropbox!  (And there are a number of offerings that do--see [Scriptogr.am][scriptogram].)  Generally, you can write your posts in any text editor using Markdown syntax or something like it.  Markdown is a super-stripped down formatting that enables you to simply and quickly write formatted text that later gets translated into HTML.  (Examples: `*italics*` makes things *italic*, `**bold**` makes things **bold**, `[This is a URL!](http://www.google.com)` makes things into [URLS](http://www.google.com).)

This means that you can create and edit posts from anywhere.  When you're ready, you save them into your site generators posts folder and run the program, which generates a fully featured site based on your posts' content and your selected theme, which styles everything.

###Jekyll

Jekyll seemed great at first, and I particularly liked the fact that it can be easily hosted on Github Pages without any extra work (or even site generation) on my part, since Github will run the Jekyll page generation for you.  Unfortunately, it only does that for Jekyll, and not for any others, like Pelican.  The other issue I ran into is Jekyll is pretty unwieldy--and even using Octopress, which sites on top of Jekyll, I still had quite a bit of trouble getting into the meat of it.  After some Googling, I found that I was far from the only Python person having trouble, and you need to have some Ruby skills if Jekyll ever breaks.

###Pelican

Next stop was Pelican, which is a static site generator similar to Jekyll, but in Python.  It's also a bit tough to set up, but I'm liking it a bit more, since I have a better understanding of the internals due to it being in Python.   On the other hand, I've still found it a bit of a handful to set up (spent a few hours on it and I'm not quite there yet!).  Additionally, it's still not *quite* "edit from anywhere"--I know that I can create and edit posts in any text editor and offline, but at the end of the day, I'll still have to move all of my posts to the contents folder in my blog repo, run the `pelican` command to generate the site, and then push the site to the final Github repo.  I can set this all up automatically with Fabric or web hooks, but at the end of the day, it's still a little bit annoying.

###Scriptogr.am
Scriptogr.am is a very cool hosted static site generator that runs out of Dropbox.  All you have to do is save your Markdown-formatted files to your special "Scriptogram" Dropbox folder, and Scriptogr.am automatically loads the files there, runs them through its own site generator using your selected (or customized) theme, and then hosts the site for you.  This is really great because you truly can edit or post from anywhere, as all you have to do is save to Dropbox, and everything happens automatically from there.  You can even publish right to Scriptogr.am from Markdown-editing programs like Mou for Mac.

The downside is, given that it's a hosted solution, I have quite a bit less control over the blog itself.  I'm sure I could manage to force the theme to do my will, but it would mean quite a bit of effort messing with the built-in HTML and CSS themes, and given that it's still a pretty small site, there aren't that many themes offered out of the box.  I'm also not totally clear if there's an RSS feed built-in.

###Conclusion
None yet.  I'm right now between Scriptogr.am and Pelican, but given that I like the ease of use of Scriptogr.am but the control of Pelican, I'm likely to go with a combined scenario, where I'll basically create my own automatically-publishing version of Pelican out of Dropbox.  Basically, what I will do is create a small Heroku instance that will do nothing but listen for a web hook from Dropbox, and upon receiving it, pull all of the files stored in the Dropbox folder, run the Pelican site generator, commit the repo, and then push to Github pages.
Unfortunately, Dropbox doesn't currently support web hooks.  Also, IFTTT only has support for the deprecated Dropbox Public folder, but it seems like Zapier does have decent Dropbox integration.


###Update
I'm at this very moment moving the site over to Pelican, and by the time you read this, it shoudl already be there.  Dropbox also just this week announced that they'll be [supporting webhooks](https://www.dropbox.com/developers/blog/90/announcing-dropbox-webhooks), which will be very exciting for enabling me to simply manage all of my post content out of Dropbox and then have the site regenerated upon any changes.



[pelican]: http://blog.getpelican.com/
[jekyll]: http://jekyllrb.com
[scriptogram]:  http://scriptogr.am
