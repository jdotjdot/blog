Title: Day 2: Algorithms
Date: 2014-02-11
Slug: algorithms
Category: Programming
Tags: quick-union, hackerschool
Status: published

Today, I'm working on the [Princeton Algorithms Coursera Course](https://class.coursera.org/algs4partI-004/lecture). 

Main goal overall for today and the next few days is to focus on making sure I know the basics of algorithms, enough to make up for the fact I didn't formally study Computer Science.

#### Quick-union
I quickly skipped past the first couple of lectures on unions to get to quick-union.  This strategy works with trees of nodes and more efficiently finds if two nodes are connected by finding each node's root and determining if they're the same root.  To connect nodes, you connect their roots.
Unfortunately, it's still a pretty slow strategy, mainly because the trees can get very tall.

#### Weighted quick-union
This strategy is a modification of quick-sort so that the trees don't get too tall.  Basically, when we're connecting a tall tree with a shorter tree, we make sure to put the smaller tree as the child of the bigger tree.  When we're adding a node that's nested in a different tree, we add that node's entire tree as a child of the tree we're moving it to.
By adding path compression, we flatten each tree out.  Not quite sure why we're doing this; professor says it's "because we can."

Some other topics I glossed over today:

 + O-time
 + Stacks
   + This included basic arithmetic expression evaluation, which is basically a small calculator interpreter, which I already did once for a Google Code Jam problem
 + Arrays (These I know well)
 + Queues (Already wrote a [queue](https://github.com/jdotjdot/CouchQueue)--not a pure one, but at least requiring an understanding of theory)
 + Iterators
 
For the rest of the week, I'm planning to finish what's available of the Algorithms course (Elementary Sorts), read chapter 3 of Introduction to Algorithms (data structures), and then try implementing a few data structures in C, finishing by working on some difficult Google Code Jam algorithms problems, before moving onto the next project.
