Title: Days 3-4: More algorithms, CTF, whoops
Date: 2014-02-13
Slug: day-3-more-algorithms
Category: Programming
Tags: hackerschool, algorithms, sort
Status: published

### Algorithms
#### Selection sort
Just going through left to right, finding the new minimum of the unsorted items, and swapping it with the left most unsorted item.

#### Insertion sort
Going from left to right, and moving the leftmost unsorted item one item left at a time until we hit the beginning of the array or an item smaller than the one we're currently moving.

#### Shellsort
Insertion sort, but making jumps of size `h`.
Interesting point that the professor made was that if you *h*-sort an array and then *g*-sort it, it still remains *h*-sorted.  This was not something I had thought of offhand, but it makes perfect sense.

Shellsort is generally pretty fast unless the array size is huge.

### Hacking
I started playing around with a really cool embedded security capture the flag game called [Microcorruption](https://microcorruption.com/login).  "Capture the Flag" games, when referring to computer security, are complex and involved games with series of levels where you have to find the (deliberately placed) vulnerability in the server or website, etc. at each level and find a secret file, codeword, or password hidden there.  Stripe has run a few of these relating to breaking into websites, so I'm very excited about this one, which actually works with breaking into (virtual) hardware to break into pretend warehouses.  Very exciting.

It would shock me if I find myself moving a bit more towards studying hardware and network security while I'm here.

### Blowing up my computer
Whoops.   Accidentally breaking Windows took up the latter half of the day.  Still working on fixing it, even though it's already the next day.  Might have to get a new computer.


