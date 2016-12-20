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

### Chapter 1 : Why
> "OO makes code understandable by encapsulating moving parts. FP makes code under‐ standable by minimizing moving parts." ~ Michael Feathers

_This chapter provides a broad overview and shows some examples of the mental shift that the author is teaching us._

* Example 1-1. Word frequencies in Java
* Example 1-2. Word frequencies in Java 8
* Example 1-3. indexOfAny() from Apache Commons StringUtils 
	* The IndexofAny() method accepts a String and an array and returns the index of the first occurrence in the String of any of the characters in the array
* Example 1-4. indexOfAny() example cases
* Example 1-5. Scala version of firstIndexOfAny()
* Example 1-6. Returning a lazy list of matches

### Chapter 2 : Shift
> "Once garbage collection became mainstream, it simultaneously eliminated entire categories of hard-to-debug problems and allowed the runtime to manage a process that is complex and error-prone for developers. Functional programming aims to do the same thing for the algorithms you write, allowing you to work at a higher level of abstraction while freeing the runtime to perform sophisticated optimizations.""

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

_The last part of the chapter is a quick overview of **3 key 'functions'** in functional programming languages - **filter**, **map** and **reduce**. The author shows code in Scala, Groovy and Clojure._

### Chapter 3 : Cede
> "Confession: I never want to work in a non-garbage-collected language again. I paid my dues in languages like C++ for too many years, and I don’t want to surrender the conveniences of modern languages. That’s the story of how software development progresses."

_It's so great to see this comment in the book! I spent close to a year in 2007 and over a year in 2015-2016 to re-engineer C++ applications into Java. Though the projects were for different companies (ebay and paypal), co-incidentally, both applications were related to payments!_

_In this chapter, the author shows five ways developers in functional languages can cede control to the language or runtime, freeing themselves to work on more relevant problems._

1. Iteration to Higher-Order Functions 
2. Closures
3. Currying and Partial Application
	* _Currying_ describes the conversion of a multiargument function into a chain of single-argument functions.
	* _Partial application_ describes the conversion of a multiargument function into one that accepts fewer arguments, with values for the elided arguments supplied in advance.
4. Recursion
5. Streams and Work Reordering

* Example 3-1. Simple closure binding in Groovy
* Example 3-2. Executing the closure block
* Example 3-3. Another closure binding
* Example 3-4. How closures work (in Groovy)
* Example 3-5. makeCounter() in Java
* Example 3-6. Currying in Groovy
* Example 3-7. Partial application versus currying in Groovy
* Example 3-8. Composing functions in Groovy
* Example 3-9. Clojure’s partial application
* Example 3-10. Scala’s currying of arguments
* Example 3-11. Partially applying functions in Scala
* Example 3-12. Using case without match
* Example 3-13. Differences between map and collect
* Example 3-14. Defining a partial function in Scala
* Example 3-15. Alternative definition for answerUnits
* Example 3-16. Defining an incrementer in Scala
* Example 3-17. Adder and incrementer in Groovy
* Example 3-18. Using partial application to supply implicit values
* Example 3-19. List traversal using (sometimes hidden) indexes
* Example 3-20. List traversal using recursion
	* Think of list as head and tail and iterate through it using recursion
* Example 3-21. Imperative filtering with Groovy
	* Accepts a list and a predicate (a Boolean test) to determine if the item belongs in the list.
* Example 3-22. Recursive filtering with Groovy
* Example 3-23. Recursive filtering in Scala
* Example 3-24. Java 8 version of the company process

_A note on Erlang's tail-call optimization._

> Given Erlang’s impressive fault-tolerance capabilities, there are likely tail-recursive loops in production that have run for **years** (!) uninterrupted.


### Chapter 4 : Smarter, Not Harder



