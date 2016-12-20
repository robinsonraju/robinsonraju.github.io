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

* Clustering for Understanding
	* Biology - creating taxonomy
	* Information Retrieval - grouping search results from the web
	* Climate - finding patterns in the atmosphere
	* Psychology and medicine - identify illness
	* Business - segment customers
* Clustering for Utility
	* Summarization - apply costly algorithms to cluster prototypes instead of the entire dataset. 
	* Compression - prototypes are used when data objects are similar and loss is acceptable. 
	* Efficiently finding nearest neighbors - use prototypes to reduce number of pairwise distance computations. 

* 8.1 Overview
	* 8.1.1 What is Cluster Analysis
		* Defined above. 
		* Groups data objects based only on information found in the data that describes the objects and their relationships. 
		* Notion of a cluster is ambiguous
		* Classification is "Supervised Classification" and Cluster analysis is "Unsupervised Classification"
		* "Segmentation" and "Partitioning" are also sometimes synonymous with Clustering
	* What is not Cluster Analysis
		* Supervised Classification
		* Simple segmentation
		* Results of a query
		* Graph partitioning
	* 8.1.2 Different types of Clusterings
		* Hierarchical vs Partitional
			* Hierarchical (nested) - leaves are singletons
			* Partitional (unnested) - non overlapping subsets
		* Exclusive vs Overlapping vs Fuzzy
			* Exclusive - assign each object to a single cluster
			* Overlapping - objects can simultaneously belong to more than one cluster
			* Fuzzy - every object belongs to every cluster with a membership weight between 0(absolutely doesn't belong) and 1(abs belongs)
				* caveat : it doesn't address true multi-class situations since the weights need to add up to 1.
		* Complete vs Partial
			* Complete - assigns every object to a cluster
			* Partial - doesn't assign every object to a cluster
		* Heterogeneous vs Homogeneous
	* 8.1.3 Different types of Clusters
		* Well Separated - any point in a cluster is closer (more similar) to every other point in the cluster than to any point not in the cluster. Can have any shape. 
		* Prototype based (center based) -  an object in a cluster is closer (more similar) to the “center” of a cluster, than to the center of any other cluster. 
			* for data with continuous attributes, center is often the centroid. when centroid is not meaningful (data with categorical attributes), centre is often the medoid. 
			* tends to be globular. 
		* Graph based - group of objects that are connected to one another but have no connection to objects outside the group. (Connected Components)
			* Contiguity-based - 2 objects are connected only if they are within a specified distance of each other. Useful when clusters are irregular or intertwined. 
			* Clique - another example of graph based cluster. 
		* Density based - a cluster is a dense region of objects that is surrounded by a region of low density. Used when clusters are irregular or intertwined and when noise and outliers are present. 
		* Shared property (conceptual clustering) - Finds clusters that share some common property or represent a particular concept.
		* Objective function - Finds clusters that minimize or maximize an objective function.
	* Characteristics of Input data
		* Type of proximity/density measure
		* Sparseness
		* Attribute Type
		* Type of data
		* Dimensionality
		* Noise and Outliers
		* Type of Distribution
	* Clustering Algorithms
		* K-means - prototype based, partitional clustering technique - finds k clusters represented by their centroids. 
		* Hierarchical Clustering - leaves are singletons, top down or bottom up. 
		* DBSCAN - density based, partial that produces a partitional clustering. number of clusters is automatically determined by the algorithm. 
* 8.2 K-means
	* Partitional clustering technique in which each cluster is associated with a centroid and each point is assigned to a cluster with the closest centroid. Number of clusters K, must be given as input. 
	* 8.2.1 The basic K-means algorithm
		* Initial centroids are often chosen randomly. 
		* The centroid is generally the mean of the points in the cluster
		* Closeness is measured by Euclidean distance, cosine similarity, correlation ..etc. 
		* Most of the convergence happens the first few iterations
		* Complexity is O(I * K * m * n)
		* Assigning points to the closest centroid - Manhattan(L1) distance can be used for Euclidean data, Jaccard measure for document data
		* Centroids and Objective function - e.g for objective function : minimize the squared distance of each point to its closest centroid. 
		* Data in Euclidean space - Objective function used is SSE(Sum of Squared Error) also known as 'scatter'.                                     
			* where dist is the standard Euclidean (L2) distance b/w objects. 
			* Centroid that minimizes the SSE of a cluster is the mean 
			* Given 2 different sets of clusters, we prefer one with lower SSE.  
		* Document data 
			* represented as a DTM(document term matrix) 
			* objective is to maximize similarity of the objects in the cluster to cluster centroid. 
			* The analogous quantity to SSE is 'total cohesion'
		* The General case 
			* There are many choices for the proximity function, centroid and objective function that can be used in basic k-means algorithm and that are guaranteed to converge.                  
			* Bregman divergence includes squared Euclidean distance, the Mahalanobis distance and cosine similarity. 
		* Choosing initial centroids
			* Eg. 1 - Poor initial centroids : Randomly selected initial centroids may provide sub-optimal clustering with a higher SSE. 
			* Eg. 2 - Limits of random initialization 
			* If there are K 'real' clusters, chance of selecting one centroid from each is very small. 
		* Solutions to Initial centroids problem
			* Perform multiple runs
				* One way to minimize the effect or a poor random initial choice of centroids is to perform multiple runs. 
				* But this also need not give optimal clustering. If a centroid falls between a pair of clusters, it will be stuck there by making one cluster out of 2. 
			* Use hierarchical clustering on a sample
				* One effective approach to counter the limitations of random poor initial centroids is to take a sample of points and cluster them using hierarchical clustering technique and use those centroids as initial centroids. 
				* But this is practical only if sample is relatively small and k is small compared to sample size. 
			* Iterative approach
				* Select first point at random (or take centroid of all points)
				* for each successive initial centroid, select a point that is farthest from the previously selected centroids. 
				* the downside is that this could select outliers. 
			* Select more than K centroids
			* Post processing
			* Bisecting K-means
		* Time and Space complexity
			* Storage required : O((m + K)n) , m = number of points, n = number of attributes
			* Time required : O(I * K * m * n) , I = number of iterations 
	* 8.2.2 K-means: Additional issues
		* Handling empty clusters
			* Basic K-means algo can yield empty clusters. 
			* Choose a replacement otherwise SSE will be large
			* Approach 1 : Choose a replacement point that is farthest from any current centroid
			* Approach 2 : Choose a replacement point from the centroid that has highest SSE. This would split the cluster and reduce overall SSE.  
		* Outliers
			* If there are outliers, centroids may not be as representative as they ought to be and SSE would be higher as well. 
			* One approach is to discover outliers and eliminate them beforehand. But there could be situations where outliers are important (compression, financial data) 
			* Another approach is to identify outliers during pre-processing. Identify points with high contributions to SSE. 
			* Also we could eliminate small clusters
		* Reducing the SSE with post processing
			* One way to reduce SSE is to increase number of clusters (larger K). 2 strategies that decrease SSE by increasing K are - 
				* Split a cluster - Choose a cluster with largest SSE or largest standard deviation for an attribute. 
				* Introduce a new centroid - One approach is to choose a point farthest from any cluster center. Another is to choose a point at random. 
			* 2 strategies that decrease K and try to minimize the SSE increase are -
				* Disperse a cluster - removing a centroid and assigning the points to other clusters.  Disperse a cluster that doesn't contribute much to the total SSE. 
				* Merge 2 clusters - Clusters with closest centroids are usually chosen. Strategy is same as that used in hierarchical clustering. 
				* Commonly used approach is to alternate cluster splitting and merging phases. 
		* Updating centroids incrementally
			* In the basic K-means algorithm, centroids are updated after all points are assigned to a centroid. An alternative is to update the centroids after each assignment (incremental approach). Each assignment updates 0 or 2 centroids.  
			* Pros
				* Guarantees that empty clusters are not produced. 
				* Relative weights may be adjusted. Better accuracy and faster convergence are possible if weights are used. 
			* Cons:
				* It is more expensive
				* Introduces an order dependency (clusters produced depends on the order in which points are processed) . Although this can be overcome by randomizing the order. 
	* 8.2.3 Bisecting K-means
		* A straightforward extension of the basic K-means algorithm that is based on a simple idea: to obtain K clusters, split the set of all points into two clusters, select one of these clusters to split, and so on, until K clusters have been produced.
		* There are different ways to choose which cluster to split, say using size or SSE. 
		* Usually the the clusters are refined by using the resulting centroids as initial centroids for basic k-means algorithm. This is useful since during bisecting k-means we're using k-means algorithm 'locally' 
		* Bisecting K-means is less susceptible to initialization problems. 
		* Also we can use bisecting k-means for hierarchical clustering. 
	* 8.2.4 K-means and different types of clusters
		* K-means has difficulty in detecting natural clusters when clusters have non-spherical shapes or widely different sizes or densities. 
		* This could be overcome if the user is willing to increase K and have more clusters. So a cluster might have many sub clusters. 
	* 8.2.5 Strengths and weaknesses
		* Strengths : Used for wide variety of data types, Very efficient 
		* Weaknesses : Cannot handle non-globular clusters, not good with data that has outliers. 
	* 8.2.6 K-means as an optimization problem
		* Gradient descent - involves picking an initial solution and then repeating the fol- lowing two steps: compute the change to the solution that best optimizes the objective function and then update the solution.
		* Derivation of K-means as an algorithm to minimize the SSE (sum of squared errors): Proof that the best centroid for minimizing the SSE of a cluster is the mean of the points in the cluster. 
		* Derivation of K-means for SAE (sum of absolute errors) : Ck is the median of the cluster. 
* 8.3 Agglomerative Hierarchical Clustering
	* 2 approaches of hierarchical clustering - 
		* Agglomerative - Start with the points as individual clusters and, at each step, merge the closest pair of clusters. 
		* Divisive - Start with one, all-inclusive cluster and, at each step, split a cluster until only singleton clusters of individual points remain. 
	* Often displayed graphically using a tree-like diagram called dendogram, which displays sub-cluster relationships and also the order in which the clusters were merged. 
	* Don't have to assume any particular number of clusters. 
	* May correspond to meaningful taxonomies. 
	* 8.3.1 Basic Agglomerative Hierarchical Clustering Algorithm
		* Key operation is the computation of proximity
		* Defining proximity b/w clusters
			* Cluster proximity is typically defined with a particular type of cluster in mind. For example, many agglomerative hierarchical clustering techniques, such as MIN, MAX, and Group Average, come from a graph-based view of clusters.
		* Time and Space complexity
			* Proximity matrix requires the storage of 1/m^2 proximities. The space needed to keep track of the clusters is proportional to the number of clusters. Hence, the total space complexity is O(m^2).
			* There are m steps and at each step the size, m^2, proximity matrix must be updated and searched. So time complexity is O(m^3). It can be reduced to O(m^2 log m) by keeping the data in a sorted list or heap
	* 8.3.2 Specific Techniques of similarity measures
		* MIN (single link) 
			* Similarity of two clusters is based on the two most similar (closest) points in the different clusters. Determined by one pair of points, i.e., by one link in the proximity graph.
			* Strength : Can handle non-eliptical shapes.
			* Weakness : Sensitive to noise and outliers.
		* MAX (complete link)
			* Similarity of two clusters is based on the two least similar (most distant) points in the different clusters. Determined by all pairs of points in the two clusters.
			* Strength : Less susceptible to noise and outliers
			* Weakness : Tends to break large clusters, Biased towards globular clusters
		* Group Average 
			* Proximity of two clusters is the average of pairwise proximity between points in the two clusters.
			* Compromise between Single and Complete Link
			* Strength : Less susceptible to noise and outliers
			* Weakness : Biased towards globular clusters
		* Ward's method
			* Similarity of two clusters is based on the increase in squared error when two clusters are merged. 
			* Similar to group average if distance between points is distance squared.
			* Hierarchical analogue of K-means – Can be used to initialize K-means.
			* Strength : Less susceptible to noise and outliers
			* Weakness : Biased towards globular clusters
		* Distance between centroids : Similarity of two clusters is based on the distance between the centroids in the different clusters. 
	* 8.3.3 The Lance-Williams formula for Cluster Proximity 
		* A general formula for expressing hierarchical clustering proximity
		* Any of the cluster proximities that we have discussed above can be viewed as a choice of different parameters in the Lance-Williams formula 
	* 8.3.4 Key Issues in Hierarchical clustering
		* Lack of a global objective function : It is greedy technique in which optimization is done locally at that specific moment. 
		* Ability to handle different cluster sizes : In order to take care of the relative sizes of the clusters that are merged, we could take weights into account. 
			* UPGMA - Unweighted Pair Group Method using Arithmetic averages.
			* WPGMA - Weighted Pair Group Method using Arithmetic averages.
		* Merging decisions are final: Once the decision is made, it cannot be undone at a later time. 
	* 8.3.5 Strengths and Weaknesses : Already discussed above. 
* 8.4 DBSCAN
	* Density-based clustering locates regions of high density that are separated from one another by regions of low density. DBSCAN is a simple and effective density-based clustering algorithm. 
	* 8.4.1 Traditional Density: Center-based approach
		* In the center-based approach, density is estimated for a particular point in the data set by counting the number of points within a specified radius, Eps, of that point. This includes the point itself.
		* Classification of Points According to Center-Based Density
			* Core point: A point is a core point if it has more than a specified number of points (MinPts) within Eps.  
			* Border point: A border point has fewer than MinPts within Eps, but is in the neighborhood of a core point. 
			* Noise point: A noise point is any point that is neither a core point nor a border point.
	* 8.4.2 The DBSCAN algorithm                                          
		* Time and Space complexity
			* The basic time complexity of the DBSCAN algorithm is O(m × time to find points in the Eps-neighborhood), where m is the number of points. In the worst case, this complexity is O(m^2). If a different data structure is used, it could be as low as O(m logm).
			* The space requirement is O(m).
		* Selection of DBSCAN Parameters
			* The big question for DBSCAN is "how to determine the parameters Eps and MinPts ?"
			* The basic approach is to look at the behavior of the distance from a point to its kth nearest neighbor(k-dist).
			* Usually points within cluster will have small k-dist and noise points will have large k-dist. So if we compute the k-dist for all the data points for some k, sort them in increasing order, and then plot the sorted values, we expect to see a sharp change at the value of k-dist that corresponds to a suitable value of Eps. 
		* Clusters of Varying Density
			* DBSCAN can have trouble with density if the density of clusters varies widely. 
			* If the Eps threshold is low and if the densities vary, the denser clusters will be picked up and the dilute ones might be categorized as noise. 
	* 8.4.3 Strengths and Weaknesses
		* Strengths 
			* Resistant to Noise
			* Can handle clusters of different shapes and sizes
		* Weaknesses
			* Doesn't work well for clusters with varying densities
			* Doesn't work well for High-dimensional data
* 8.5 Cluster Evaluation
	* For supervised classification we have a variety of measures to evaluate how good our model is – Accuracy, precision, recall
	* For cluster analysis, the analogous question is "how to evaluate 'the goodness' of the resulting clusters?"
	* The difficulty - Many times clustering is done as part of exploratory data analysis. So validation may not be needed. Also, different clustering algorithms might need different evaluation techniques - SSE might be suited for K-means but not for DBSCAN. 
	* 8.5.1 Overview
		* Aspects of Cluster Validation
			* Determining the clustering tendency of a set of data, (distinguishing whether non-random structure actually exists in the data).
			* Determining the correct number of clusters.
			* Evaluating how well the results of a cluster analysis fit the data without reference to external information.
			* Comparing the results of a cluster analysis to externally known results, such as externally provided class labels.
			* Comparing two sets of clusters to determine which is better.
		* Items 1, 2, and 3 do not make use of any external information - they are unsupervised techniques - while item 4 requires external information. Item 5 can be performed in either a supervised or an unsupervised manner.
		* The evaluation measures (indices), that are applied to judge various aspects of cluster validity are traditionally classified into the following three types - 
			* Unsupervised (Internal indices) - 
				* Measures the goodness of a clustering structure without referring to external information. 
				* e.g SSE
				* Further divided into 2 classes - measures of cluster cohesion, cluster separation
			* Supervised (External indices)
				* Measures the extent to which the clustering structure discovered by a clustering algorithm matches some external structure.
				* e.g Entropy (measures how well cluster labels match externally supplied class labels) 
			* Relative
				* Compares different clusterings or clusters
				* e.g Two K-means clusterings can be compared using either the SSE or entropy.
	* 8.5.2 Unsupervised Cluster Evaluation Using Cohesion and Separation 
		* Cluster validity for a set of K clusters is a weighted sum of the validity of individual clusters. 
		* The validity function can be cohesion, separation or some combination of these. The weights will vary depending on the validity measure. For cohesion, higher values are better, for separation, lower values are better. 
		* Graph-Based View of Cohesion and Separation     
			* Cohesion of a cluster = sum of the weights of the links in the proximity graph that connect points within the cluster.
			* Separation between two clusters = sum of the weights of the links from points in one cluster to points in the other cluster.
			* The proximity function can be a similarity, a dissimilarity, or a simple function of these quantities
		* Prototype-Based View of Cohesion and Separation    
			* Cohesion of a cluster = sum of the proximities with respect to the prototype (centroid or medoid) of the cluster. 
			* Separation between two clusters = proximity of the two cluster prototypes.
			* There are two measures for separation because, the separation of cluster prototypes from an overall prototype is sometimes directly related to the separation of cluster prototypes from one another
		* Overall Measures of Cohesion and Separation
			* The previous measures (cohesion & separation) can be combined into an overall measure of cluster validity by using a weighted sum.   
		* Relationship between Prototype-Based Cohesion and Graph-Based Cohesion
			* For some proximity measures, the measures of cohesion and separation are equivalent for Graph-based and prototype-based approaches even though they seem distinct. 
			* For instance, for the SSE and points in Euclidean space, it can be shown that the average pairwise distance between the points in a cluster is equivalent to the SSE of the cluster                
		* Two Approaches to Prototype-Based Separation                              
			* When proximity is measured by Euclidean distance, the traditional measure of separation between clusters is the between group sum of squares (SSB), which is the sum of the squared distance of a cluster centroid.
			* The higher the total SSB of a clustering, the more separated the clusters are from one another.
		* Relationship between Cohesion and Separation
			* In some cases there is a strong relationship b/w cohesion and separation. It is possible to show that the sum of the total SSE and the total SSB is a constant.
			* Total sum of Squares (TSS) = sum of squares of the distance of each point to the overall mean of the data. 
			* TSS = SSE + SSB
			* The importance of this result is that minimizing SSE (cohesion) is equivalent to maximizing SSB (separation).
		* Evaluating Individual Clusters and Objects
			* Many of the measures that we studied above can be used to evaluate individual clusters and objects. 
			* We could rank individual clusters according to their specific value of cluster validity (cohesion or separation) and make some observations - 
			* Since higher value of cohesion may be better than lower, we could decide to split a cluster with lower value. 
			* If separation between clusters is low, we could decide to merge the clusters. 
			* Objects that contribute more to the cohesion and separation are probably near the interior of the cluster and others are probably near the edge. 
		* The Silhouette Coefficient
			* How to compute Silhouette coefficient
				* For the i th object, calculate its average distance to all other objects in its cluster. Call this value ai.
				* For the i th object and any cluster not containing the object, calculate the object's average distance to all the objects in the given cluster. Find the minimum such value with respect to all clusters; call this value bi.
				* Silhouette coefficient, si = (bi − ai)/ max(ai, bi).
			* The value of the silhouette coefficient can vary between −1 and 1.
			* When 
				$a_i = 0, s_i = 1$
	* 8.5.3 Unsupervised Cluster Evaluation Using the Proximity Matrix
		* Measuring Cluster Validity via Correlation
			* Input -> Similarity matrix for a data set and the cluster labels from a cluster analysis of the data set. 
			* Output -> Evaluate “goodness” of the clustering by looking at the correlation between the similarity matrix and the cluster labels.
			* While computing the correlation, since the matrices are symmetric, only the correlation between n (n - 1) / 2 entries needs to be calculated.
			* High correlation indicates that points that belong to the same cluster are close to each other.
		* Judging a Clustering Visually by Its Similarity Matrix
			* If we sort the rows and columns of the similarity matrix so that all objects belonging to the same class are together, then an ideal similarity matrix has a block diagonal structure.
			* Well-separated clusters show a very strong, block- diagonal pattern in the reordered similarity matrix. 
		* Computation of the proximity matrix takes O(m ^ 2) time
	* 8.5.4 Unsupervised Evaluation of Hierarchical Clustering
		* Previous approaches are for paritional clusterings. 
		* Cophenetic correlation is a popular evaluation measure for hierarchical clusterings
		* Cophenetic distance between two objects = Proximity at which an agglomerative hierarchical clustering technique puts the objects in the same cluster for the first time.
		* The CoPhenetic Correlation Coefficient (CPCC) is the correlation between the entries of the cophenic distance matrix and the original dissimilarity matrix and is a standard measure of how well a hierarchical clustering (of a particular type) fits the data.
	* 8.5.5 Determining the Correct Number of Clusters
		* Plot SSE and Silhouette co-efficient for different values of k. 
		* Choose k where there is a distinct knee in the SSE and a distinct peak in the silhouette coefficient  
	* 8.5.6 Clustering Tendency
		* Clustering algorithms produce clusters for any input data. But can the data even be clustered ? 
		* One approach is to evaluate the resulting clusters and only claim that a data set has clusters if at least some of the clusters are of 'good' quality. To make sure that the poor quality is not due to wrong choice of algorithm, we could use multiple algorithms and again evaluate the quality of the resulting clusters.
		* Another approach is to try to evaluate whether a data set has clusters without clustering. Most common approach, especially for data in Euclidean space, has been to use statistical tests for spatial randomness
	* 8.5.7 Supervised Measures of Cluster Validity
		* If we have external information about data, say in the form of class labels for the data objects, we could measure the degree of correspondence between the cluster labels and the class labels. 
		* We could have different approaches to measure the extent to which two objects that are in the same class are in the same cluster.  There are 2 main approaches - classification oriented and similarity oriented.
		* Classification-Oriented Measures of Cluster Validity
			* Uses measures from classification, such as entropy, purity, and the F-measure. These measures evaluate the extent to which a cluster contains objects of a single class. 
			* Entropy : The degree to which each cluster consists of objects of a single class
			* Purity: Another measure of the extent to which a cluster contains objects of
			* a single class. 
			* Precision : The fraction of a cluster that consists of objects of a specified class.
			* Recall : The extent to which a cluster contains all objects of a specified class.
			* F-measure : A combination of both precision and recall that measures the extent to which a cluster contains only objects of a particular class and all objects of that class.
		* Similarity-Oriented Measures of Cluster Validity
			* We can view this approach to cluster validity as involving the comparison of two matrices: 
			* (1) the ideal cluster similarity matrix discussed previously, which has a 1 if two objects are in the same cluster and 0 otherwise, and 
			* (2) an ideal class similarity matrix defined with respect to class labels, which has 1 if objects are in the same class and 0 otherwise. 
			* Rand statistic and Jaccard coefficient are two of the most frequently used cluster validity measures.
		* Cluster Validity for Hierarchical Clusterings
			* Supervised evaluation of a hierarchical clustering is more difficult for a variety of reasons, including the fact that a preexisting hierarchical structure often does not exist
			* To evaluate a hierarchical clustering, we compute, 
			* for each class, the F-measure for each cluster in the cluster hierarchy.
			* For each class, we take the maximum F- measure attained for any cluster.
			* Finally, we calculate an overall F-measure for the hierarchical clustering by computing the weighted average of all per-class F-measures, where the weights are based on the class sizes. 
	* 8.5.8 Assessing the Significance of Cluster Validity Measures
		* How do we interpret the significance of the number given by a cluster evaluation technique ?
		* Need to be aware of the basic definitions of evaluation measures used, like - a purity of 0 is bad, while a purity of 1 is good, an entropy of 0 is good, as is an SSE of 0.
		* If we don't have an absolute standard, a common approach is to interpret the value of our validity measure in statistical terms. e.g - plotting a histogram of SSE for random data sets. 


Wow ! That was a really long chapter and took 1 full day to read through! Thanks to Tan, Steinbach and Kumar for an excellent narrative. 

I really cannot forget this quote - 

> "Just as people can find patterns in clouds, data mining algorithms can find clusters in random data. While it is entertaining to find patterns in clouds, it is pointless and perhaps embarrassing to find clusters in noise."


**Ref** : 

* Power Point slides : [http://www-users.cs.umn.edu/~kumar/dmbook/index.php#item4](http://www-users.cs.umn.edu/~kumar/dmbook/index.php#item4)
* Sample Chapters : [http://www-users.cs.umn.edu/~kumar/dmbook/index.php#item2](http://www-users.cs.umn.edu/~kumar/dmbook/index.php#item2 )
