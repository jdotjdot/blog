Title: Asynchronous programming with Arduino
Date: 2014-03-11
Slug: asynchronous-programming-with-spark-core
Category: Programming
Tags: C, async
Status: published

I've been working quite a bit this week and last week with [Arduinos](http://www.arduino.cc/) and [Spark Cores](https://www.spark.io/) (an Arduino-like device with WiFi and a cloud service built-in).   I've been working on a few projects, including many out of the Arduino starter book, hooking up a remote control car to WiFi, and hooking up the Hacker School door buzzer to our WiFi so that we can let people in  without pressing the door buzzer--or so that people can let themselves in.

One of the issues I've run across that's been interesting is how to run threaded or asynchronous commands.  This is important if we want the Arduino to do something, but we also need a time delay.  For example, if someone sends a command to the Arduino to open the door, we need to do the following two things:

1. Open the door, wait 10 seconds, close the door
2. Respond to the request and close the connection--e.g. with a `HTTP 200 OK` or something similar.

The way my code was structured, I was sending the command to the door before responding to the client.  The problem is that the Arduino is running a single set of instructions, so the response to the client is delayed by waiting for the door to close.  For example, the steps occured in the following order:

1. Arduino server recieves request to open the door
2. Arduino opens door
3. Arduino sits and waits for 10 seconds
4. Arduino closes door
5. *Then*, Arduino sends response message

The client is then sitting there and waiting for 10 seconds to know what happened.  I didn't want to have this happen, so there had to be a better way to do it--and I realized I could take advantage of the Arduino's built-in looping structure.

###First, some background
The Arduino requires its code to be set up in a specific manner, with two specific functions that it will always run.

    :::arduino
    void setup() {
       // This function is called once upon start-up
       //  to do any set-up required--e.g., initalizing
       //  intput and output pins
    }
    
    void loop() {
       /* This function is called over and over again, many 
       times per second.
       
       However, it only runs once at a time, so if you have a "delay" command in there, all activity will cease until the delay is over.
       */
    }

###What I did
I took advantage of how frequently `loop()` is called.  I set up a block at the top of `loop()` (or alternatively could be a different function that is called at the top of `loop()`) that would run the open door command when a state variable, declared at the beginning, was set to `true`, and then immediately turn it to false.  
Rather than open the door immediately upon receiving the request, the Arduino would set this "openDoor" variable to `true` and would immediately respond to the client.  The next time the program looped around, it would see that `openDoor` says that the door needs to be open it--and so it would open it and have the delay, but it would do all this after the client had been responded to.

Overall, the code looked something like this:

    :::arduino
    boolean asyncOpenDoor = false;
    
    void openDoor() {
        // code to open the door
        // below is pseudocode
        
        asyncOpenDoor = false; // so door isn't opened again
        
        openTheDoor();
        delay(15000); // delay for 15 seconds
        closeTheDoor();
        
    }
    
    void setup() {
        pinMode(doorOpener, OUTPUT);
        
        // code to set up the server
    }
    
    void loop() {
    
       if (asyncOpenDoor) {
          openDoor();
       }
       
       // Code to receive incoming requests
       
       if (requestSaysToOpenTheDoor) {
          // Valid door-opening request
       
          asyncOpenDoor = true;
          
          // respond to client
          client.println("HTTP 200 OK");
       } else {
          // invalid door-opening request
          
          // respond to client
          client.println("HTTP 401 Unauthorized");
       }

       // kill the connection
       client.stop();
       client.flush();
    
    }
