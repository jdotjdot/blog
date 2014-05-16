Title: Week 2: Dial-up over cell phone
Date: 2014-02-20
Slug: dial-up-over-cell-phone
Category: Programming
Tags: hackerschool, dial-up-over-cell-phone, tcp, internet, framing, signal-processing, error-correction, compression
Status: published

This week, I decided on and started on what will be my first project for a bit, assuming everything works out:

###Internet over cell phone

The thought behind this is that in the US, we used to have unlimited data plans and limited voice plans, but now things have switched and the carriers mostly force everyone into limited data but unlimited voice plans. 

I think it would be really cool if you could use your **voice minutes** to access the internet instead of your data connection, essentially transmitting arbitrary data from the internet over an analogue connection--the same way was done with dial-up modems or fax.

The difference here, though, is that we'd be using cellular connections, which are a lot more likely to be lossy and/or drop calls than the landlines that used to be used for this kind of thing.

---
####Getting Started

I got started with all of this yesterday, and by speaking to quite a few people, I was assisted in boiling the overall project down into a basic stack that should cover all elements of what would be necessary for this technology, from the highest-level to the lowest-level layer:

1. **Compression**
This would be taking the data pulled from the internet (a web page, a picture, whatever) and compressing it so that I have physically less data to send.  There are many compression algorithms already available, many of which can slice up the data into smaller chunks to be sent out separately like I will have to do, so I will use a library that's already built.  `LZMA` was recommended to me as a good compression algorithm.
2. **Transport protocol**
This is one of the major pieces of this technology that I'm going to have to design and implement effectively from scratch.  Somehow, I need a way for the sending server to decide how to bundle up the different packets of compressed information and send them one at a time (or more than one at at time) similar to how it's done currently on the internet.
It's kind of like the way it was sending letters by mail before telephone and internet - the sender would send a letter and would have no way of knowing if the intended recipient received it unless he sent a letter back, as well.  Current internet protocols (like TCP) have this built in in what is called a ["three-way handshake"](http://www.inetdaemon.com/tutorials/internet/tcp/3-way_handshake.shtml) so that the two computers know that they are both sending and receiving.
Super-summarized, if we continued with the letter-sending comparison, it's something along these lines:
   + Bob sends a letter to Alice, saying "Hey!  Did you receive this letter?"
      + This is called the **SYN** packet, since Bob('s server) is asking to **synchronize** with Alice
   + Alice, if she receives the letter, sends one back to Bob, saying "Yup, got yours!  Are you getting this one?"
      + This is called the **SYN-ACK** packet, because Alice is **acknowledging** Bob's letter and also asking to **synchronize** with him.
   + Finally, Bob receives Alice's letter and sends one back saying "Yup, got yours too!  We're in business."
      + This final packet in the handshake is called the **ACK** packet, because it's just an **acknowledgement**.
      
    I'm basically going to have to do the equivalent of this using tones over a cell phone line.

3. **Framing**
In this layer, I will take the data that the user requested from the internet, and chop it up into little pieces that can be sent individually so that I don't have to send it all at once.
This is necessary because it would be too difficult to send all the requested data all at once in one giant package.  One way you could think about it is to compare it to if you had to send the entirety of Harry Potter to someone by mail, and you could only use normal envelopes, because sending by box was too expensive.  Stuffing it all in one envelope isn't really practical and could easily get messed up, plus if it gets lost, you've lost everything.   What you would do is but the books up into a bunch of different pieces, stuff them all into separate envelopes, and then send those all out to reach the requester.
However, since they may all arrive at different times, you'll probably want to number the enveleopes to make sure that the requester (a) knows the order that they should get put back together in and (b) can tell if any of the envelopes didn't make it all the way through, so they can request them from you again.
It's obviously more complex than that, but those are the basics behind the transport protocol--the system of deciding how much to put in each envelope, the numbering of the envelope, and sending, receiving, and acknowledgement of the envelope is all part of framing and the protocol.

4. **Error-correcting Code**
Hamming code or Golay

5. **Symbol modulation**
QAM or PSK

6. **Audio**
4- or 8-bit harmonics


*(To be completed...)*
