Title: How to use getopts inside a Bash function
Date: 2014-03-18
Slug: how-to-use-getopts-inside-a-bash-function
Category: Programming
Tags: hackerschool, bash, getopts
Status: published

As part of my quest to finish packaging up my Bash function that gets the updated weather in your Bash prompt, I needed to better organize my code, and so started putting some code into functions.  Bash, however, is a fickle language, and the difficulty that quickly arose was using `getops` within a Bash function.

The reason that I wanted to do this is that Bash, in its infinite wisdom, doesn't have regular namespacing.  When you use `source` or `.` on a Bash script and it sets a variable, that variable is now set across your entire environment (e.g., that terminal window).  That's not great to begin with, but given that this script is going to be called every time the prompt is run (meaning, literally every time a command is run), I want to be sure not to clutter up users' global namespace.

Originally, it was working fine when placed straight in the shell script:

    #!/bin/bash
    
	  while getopts ":c:l:u:s:" opt ; do
	      case "$opt" in
	          c  )   # default character to display if no weather, leave empty for none
	              c="$OPTARG"
	              ;;
	          l  )   # supply city name instead of using internet
	              l="$OPTARG"
	              ;;
	          u  )   # how often to update weather in seconds
	              u="$OPTARG"
	              ;;
	          s  )   # weather update alert string to supply, if any
	              s="$OPTARG"
	              ;;
	          h  )
	              # echo the help file
	              ;;
	          \? )
	              echo "Invalid option: -$OPTARG" >&2
	              ;;
	          :  )
	              echo "Option -$OPTARG requires an argument." >&2
	              exit 1
	              ;;
	      esac
	  done 

What this does is it allows you to call my shell script with various parameters, e.g.:

    BashWeather -c "$" -u 30

My first thought to be able to stick it inside a function was to simply pass on the parameters to the function, but you can't really pass arguments to Bash functions, nor can you return values except for `0` or `1` as an exit status code.   In Python, you could just declare a function with arguments like `def myfunc(arg1):`, but in Bash there's no equivalent to that, and `getopts` itself is actually how you'd likely parse any arguments passed in.

Ultimately, that was what I ended up doing, but I had to do it the Bash way, passing it to the function as `"$@"`, referencing the inputs that were passed in by the calling script.  I had a hard time figuring this out, so I thought it would be useful to post this here.

Final output:

	#!/bin/bash
	
	function getOptsFunction {
	  local OPTIND
	  while getopts ":c:l:u:s:" opt ; do
	      case "$opt" in
	          c  )   # default character to display if no weather, leave empty for none
	              c="$OPTARG"
	              ;;
	          l  )   # supply city name instead of using internet
	              l="$OPTARG"
	              ;;
	          u  )   # how often to update weather in seconds
	              u="$OPTARG"
	              ;;
	          s  )   # weather update alert string to supply, if any
	              s="$OPTARG"
	              ;;
	          h  )
	              # echo the help file
	              ;;
	          \? )
	              echo "Invalid option: -$OPTARG" >&2
	              ;;
	          :  )
	              echo "Option -$OPTARG requires an argument." >&2
	              exit 1
	              ;;
	      esac
	  done
	  shift $((OPTIND-1))
	
	  # set defaults if command not supplied
	  if [ -z "$u" ] ; then u=10800 ; fi
	  if [ -z "$c" ] ; then c="$" ; fi
    }
    
    getOptsFunction "$@"
