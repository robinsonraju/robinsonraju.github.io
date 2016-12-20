---
layout: post
title:  "Introduction to Data Mining"
date:   2014-02-16 18:17:11
description: Pang-Ning Tan, Michael Steinbach, Vipin Kumar
categories: books
header-img: ""
---

**"Introduction to Data Mining"** by Pang-Ning Tan, Michael Steinbach and Vipin Kumar has been recommended to me as a great book to learn about Data Mining. Read the first chapter and it felt very inspiring as though it was beckoning me to keep at it and read more.

Thought I will capture notes as I read. The way I usually capture notes is to make a list of all the headings, go over them once I finish a chapter or at a later time. Brain just needs a key to fetch information. The headings serve as good keys.

The best thing about the book is that sample chapters and lecture notes (ppt) are available on the publisher's website. 

* **Main Page** : [http://www-users.cs.umn.edu/~kumar/dmbook/index.php](http://www-users.cs.umn.edu/~kumar/dmbook/index.php)
* **Power Point slides** : [http://www-users.cs.umn.edu/~kumar/dmbook/index.php#item4](http://www-users.cs.umn.edu/~kumar/dmbook/index.php#item4)
* **Sample Chapters** : [http://www-users.cs.umn.edu/~kumar/dmbook/index.php#item2](http://www-users.cs.umn.edu/~kumar/dmbook/index.php#item2) 

-----

### Chapter 1 - Introduction
**Data Mining** : Non-trivial extraction of implicit, previously unknown and potentially useful information from data. Exploration & analysis, by automatic or semi-automatic means, of large quantities of data in order to discover meaningful patterns. 

* 1 Introduction
	* Fields - business, medicine, science & engineering
	* 1.1 What is Data Mining
		* Different from Information Retrieval
		* Integral part of KDD(Knowledge discovery in databases) 
	* 1.2 Motivating Challenges
		* Scalability, High Dimensionality, Heterogenous and complex data, Data Ownership and distribution, Non-traditional analysis
	* 1.3 The Origins of Data Mining
		* Relates to fields of Statistics, AI, Machine Learning & Pattern Recognition
		* Built on Database technology, Parallel Computing, Distributed computing
	* 1.4 Data Mining Tasks
		* Predictive tasks, Descriptive tasks
		* Predictive modeling - classification (discrete target variables), regression ( continuous target variables)
		* Association analysis 
		* Cluster analysis
		* Anomaly detection 
	* 1.5 Scope and Organizations of the Book

Ref : Introduction to Data Mining - Chapter 1. 

[http://www-users.cs.umn.edu/~kumar/dmbook/dmslides/chap1_intro.pdf](http://www-users.cs.umn.edu/~kumar/dmbook/dmslides/chap1_intro.pdf)

### Chapter 2 - Data
Data is a collection of objects and their attributes. An attribute is a property or characteristic of an object. A collection of attributes describe an object. 

* 2 Data
	* 2.1. Types of data
		* 2.1.1. attributes & measurement
			* operations used to describe attributes - distinctness, order, addition, multiplication
			* 4 types of attributes - nominal, ordinal, interval, ratio
			* Nominal and Ordinal are Categorical (Qualitative) 
			* Interval and Ratio are Numeric (Quantitative)
				* Nominal (ids, zip codes) -> distinctness
				* Ordinal (rankings, grades) -> distinctness + order
				* Interval (dates, temp in C) -> distinctness + order + addition
				* Ratio (temp in K, length, time) -> distinctness + order + addition + multiplication
				* attribute categorization by values -> discrete, continuous 
		* 2.1.2. Types of data sets
			* Characteristics of data sets -> dimensionality, sparsity, resolution 
			* Types -> record, graph, ordered
				* Record data : a. record data, b. transaction data, c. data matrix, d. document-term matrix
				* Graph based data : a. data with relationship among objects (www), b. data with objects that are graphs (molecular structure) 
				* Ordered data : a. sequential data (timestamps), b. sequence data (genetic code), c. time series data, d. spatial data
	* 2.2. Data Quality
		* 2.2.1. Measurement and data quality issues
			* Noise & artifacts -> precision (std deviation), bias (mean-actual), accuracy (closeness to true value) 
			* Outliers
			* Missing values -> how to solve : eliminate data objects, eliminate missing value attributes, ignore missing value during analysis
			* Inconsistent values
			* Duplicate data
		* 2.2.2. Issues related to applications
			* timeliness, relevance, knowledge about the data

	* 2.3. Data Preprocessing
		* 2.3.1. Aggregation 
			* Purpose : data reduction (smaller dataset means lesser memory), change of scale, more 'stable' data
		* 2.3.2. Sampling
			* Processing all records is very expensive. but sampling needs to be representative
			* Sampling approaches : 
				* Simple random sampling
				* Sampling without replacement
				* Sampling with replacement
				* Stratified sampling
				* Progressive sampling
		* 2.3.3. Dimensionality reduction 
			* Curse of dimensionality (COD)
			* Purpose : avoid COD, reduce processing time, better visualization, reduce noise
			* Techniques : PCA (Principal Components Analysis), SVD (Singular Value Decomposition) 
		* 2.3.4. Feature subset reduction
			* Remove redundant features, irrelevant features
			* Techniques : brute force, embedded, filter, wrapper
		* 2.3.5. Feature Creation
			* Create new attributes from existing
			* Methods : feature extraction, mapping data to new space (Fourier transformation, wavelet trans'n), feature construction 
		* 2.3.6. Discretization & Binarization 
			* discretization, binarization, discretization of continuous attributes
			* Unsupervised discretization (no class labels) : equal width, equal frequency -> K-means
			* Supervised discretization (using class labels) : entropy
		* 2.3.7. Variable Transformation
			* Simple functions, normalization

	* 2.4. Measures of Similarity & Dissimilarity
		* 2.4.1. Basics 
			* definitions - similarity, dissimilarity
			* transformations -> e.g s' = (s - min_s) / (max_s - min_s) 
		* 2.4.2. S & D b/w simple attributes
			* nominal : d = 0 or 1 if x = y or x != y ; s = 1 or 0 
			* ordinal : 
				$d = |x - y| / (n-1) ; s = 1 - d$   
			* interval or ratio : 
				$ d = |x - y| ; s = -d, s = 1/(1+d) $
		* 2.4.3. Dissimilarities b/w data objects
			* Distances
				* Euclidean distance : 
					$f(x) = \sqrt{\sum_{k=1}^n (x_k - y_k)^2}$
				* Minkowski distance (Generalization) : 
					$f(x) = (\sum_{k=1}^n (x_k - y_k)^r) ^ {1/r} $
					* Hamming distance (city blocks) : r = 1
					* Euclidean distance : r = 2
					* Supremum distance : r = 
						$ \infty $
			* Common properties : a. Positivity, b. Symmetry, c. Triangle inequality
			* 'metric' satisfies all common properties
		* 2.4.4 Similarities b/w data objects
			* typical properties
			* s(x, y) = 1 only if x = y [max similarity]
		* 2.4.5 Examples of proximity measures
			* Similarity co-efficients
				* Simple Matching : 
					$ SMC =  (f_11 + f_00) / (f_01 + f_10 + f_11 + f_00) $
				* Jaccard : 
					$ JC =  f_11 / (f_01 + f_10 + f_11 + f_00) $ 
				* Cosine : 
					$ cos(x, y) = $ x.y / ||x||.||y|| $
					* x.y is the vector dot product = 
						$ \sum_{k=1}^n (x_k y_k) $
					* x.y is the vector dot product = 
						$ \sum_{k=1}^n (x_k y_k) $
					* ||x|| = 
						$ \sqrt{x.x}$
				* Extended Jaccard : 
					$ EJ =  x.y / (||x||^2 + ||y||^2 - x.y) $ 
				* Correlation : $ P_k $ -> Pearson's Correlation
					* 
					$ P_k (x, y) = covariance (x, y) / SD(x) . SD(y) $
				* 
					$ covariance(x, y) = 1 / (n-1)  \sum_{k=1}^n(x_k - \bar{x}) (y_k - \bar{x}) $
				* 
					$ = 1/n \sum_{k=1}^n(x_k)$
				* 
					$ \bar{x} = $ mean of x $ = 1/n \sum_{k=1}^n(x_k)$
				* 
					$ \bar{y} = $ mean of y
				* 
					$ SD(x) = Standard deviation = \sqrt{1 / (n-1)  \sum_{k=1}^n(x_k - \bar{x})^2 } $
				* Bregman divergence
					* 
						$ D(x, y) = \phi{(x)} - \phi{(y)} - \langle \nabla \phi{(y)}, (x - y) \rangle $
					* 
						$ D(x, y) = \phi{(x)} - \phi{(y)} - \langle \nabla \phi{(y)}, (x - y) \rangle $

		* 2.4.6 Issues in Proximity calculation
			* a. different scales, b. different attributes, c. different weights
			* Standardization 
				* 
				$ mahalanobis(x, y) = (x - y) \sum_{}^{-1}(x-y)^T $
			* Combining Similarities
				* 
				$ Similarity(x, y) = \sum_{k=1}^n w_k \delta_k s_k(x, y)  / \sum_{k=1}^n \delta_k $
		* 2.4.7 Selecting the right proximity measure
			* Type of proximity should fit type of data
			* Use Euclidean distance for dense continuous data
			* Usually expressed as differences
			* Sparse data -> ignore 0-0 matches -> use Jaccard, cosine, Extended Jaccard.
			* Time series -> use Euclidean distance
			* Time series with different magnitudes -> use Correlation
			 
That was a pretty long chapter. Lots learnt !
Best thing that I learnt outside the chapter was 'how to write mathematical equations in a blog'! Used a Javascript library named MathJax which renders LaTeX notation at runtime into HTML. 

**Ref** : [http://docs.mathjax.org/en/latest/start.html](http://docs.mathjax.org/en/latest/start.html)

Putting this snippet in <head> section worked


	<script src="http://cdn.mathjax.org/mathjax/latest/MathJax.js" type="text/javascript">
	    MathJax.Hub.Config({
	        extensions: ["tex2jax.js","TeX/AMSmath.js","TeX/AMSsymbols.js"],
	        jax: ["input/TeX","output/HTML-CSS"],
	        tex2jax: {
	            inlineMath: [ ['$','$'], ["\\(","\\)"] ],
	            displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
	            processEscapes: true,
	        },
	        "HTML-CSS": { availableFonts: ["TeX"] }
	    });
	</script>

**Ref** : [http://narnia.cs.ttu.edu/drupal/node/129](http://narnia.cs.ttu.edu/drupal/node/129)

**References for this chapter :**

* Text : Introduction to Data Mining - Chapter 2
* ppt : [http://www-users.cs.umn.edu/~kumar/dmbook/dmslides/chap2_data.pdf](http://www-users.cs.umn.edu/~kumar/dmbook/dmslides/chap2_data.pdf)

### Chapter 3 - Exploring Data
Data exploration is a preliminary exploration of the data to better understand its characteristics.

* 3 Exploring Data
	* 3.1 The Iris Data Set
	* 3.2 Summary Statistics
		* 3.2.1 Frequencies and the Mode
		* 3.2.2 Percentiles
		* 3.2.3 Measures of Location : Mean and Median
		* 3.2.4 Measure of Spread : Range and Variance
		* 3.2.5 Multivariate Summary Statistics
		* 3.2.6 Other ways to Summarize the Data
	* 3.3 Visualization
		* 3.3.1 Motivations for Visualization
		* 3.3.2 General Concepts
		* 3.3.3 Techniques
		* 3.3.4 Visualizing Higher dimensional data
		* 3.3.5 Do's and Don'ts
	* 3.4 OLAP and Multidimensional Analysis
		* Representing Iris data as a multidimensional array
		* Multidimensional data : The General Case
		* Analyzing multidimensional data
		* Final comments on multidimensional data

`April 2014`

### Chapter 4 - Classification
Classification is the task of assigning objects to one of several pre-defined categories. E.g - detecting spam email messages based upon the message header and content, categorizing cells as malignant or benign based upon the results of MRI scans, and classifying galaxies based upon their shapes ..etc

* 4 Classification
	* 4.1 Preliminaries
	* 4.2 General Approach to solving a classification problem
	* 4.3 Decision Tree Induction 
		* 4.3.1 How a Decision Tree works
		* 4.3.2 How to build a Decision Tree
		* 4.3.3 Methods for expressing attribute test conditions
		* 4.3.4 Measure for selecting the Best Split
		* 4.3.5 Algorithm for Decision Tree induction
		* 4.3.6 An Example : Web Robot Detection
		* 4.3.7 Characteristics of Decision Tree Induction
	* 4.4 Model Overfitting
		* 4.4.1 Overfitting due to presence of noise
		* 4.4.2 Overfitting due to lack of representative samples
		* 4.4.3 Overfitting and the multiple comparison procedure
		* 4.4.4 Estimation of Generalization Errors
		* 4.4.5 Handling overfitting in Decision Tree Induction
	* 4.5 Evaluating the performance of a Classifier
		* 4.5.1 Holdout method
		* 4.5.2 Random subsampling
		* 4.5.3 Cross Validation
		* 4.5.4 Bootstrap
	* 4.6 Methods for Comparing Classifiers
		* Estimating a confidence interval for accuracy
		* Comparing the performance of two models
		* Comparing the performance of two classifiers


`May 2014`

### Chapter 8 - Cluster Analysis
Cluster analysis could be defined as "Finding groups of objects such that the objects in a group will be similar (or related) to one another and different from (or unrelated to) the objects in other groups."
In short, cluster analysis divides the data into groups(clusters) that are meaningful, useful or both.
There are many applications of cluster analysis to practical problems.

