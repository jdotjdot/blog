Title: How to get Facebook Chat on OS X Messages
Date: 2014-03-04
Slug: how-to-get-facebook-chat-on-os-x-messages
Category: Programming
Tags: jabber, os-x, messages-app
Status: published

I use Facebook Messenger to talk to many of my friends, but I find it really annoying when I'm using the internet and working on other things as well to have to switch between the current window or tab and Facebook to be able to respond to anyone.  It becomes much more of a distraction because it forces me to block much more of the screen than I'd otherwise have to, since I'm switching to an entire browser pane of Facebook, and resizing an individual lone tab simply for Facebook Chat doesn't really work, given what happens to Facebook pages when you resize.

So, I was pleased to discover that Facebook Chat just operates on Jabber, meaning that you can add it as an account to the OS X Messages client.

Here are instructions for doing so:

1.  Open up the Messages app; looks like the following:<br>![Messenger App](http://snag.gy/N3aw0.jpg)
2.  Go to the Accounts tab, and then add a new account by clicking the `+` sign near the bottom left.
3.  Select "Other messages account..."
4.  Under "Account Type", select "Jabber".  Then, for "Account Name", write your Facebook ID (this is the ID that follows `https://www.facebook.com/` when you go to your Facebook page) followed by "@chat.facebook.com".  For example, Obama would put "barackobama@chat.facebook.com", because if you go to [his Facebook page](https://www.facebook.com/barackobama), you'll see in the URL bar that "barackobama" is his account ID.
5.  Put your Facebook password as your password.  If you're using 2-factor authentication (which you should be), after submitting, you'll get a text/notification with a 6-digit numerical code for you to use instead, which you should then use as the password instead. 
6.  For "Server", write "chat.facebook.com".<br>
![Messages app settings](http://snag.gy/kFuco.jpg)
7.  You can leave everything else unchecked, and just press "Create"--and you're good to go!  You'll see your Facebook friends and chats alongside your iMessages and any other accounts you have on the Messages app.  Note that anything you send through the Messages app can still be seen in your Facebook windows, and anything sent to you on Facebook while logged in via Messages will show up in your computer, but if you send a Facebook message from another device, it will be updated on Facebook only and **not** on the Messages app.

This method can be used to enable Facebook chat on basically any other Jabber client, as well.
