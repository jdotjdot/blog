Title: Ultrasonic distance detectors in Arduino
Date: 2014-03-27
Slug: ultrasonic-distance-detectors-in-arduino
Category: Programming
Tags: hackerschool, arduino, ultrasonic, distance
Status: published


<!-- 3/27/2014 -->

Matt at Hacker School has plans to go back home and hook up a Raspberry Pi or an Arduino to a motion sensor in order to detect when his cat jumps onto the table (which apparently happens too much)--and maybe scare him as well, making it make a loud noise every time he does it.

Since I've worked quite a bit with Arduino at this point, between the [wireless remote control car project](https://github.com/jdotjdot/B_FURIOUS) and the [internet-enabled door opener](https://github.com/jdotjdot/doorduino), Matt asked me to walk him through what the code would look like in C.  Up until now, he's been working with Arduinos using a Ruby library (I think [this one](http://ruby-serialport.rubyforge.org/)), but it's fairly limited, and I also would imagine that being another step away from the C would make it harder to program the micro controller.  So we went over what the C code would look like for a very simple use case.

We set up an Arduino to detect the closest item (linearly) using the ultrasonic distance detector, and then to dim a light depending on how far the item was.

Here it is in action:

<iframe align="center" width="560" height="315" src="//www.youtube.com/embed/n7D4ZiQezQI" frameborder="0" allowfullscreen></iframe>
<br>
###Schematic

<div class="center container"><img width="700px" align="center" alt="Schematic" src="https://dl.dropboxusercontent.com/s/o2mjj69763su8rq/Ultrasonic-distance-detector.png"></div>

**The basic setup:**
The ultrasonic distance detector, the big blue thing that isn't the Arduino, is hooked up to the 5V Arduino output and to ground, and then the middle two pins are hooked up to Arduino digital pins--one to trigger an ultrasonic blast, and one to listen for the blast's response.  The red LED hooked up to pin 13 flashes when nothing is detected in the vicinity, and then turns solid red when something is detected.  The yellow LED fades depending on the distance of the detected object--the closer it is, the dimmer the light, unless there are no objects within the specified maximum detection range, in which case the light is completely off.

**How it works:**
The ultrasonic distance detector, when turned on by setting the pin hooked up to the trigger to `HIGH`,  sends out an ultrasonic blast forward.  We have the Arduino wait about 10 microseconds for the sound to emit using `delayMicroseconds(10);`, and then we use `pulseIn` to wait for the sound to return.  The longer it takes the sound to return, the farther away the object is.  To find the number of centimeters away the object is, we can take the response from `pulseIn` and divide it by `(2 * 29)` to get the distance in centimeters rather than milliseconds.

In the case of this Arduino project, we then use that information to determine if the object is within the specified distance range (`iMaxDistance` in the code below), and if so, we turn the red light on and scale the output to a range of 0-255, which is the allowed analog output from the Arduino to the yellow LED using `analogWrite`.

And that's it!


###The Code

    :::arduino
    // Credit to JamesHappy for much of this tester code

    // Onboard LED should blink while searching for surface
    // Onboard LED should be solid when surface is within a specified distance
    // Rangefinder should only wait for echos under a calculated timeout


    int iTrigger     = 2;  // Digital Pin 2
    int iEcho        = 3;  // Digital Pin 3
    int iAlertLED                  = 13; // Digital Pin 13
    int iEchoTimeout = 0;  // In Microseconds
    int iMaxDistance = 30; // In Centimeters

    int iTriggerPullDown = 2;  // In Microseconds
    int iPingWidth       = 10; // In Microseconds

    int changingLed = 9;

    void setup() {
      Serial.begin(9600);
      pinMode(iTrigger,OUTPUT);
      pinMode(iEcho,INPUT);
      pinMode(iAlertLED, OUTPUT);
      pinMode(changingLed, OUTPUT);
      iEchoTimeout = iMaxDistance*2*29;
      digitalWrite(changingLed, HIGH);
    }



    void loop() {
      digitalWrite(iTrigger, LOW);
      delayMicroseconds(iTriggerPullDown);
      digitalWrite(iTrigger, HIGH);
      delayMicroseconds(iPingWidth);
      digitalWrite(iTrigger, LOW);
      unsigned long ulPing = pulseIn(iEcho,HIGH,iEchoTimeout);
      Serial.println((String) (ulPing / 2 / 29));
      if(ulPing) {
        digitalWrite(iAlertLED, HIGH);
    //    digitalWrite(changingLed, ((ulPing/2/29)/iEchoTimeout*255));
        analogWrite(changingLed, map(ulPing, 0, iEchoTimeout, 0, 255));
        SimulateLoad(250);
      }
      else {
        digitalWrite(changingLed, LOW);
        digitalWrite(iAlertLED, HIGH);
        delay(25);
        digitalWrite(iAlertLED, LOW);
        SimulateLoad(225);
      }
    }

    void SimulateLoad(int iDutyCycle) {
      delay(iDutyCycle);
    }
