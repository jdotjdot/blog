Title: Introduction to HTML5 canvas
Date: 2014-04-02
Slug: introduction-to-html5-canvas
Category: Programming
Tags: hackerschool, pacman, canvas, html5
Status: published

<!-- 4/2/2014 -->
<!-- Custom CSS: -->
<style type="text/css">
	blockquote p {
    	font-style: normal;
    }
</style>

In my quest to learn a bit more about front-end and responsive design, I've decided to do a mini-project building a Pacman map-editor in the browser.   Hopefully, I'll also be able to make it playable.  This was inspired by a conversation with [Mary](https://github.com/maryrosecook) about what I should be working on next, in which she told me about someone in a previous batch who had built multiplayer Pacman, where live players controlled the ghosts as well as Pacman.

After doing a bit of research on some larger library options like AngularJS, I decided on simply using HTML5's `<canvas>` element.  While I may eventually use a canvas library like KineticJS, I decided to start off learning the built-in basics, using [this great tutorial](http://diveintohtml5.info/canvas.html) from **Dive Into HTML5**.

####Canvas is just a place for pixels to dance

Canvas is best just thought of as a defined element in the webpage where you draw and erase pixels.  That's it.  

Even if you have very complex Javascript frameworks and architecture going on in the background, at the end of the day, all that `<canvas>` ever sees is various instructions to turn a certain pixel a certain color, with no knowledge of what's going on above.  It's much like your monitor--your monitor displays to you everything happening in your computer display, but the monitor doesn't actually understand where one window ends and another begins, or even what a "window" is--that's all in the computer, which tells the monitor every 16ms or so what color to make each pixel.

####Canvas just needs to be told what to do
Working with `canvas` (without any external Javascript libraries on top) is quite different than working with straight HTML--you have to specifically instruct what you want canvas to do.

To describe the difference a bit better to the uninitiated, HTML could be described as "declarative" programming, meaning you describe what you want and how you want it to be.

> **Declarative programming:**<br>
> Let there be light! <br><br>
> ...*and there was light.*

Notice how above, all I did was say that I wanted there to be light--I didn't specify how it would happen.  It "just works."

In imperative programming, you're getting much deeper into the grimy details of telling the computer exactly what to do.

> **Imperative programming:**<br>
> Every nanosecond, create another photon over there and have each one immediately come over here at the speed of light!<br><br>
>*...and there was light.*

Though oversimplified, this is somewhat the difference between working with HTML in general and working with `<canvas>`.

>**HTML** (declarative)**:**<br><br>
> Code: <br>
>`<div style="background-color: red; width: 100px; height: 100px;"></div>`
> <br><br>
>Translation:<br>
>Let there be a red `div` element with dimensions 100 pixels by 100 pixels!
><br><br>
>What happens:
><div style="background-color: red; width: 100px; height: 100px;"></div>

Compare this to what you do to get the same thing in `canvas`:

>**Canvas** (imperative)**:**<br><br>
>Code:
>
>     // This code is in Javascript
>     var ctx = document.getElementById("myCanvas").getContext("2d");
    function manualrect(x,y,w,h) {
        ctx.beginPath();
        ctx.moveTo(x, y);
        ctx.lineTo(x + w, y);
        ctx.lineTo(x + w, y + h);
        ctx.lineTo(x, y + h);
        ctx.lineTo(x, y);
        ctx.closePath();
        ctx.fillStyle = "red";
        ctx.fill();
    }
>     manualrect(0, 0, 100, 100);
>
>     /* There are built-in functions that make making a rectangle easier, like ctx.rect(x, y, height, width) to create one or ctx.fillRect(...) to create a rectangle and fill it.  However, both ultimately boil down to the code we've used above. */
>
>Translation:<br>
>Browser, go get the element on my webpage with the id `myCanvas`.  Now, in that element, I want you to start creating a path--use your invisible erasable  pencil to ghost out the path.  Start at coordinates `(0, 0)`.  With the pencil to the page, move to `(100, 0)`.  Still with the pencil to the page, move to `(100, 100)`.  [etc.] Now, pencil to the page, move back to `(0, 0)`.<br>
Now, take all those invisible paths we've drawn, and close it to make it a closed shape.
Prepare to use the color "red" to fill in anything we might fill in in the future.
Fill in the last thing we did with the current style (red).
><br><br>
>What happens:

><canvas id="myCanvas" width=110 height=110></canvas>
<script type="text/javascript">
    var ctx = document.getElementById("myCanvas").getContext("2d");
    function manualrect(x,y,w,h) {
        ctx.beginPath();
        ctx.moveTo(x, y);
        ctx.lineTo(x + w, y);
        ctx.lineTo(x + w, y + h);
        ctx.lineTo(x, y + h);
        ctx.lineTo(x, y);
        ctx.closePath();
        ctx.fillStyle = "red";
        ctx.fill();
    }
    manualrect(0, 0, 100, 100);
</script>


We end up in the same place, but it takes a bit more work and explicit instruction to get there.

So, why would we do this?  For a single, unchanging element `canvas` isn't necessarily the better move, but given how it acts like a mini-monitor, it becomes a great way to deal with highly complex visual output and user interaction.
Even more importantly, before `canvas`, drawing a diagonal line meant stacking a bunch of block-like html elements on a page diagonally and coloring them all your color--very complex, and we were essentially creating a giant set of building block/pixles--creating our own `canvas`es.
Now, with `canvas`, we just tell canvas which pixels to color or to draw a diagonal line from here to there, and it does it--no building blocks required.

Also, [some pretty amazing stuff](https://developer.mozilla.org/en-US/demos/detail/zen-photon-garden/launch) can be made with `canvas`.
