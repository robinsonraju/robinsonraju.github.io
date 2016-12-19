---
layout: post
title:  "Functional Thinking"
date:   2016-10-16 09:27:14
description: Neal Ford
categories: books
header-img: ""
---

_For someone who has been doing Java programming and reading through lot of OO codebase over a decade, functional programming is truly a paradigm shift. It is not like learning a different language or different version of Java from Java 2 (1.2) to Java 8. The first time I was exposed to functional programming is probably around 2012 when I had to do a project for an ML course using R language. It was refreshing to do things differently for sure. Thanks to [RV](http://rovarghe.blogspot.com), I learnt the basics of Clojure last year. I'm at a stage where I can read Clojure code and understand and may be write very simple programs but not beyond that. Anyway, the paradigm shift that Ford talks about can be summarized in the example that he gives in the first chapter of the book._

> Let’s say for a moment that you are a lumberjack. You have the best axe in the forest, which makes you the most productive lumberjack in the camp. Then one day someone shows up and extols the virtues of a new tree-cutting paradigm, the chainsaw. The sales guy is persuasive, so you buy a chainsaw, but you don’t know how it works. Demon‐ strating your expertise with the previous tree-cutting paradigm, you swing it vigorously at a tree—without cranking it. You quickly conclude that this newfangled chainsaw is a fad, and you return to your axe. Then, someone appears and shows you how to crank the chainsaw.

_The best thing about the book is that he gives a lot of code examples. So one needs to just think of how to solve these examples and get the gist of what is being talked about._

### Chapter 1	: Why
> "OO makes code understandable by encapsulating moving parts. FP makes code under‐ standable by minimizing moving parts."
> ~ Michael Feathers

_This chapter provides a broad overview and shows some examples of the mental shift that the author is teaching us._

* Example 1-1. Word frequencies in Java
* Example 1-2. Word frequencies in Java 8
* Example 1-3. indexOfAny() from Apache Commons StringUtils 
	* The IndexofAny() method accepts a String and an array and returns the index of the first occurrence in the String of any of the characters in the array
* Example 1-4. indexOfAny() example cases
* Example 1-5. Scala version of firstIndexOfAny()
* Example 1-6. Returning a lazy list of matches

### Chapter 2	: Shift
> Once garbage collection became mainstream, it simultaneously eliminated entire categories of hard-to-debug problems and allowed the runtime to manage a process that is complex and error-prone for developers. Functional programming aims to do the same thing for the algorithms you write, allowing you to work at a higher level of abstraction while freeing the runtime to perform sophisticated optimizations.

* Example 2-1. Typical company process (in Java)
	*  Let’s say that you are given a list of names, some of which consist of a single character, and you are asked to return a comma-delimited string with the single letter names removed, with each name capitalized. 
* Example 2-2. Pseudocode for the “company process”
* Example 2-3. Processing functionally in Scala
* Example 2-4. Java 8 version of the Company Process
* Example 2-5. Processing in Groovy
* Example 2-6. Processing in Clojure
	* _"One of Clojure’s selling points is that it removes concurrency as a developer concern just as Java removed garbage collection."_
* Example 2-7. Improved readability for Clojure via the thread-last macro
* Example 2-8. Scala processing in parallel
* Example 2-9. Java 8 parallel processing
* Example 2-10. Number classifier in Java
	* Perfect : Sum of factors = number
	* Abundant : Sum of factors > number
	* Deficient : Sum of factors < number
	* _Consider aliquotSum where sum of factors doesn't contain the number itself._
* Example 2-11. Slightly more functional number classifier
* Example 2-12. Number classifier in Java 8
* Example 2-13. Number classifier using the Functional Java framework
* Example 2-14. Filtering in Java 8
* Example 2-15. Using filtering (called findAll()) in Groovy
* Example 2-16. Number classifier optimized
* Example 2-17. Groovy optimized factors
* Example 2-18. The (classify ) function in Clojure encapsulates all the behavior within assignments
* Example 2-19. The foldLeft() method from Functional Java
* Example 2-20. foldLeft() with user-supplied criteria

### Chapter 3	: Cede
> One of the values of functional thinking is the ability to cede control of low-level details (such as garbage collection) to the runtime, eliminating a swath of bugs you must chase.




