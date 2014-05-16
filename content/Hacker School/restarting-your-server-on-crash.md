Title: Automatically restarting your process or server on crash
Date: 2014-04-10
Slug: restarting-your-server-on-crash
Category: Programming
Tags: hackerschool, bash, doorbot, doorduino, server, crash, restart
Status: published

While working with [Robert](http://github.com/lord) on the [Doorbot](http://github.com/lord/doorbot) webserver as part of our project to hook up the front door of Hacker School to the web, we ran across a small problem with the Ruby server that he had set up.

In the past, my sites have always been hosted places like Heroku or [Webfaction](http://www.webfaction.com?affiliate=thecampusrep), which take care of restarting the server in case of shutdown.

However, we were hosting the Doorbot server on a Raspberry Pi that we were planning to lock in the network closet.   This meant that no one was going to be able to get in there to physically unplug and replug the Pi, which is the method we'd been using to restart the server after we (with great difficulty) got the server launch script into Raspbian's `init.d` to start on startup.  Another method we'd also been using was to SSH into the Pi to manually restart the server, but this of course wasn't a sustainable long-term solution.  If the server shut down on its own, people weren't going to be able to get through the door until someone alerted us and we restarted the server manually.   **We needed a better solution that would automatically and reliably restart the server upon shutdown without any human intervention.**

I suggested a strategy that I presented at a [lecture](https://github.com/jdotjdot/Data-Scraping-Talk--PennApps-F2012-) at [PennApps](http://pennapps.com) Fall 2012.   I had previously used this strategy on some web scraping projects to get a running Python process to restart immediately upon shutdown.  For processes like that scraper or the Ruby server, if the process dies with an error, we actually don't generally care in this case why it shut down or what the error was--just that it shut down and that we want it back up immediately.  

The strategy is to **wrap the server set-up process in a Bash script** within a `while` or `until` loop, as in the following example with my old Python scraper:

    :::bash
    # Runs our scraper indefinitely
    # will only stop upon a GRACEFUL exit--
    #  but keep in mind a graceful exit only means that
    #  no error is thrown, but that doesn't mean that we
    #  actually want the program to end!

    until python scraper.py; do
        echo "Process crashed with exit code $?.  Respawning..." >&2
        sleep 2
    done
    
For a server, you would replace `python scraper.py` with `python manage.py runserver` for Django, or the equivalent command in Ruby or your preferred web framework.

What happens here is the `until` loop starts to test the "condition," but the condition here is actually our intended process.  That process runs indefinitely, and ideally would never stop and we'd never hit the `echo`.  However, in the event that the server *does* crash, we take advantage of a trick with Bash--an exit upon failure will evalute "false-y" for the `until` loop, and so on a crash, we will always enter and repeat the loop.  The only way to exit the loop is a successful server program exit, which will never happen, because we never intentionally shut down the server!

After wrapping the Ruby server startup call in that tiny Bash script, the server now automatically restarts itself upon failure.
