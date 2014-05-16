Title: Day 9: It works!
Date: 2014-02-20
Slug: day-9-victory
Category: Programming
Tags: hackerschool, dial-up-over-cell-phone, android, mel-chua, it-works, productively-lost
Status: published

We had a great talk by Mel Chua not long ago about different types of learning, and [how learning works at Hacker School](http://de.slideshare.net/mchua/edutalk-w2014).   One of the main things she pointed out at the beginning was that learning at Hacker School is very different than the kind of directed learning that you might find in school - all of us are going to spend a fair amount of time being **productively lost**.  

This means that we'll be sitting there hacking away at something, having no idea what we're doing or how it works, feeling very stupid, thinking we're not cut out for this, and then every once in a while, out of nowhere...


###<center>It works!</center>

I had one of those moments today, while working on an extremely basic android app to record a call, as part of my efforts on the Dial-Up Over Cell Phone project.  I knew absolutely no android before this and no Java, so it's been a lot to pick up at once, especially because android development has turned out to be pretty confusing and not that well designed. I was following the official ["Building Your First App"](https://developer.android.com/training/basics/firstapp/index.html) guide, but I was having quite a bit of trouble with it. 

After a while, I managed to get an extremely basic two page (or "activity", in android parlance) app up on an emulator.  Eventually I actually put it on a phone, which felt pretty cool.

First page of the app:
<center><img src="https://dl.dropboxusercontent.com/s/l9m93na1vaiattb/Screenshot_2014-02-20-17-51-15.png" alt="First page of my app" width="50%" height="50%"></center>

And then, after you've written the message:
<center><img src="https://dl.dropboxusercontent.com/s/kdbtub8zh4jdt84/Screenshot_2014-02-20-17-51-27.png" alt="Writing the message" width="50%" height="50%"></center>

Finally, send the message to the second page:
<center><img src="https://dl.dropboxusercontent.com/s/u0isb6mr4fchue5/Screenshot_2014-02-20-17-51-31.png" alt="The message was sent!" width="50%" height="50%"></center>

So that was great, but ultimately, the goal of today was to get an app working where I could press a button to record a sound, and then press another button to play it back.  This is to help get me on my way towards an app where I can actually record the voice downlink of a call, which is the painful but necessary first step for my Dial-Up Over Cell Phone project.

I was having trouble with this all day.  Recording is apparently pretty fraught with bugs in android, and playing back is too. I spent much of the data looking at scary errors like `media server died` or `incorrect format for writing` or completely useless errors like `prepare() failed!`  So I just kept trying different settings, different audio codecs like using `AAC` instead of the default `3GP`, looking at the saved audio file itself to see if maybe audio was getting written but the player just wasn't working, and then I went back to `3GP` and noticed that the filename I was saving as didn't match so fixed that from ending in `.aac` to `.3gp` and then all the sudden

###<center>It worked!</center>

I had my android app on my android phone, pressed the "Audio Page" button to go the audio page, and then pressed the "Record" button to record, recorded a sound, stopped the recording, and then pressed the "Play" button to play it back!

Even though I'm only 80% of the way there in understanding why this particular configuration worked and I need to understand in order to go the rest of the way, it's those moments of "aha!" that make it all worth it.
