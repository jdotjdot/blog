Title: Getting syntax highlighting on Scriptogr.am (and other hosted static site generators)
Date: 2014-03-26
Slug: getting-syntax-highlighting-on-scriptogr-am-and-other-hosted-static-site-generators
Category: Programming
Tags: hackerschool, scriptogr.am, static-site-generators, syntax-highlighting, highlightjs
Status: published

The benefits of hosted static site generators include crazy ease of use, auto-deployment, hosting, etc.--but on the downside, you're sometimes a bit more limited in the control you have over the site.

When starting out with trying [Scriptogr.am](http://scriptogr.am), I was a bit disappointed by the lack of syntax highlighting.  Pelican uses [Pygments](http://pygments.org), but that runs on the server side in Python--so it's fine for a personally hosted static site generator, but I wouldn't be able to get a hosted solution like Scriptogr.am (or Github Pages, for that matter) to use it.

A solution I found was [HighlightJS](http://highlightjs.org/), which is a Javascript-based code syntax detection and highlighting platform.  This is great, because being Javascript based, I can simply throw a link to the code into my Scriptogram (or whatever else) theme, and let the browser rather than the server (or static site generator) do the work.

I had a bit of difficulty getting it working, so I thought I'd post this here for those of you with the same issue so you can avoid the trouble.

####Step 1: `<head>`
This is easy.  They are nice enough to host a prebuilt version of HighlightJS, so you can simply link to it in your `<head></head>` tag.  At the bottom, paste the following:

	<head>
	<!-- any other html stuff -->
		<link rel="stylesheet" href="http://yandex.st/highlightjs/8.0/styles/default.min.css">
		<script src="http://yandex.st/highlightjs/8.0/highlight.min.js"></script>
	</head>
	
For a different HighlightJS theme for the syntax highlighting, simply change the `href` attribute in the CSS `<link>` to your preferred theme stylesheet.
	
	
####Step 2: Make sure HighlightJS is called last
The javascript you're already loading is supposed to run HighlightJS after the page loads, but that wasn't working for me with Scriptogr.am--I imagine because Scriptogr.am itself probably had some functions that run after the page fully loads that were overriding and coming after what I had specified.

The way to get this working is to add another function to the very bottom of your HTML:

	<!-- above, the rest of your HTML file/theme -->
	<script>(function(){hljs.initHighlighting();})();</script>
	</body>
	</html>
	
####Step 3: Profit
Reload the page, and see if it works!  All of the code in `<pre><code>` blocks should be automatically detected and highlighted.

If you need to make any changes or customization (e.g., your code isn't in `<pre><code>` blocks), see the [HighlightJS usage docs](http://highlightjs.org/usage/), which are very helpful.
