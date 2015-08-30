---
layout: post
title:  "Winnowing: local algorithms for document fingerprinting"
date:   2015-02-15 01:23:11
author:     "Robinson Raju"
categories: Data Compression 
header-img: "img/pres3/winnowing.jpg"
---

**Paper reviewed**:

> Schleimer, S., Wilkerson, D. S., and Aiken, A. 2003. Winnowing: local algorithms for document fingerprinting. In Proceedings of the 2003 ACM SIGMOD International Conference on Management of Data (San Diego, California, USA, June 09 – 12, 2003). 

My focus area right now is data chunking alogrithms. I'd jumped right into data chunking using hashing and finger-printing algorithms since those are popular and there are multiple papers on them. 
This week I thought I'd take a step back and review some other techniques. 

Here is a high level overview of different chunking algorithms - 

* Overlap
	* K-gram algorithm 
	* 0 mod p algorithm 
	* **Winnowing algorithm** 

* Non-Overlap 
	* Hash-breaking 

Last paper focused on non-overlap method. This has more information on overlap methods. 
The paper gives an overview of local fingerprinting algorithms. It provides an introduction to Winnowing, a special local fingerprinting algorithm. It goes on to show experimental results for Winnowing's performance being less than 33% of earlier lower bound. 

---
_Header Image - "**Seminole Winnowing Basket**" by Mathers Museum of World Cultures via [Flickr](https://flic.kr/p/pfY1mV)_




