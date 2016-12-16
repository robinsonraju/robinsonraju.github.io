---
layout: post
title:  "Data De-Duplication Performance With Multi-Threaded FBC Algorithm"
date:   2015-03-01 23:13:21
author:     "Robinson Raju"
categories: Data Compression 
header-img: "img/pres5/nasa_comp.jpg"
---

**Paper reviewed**:

> Jiang, X., Zhao, J., & Zheng, J. (2014). Enhance Data De – Duplication Performance With Multi – Thread Chunking Algorithm. Santa Clara, CA: Santa Clara University.

We've so far reviewed BSW, TTTD and Winnowing algorithms and also reviewed some papers that showed an improvement over TTTD algorithm. 
Through this paper we look at multi-threaded Frequency based Chunking (FBC) method.
FBC makes much improvement in reducing total chunk size and metadata overhead compared to BSW and TTTD but since frequency has to be computed first, it could be slower. 
This paper talks about a multi-threaded FBC that exploits the multicore architecture of the modern microprocessor. 

---
_Header Image - "**Columbia Supercomputer**" by Scott Beale via [Flickr](https://flic.kr/p/H8UJY)_




