Title: Killing a Python WAT: Forcing immutable default arguments
Date: 2014-04-26
Slug: killing-a-python-wat-forcing-immutable-default-arguments
Category: Programming
Tags: hackerschool, python, wat, decorator, mutability, default-args
Status: published

Fellow Hacker Schooler [Amy](http://mathamy.com/author/amy-hanlon.html) had a great post today on [mutable default arguments in Python][1], a very typical Python "WAT".

(If you haven't seen the [CodeMash 2012 WAT video](https://www.destroyallsoftware.com/talks/wat), you should.)

In this case, Amy wrote about how unintuitively in Python, when creating a function with default arguments, those arguments are actually **mutable** and **preserved**, meaning any mutations made to the default arguments remain that way for all future calls to that function.  We just often don't see this behavior because most of the time numbers and strings are used as default arguments, which *by implementation* are immutable and so aren't given a chance to exhibit this behavior.

The example she used:

    :::python
    def foo(l=[]):
    	l.append('cat')
        return l
        
What happens when you call `foo` repeatedly?  You'd expect `l` to be reinstantiated every time with a new empty list, but instead, you get the following:

    :::python
    >>> foo()
    ['cat']
    >>> foo()
    ['cat', 'cat']
    >>> foo()
    ['cat', 'cat', 'cat']
    
Ultimately, this is because the default argumetns for the `foo` function are stored in `foo.func_defaults`, which contains our empty list in question.  The list is only instantiated once, and since lists are mutable, every time we call `l.append`, we're mutating the actual default for future calls to the function. 

The only reason this doesn't occur when we use number or string defaults is because they're always immutable, so even if we make a change that looks like a mutation, we're really getting a new object.

    :::python
    def new_foo(a=3):
        a += 1
        # we're actually getting a new object 4
        return a

Read the rest of [her post][1] for more on why this is the case.

This got me thinking that it must be possible to write a decorator that would preserve the original default arguments, even in mutable cases.  Basically, what we'd be doing is intercepting Python's reference to `<function>.func_defaults` with our own.

So what would this look like?

###Make the decorator

First, let's get our basic decorator structure out:

    :::python
    def enforce_defaults(function):
        
        def wrapper(*args, **kwargs):
        	return function(*args, **kwargs)
        	
        wrapper.func_name = function.func_name
        	
        return wrapper
        
###Getting our default arguments
        
Next, we'd like to grab the default arguments and variable names from our to-be-decorated function.  We know already we can get the defaults from `function.func_defaults`, and we can grab the variable names from `function.func_code.co_varnames`.  We also will grab the number of arguments for the function from `function.func_code.co_argcount`.

    :::python
    def enforce_defaults(function):
    	varnames = function.func_code.co_varnames
    	defaults = function.func_defaults
        argcount = function.func_code.co_argcount
    
        def wrapper(*args, **kwargs):
        	return function(*args, **kwargs)
        	
        wrapper.func_name = function.func_name
        
        return wrapper

The strategy we're going to use here is to build up a dictionary of all the arguments that we're eventually going to pass to the decorated function.  We can't know ahead of time which arguments will and won't be passed, so we'll start with a dictionary of the default arguments, and replace them with the updated, user-supplied args as we go along.  
        
`function.func_defaults` only returns the defaults to us, though, not a full array we can use to match to the full list of varnames.  For example, for function `bas`:

    :::python
    def baz(a, b, c=[], d=4):
        pass
        
We get the following:

    :::python
    >>> baz.func_code.co_varnames
    ('a', 'b', 'c', 'd')
    >>> baz.func_defaults
    ([], 4)
    
So we'll have to match our `func_defaults` tuple to the end of our `varnames` list, so that we match up our defaults with the right args.  We can do that like this:

    :::python
    >>> varnames = baz.func_code.co_varnames
    >>> defaults = baz.func_defaults
    >>> varnames[-len(defaults):]
    ('c', 'd')
    >>> matched = zip(varnames[-len(defaults):], defaults)
    >>> matched
    [('c', []), ('d', 4)]
    >>> dict(matched)
    {'c': [], 'd': 4}
    
So there we have our initial args dictionary with our default arguments:

    :::python
    def enforce_defaults(function):
    	varnames = function.func_code.co_varnames
    	defaults = function.func_defaults
        argcount = function.func_code.co_argcount

        def wrapper(*args, **kwargs):
        	# "holder" is where we're storing our args
        	holder = dict(zip(varnames[-len(defaults):], defaults))
        	
        	return function(*args, **kwargs)
        	
        wrapper.func_name = function.func_name
        
        return wrapper

###Other variables in the function?
Unfortunately, Python functions are going to store **all** of the function variables in `func_code.co_varnames`, including ones declared in-function.  For example:

    :::python
    def test(a, b=3):
        c = 4

    >>> test.func_code.co_varnames
    ('a', 'b', 'c')
    >>> test.func_defaults
    (3,)
    >>> test.func_code.co_argcount
    2

To deal with that scenario, because the internally declared variables are stuck on at the end, we'll have to make a slight modification to our `holder` variable.  Since we know from `argcount` how many arguments they are, we can go back to `varnames` and simply just chop off any extra appended variables before doing our trick with `[-len(defaults):]`.

    holder = dict(zip(varnames[:argcount][-len(defaults):], defaults))

###Oh no!
Looks like what we've done isn't helping at all!  If we stick a print statement in there to debug, you can see what's happening:

    :::python
    def enforce_defaults(function):
    	varnames = function.func_code.co_varnames
    	defaults = function.func_defaults
        argcount = function.func_code.co_argcount
    
        def wrapper(*args, **kwargs):
        	# "holder" is where we're storing our args
        	holder = dict(zip(varnames[:argcount][-len(defaults):], defaults))
        	
        	print holder
        	
        	return function(*args, **kwargs)
        	
        wrapper.func_name = function.func_name
        
        return wrapper

 	@enforce_defaults
 	def foo(l=[]):
 		l.append('cat')
 		return l
 		
 	# >>> foo()
 	# {'l': []}
 	# ['cat']
 	# >>> foo()
 	# {'l': ['cat']}
 	# ['cat', 'cat']
 	
And after all that work!  Why is this happening to us?

Right now, we're accessing our defaults for `holder` from the `defaults` variable, but that's actually just a direct reference to the original `function.func_defaults`, and so we're just mutating the originals like before.  In short, **we haven't actually changed anything.**

We can make sure we're always getting **new** args rather than our old mutating ones by using `copy.deepcopy`.

    :::python
	def enforce_defaults(function):
	  import copy
	  varnames = function.func_code.co_varnames
	  defaults = function.func_defaults
      argcount = function.func_code.co_argcount
	  
	  def wrapper(*args, **kwargs):
	    inner_defaults = copy.deepcopy(defaults)
	    holder = dict(zip(varnames[:argcount][-len(inner_defaults):], inner_defaults))
	    
	    print holder # for debugging
	
	    return function(**holder)
	
	  wrapper.func_name = function.func_name
	
	  return wrapper

Now, we should be good to go:

    :::python
 	# >>> foo()
 	# {'l': []}
 	# ['cat']
 	# >>> foo()
 	# {'l': []}
 	# ['cat']
 	
Excellent!  We've solved our mutating default arguments problem.  Now, we just have to finish the decorator.

###Accounting for user-supplied args
We'll need to read in both `*args` and `**kwargs` and update our `holder` dictionary accordingly, to make sure if the user has supplied any updated arguments over our defaults, we don't continue passing the defaults.

For `**kwargs`, it's pretty easy; we simply update the dictionary:

    :::python
    holder.update(kwargs)
    
Since `*args` is ordered, we can simply use `zip` with the function's argument names, similarly to how we did above:

    :::python
    holder.update(dict(zip(varnames, args)))
    
And then, we just have to update our calling of `function`, since we're only using our specially curated dictionary:

    :::python
    return function(**holder)
   
...and voilà! We're done!  You can now use mutable objects in functions with our decorator without fear!

As final proof:

    :::python
	@enforce_defaults
    def foo(l=[]):
    	l.append('cat')
        return l
        
    >>> foo()
    ['cat']
    >>> foo()
    ['cat']
    >>> foo()
    ['cat']
    
...and you could just do that all day.

###Final code

    :::python
	def enforce_defaults(function):
	  import copy
	  varnames = function.func_code.co_varnames
	  defaults = function.func_defaults
      argcount = function.func_code.co_argcount
	  
	  def wrapper(*args, **kwargs):
	    inner_defaults = copy.deepcopy(defaults)
	    holder = dict(zip(varnames[:argcount][-len(inner_defaults):], inner_defaults))
	    holder.update(dict(zip(varnames, args)))
	    holder.update(kwargs)
	
	    return function(**holder)
	
	  wrapper.func_name = function.func_name
	
	  return wrapper
    

    
[1]: http://mathamy.com/python-wats-mutable-default-arguments.html)

