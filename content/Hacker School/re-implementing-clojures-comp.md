Title: Re-implementing Clojure's comp
Date: 2014-04-22
Slug: re-implementing-clojures-comp
Category: Programming
Tags: hackerschool, python, clojure, comp
Status: published

While working through [Clojure for the Brave and True](http://www.braveclojure.com/functional-programming/), I came across an explanation of Clojure's `comp` function and some basic implementations of versions of `comp` that take only two arguments or three arguments.  The tutorial challenged me to try to completely re-implement `comp` to accept an arbitrary number of function arguments, and that got me thinking that it would be a very good exercise to try in Clojure.

The book had an implentation of the two-argument `comp` that looked something like this;

    :::clojure
    (defn two-comp [f g]
      (fn [& args]
        (f (apply g args))))
       
I worked off of that as a base for a while, but kept running into trouble.  I kept running into rather complicated functions-of-functions that seemed to be returning functions that operated on the input functions, rather than the actual arguments, which was not what we were looking for.  It's a bit hard to wrap your head around this, since it's very meta and we're talking about a function that has functions as arguments and returns a function of functions as its result.

I decided to take a stab at this in Python, my go-to language.

What I came up with ended up looking like this:

    :::python
    def clojure_comp(*args):
        def wrap_function(to_wrap, wrapper):
            def return_function(*inner_args):
                # Here is where we actually call the function
                return wrapper(to_wrap(*inner_args))
            return return_function
            
        return reduce(wrap_function, reversed(args))
        
This ended up working out very nicely, using string maniuplation as a test:

    :::python
    >>> clojure_comp(lambda x: x.upper(), lambda x: x.strip(), lambda x: x.replace('a', 'b'))(" abcdefgh   ")
    'BBCDEFG'
    
So I gave this another shot in Clojure.

    :::clojure
    (defn mycomp [& args]
      "A function that takes an arbitrary number of functions and returns a function that 
      applies each of those functions, last first, to the input arguments."
      (defn wrapper-function [wrapped wrapper]
        (fn [& inner-args] (wrapper (apply wrapped inner-args)))
        )

      (reduce wrapper-function (reverse args))

      )
      
 And it does work--

    :::clojure
    user=> ((mycomp clojure.string/trim clojure.string/lower-case) "   this IS a test   ")
    "this is a test"
    
But ultimately, I think it might be a bit too Pythonic rather than right for Clojure.  I don't tend to see too many functions that declare another named function within themselves, and I also feel like this is the kind of function that might better use recursion or `loop` than `reduce`, which I feel like I'm falling back on as a replacement for Python's convenient `for` iteration.  

That being said, it could still be a valuable way of doing it.  I recently got complimented by a Javascript developer for my use of `reduce` in some Javascript I was writing for the [Sefaria](http://www.sefaria.org) project.  He said `reduce` and `map` were functional elements of JS that even most seasoned Javascript developers don't use, so he was surprised that I was--but to me, languages like Clojure make it seem quite natural to use, and much more elegant in many cases than iteration and mutation.
