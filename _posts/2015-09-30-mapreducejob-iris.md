---
layout: post
title:  "A Simple MapReduce Job for Iris Dataset"
date:   2015-09-30 22:50:11
author:     "Robinson Raju"
categories: Big Data 
header-img: "img/hadoop/iris.jpg"
---

This blog is an attempt to walk through the process of using hadoop to analyze a dataset that might look similar to an actual dataset that we might encounter. 

In the last blog on wordcount, I used an eclipse project that was bundled automatically with the Cloudera VM and just modified the StubMapper, StubReducer and Driver to plugin the code for wordcount. In this, I thought I'll create one from scratch and see how it works. 

## Step #1 : Create a Java project 
Create a Java project using Eclipse. 
Add Mapper, Reducer and Driver stubs from the other project. You'll immediately notice that there are many compilation errors. 


## Step 2: Configure Build Path 
Add the following libraries from ``/usr/lib/hadoop/client`` and ``/cloudera/lib``

``Properties > Java Build Path > Add External Jars``

<img src="/img/hadoop/add_lib2.png" width="420"/>

<img src="/img/hadoop/add_lib1.png" width="420"/>

Also add ``<project>/conf`` as the class folder. 

<img src="/img/hadoop/class_folder.png" width="420"/>

Now the compilation issues would be resolved. 

## Step 3: Add code for Mapper and Reducer

The objective is to read the records from the data and compute the mean sepal length of each class of the Iris flower. 

### Mapper 

	package com.iris.data.mapreduce;
	import java.io.IOException;

	import org.apache.hadoop.io.FloatWritable;
	import org.apache.hadoop.io.LongWritable;
	import org.apache.hadoop.io.Text;
	import org.apache.hadoop.mapreduce.Mapper;

	public class IrisMapper extends Mapper<LongWritable, Text, Text, FloatWritable> {

		/**
		 * Iris data : http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data 
		 * Sample record: 5.1,3.5,1.4,0.2,Iris-setosa
		 * Attribute Information:
			   1. sepal length in cm
			   2. sepal width in cm
			   3. petal length in cm
			   4. petal width in cm
			   5. class: 
			      -- Iris Setosa
			      -- Iris Versicolour
			      -- Iris Virginica
		 * 
		 */
		@Override
		public void map(LongWritable key, Text value, Context context)
				throws IOException, InterruptedException {

			String[] columns = value.toString().split(",");
			float sepal_len = Float.valueOf(columns[0]);
			String flower_class = columns[4];
			
			context.write(new Text(flower_class), new FloatWritable(sepal_len));
		}
	}

### Reducer
	package com.iris.data.mapreduce;
	import java.io.IOException;

	import org.apache.hadoop.io.FloatWritable;
	import org.apache.hadoop.io.Text;
	import org.apache.hadoop.mapreduce.Reducer;

	public class IrisReducer extends
			Reducer<Text, FloatWritable, Text, FloatWritable> {

		@Override
		public void reduce(Text key, Iterable<FloatWritable> values, Context context)
				throws IOException, InterruptedException {

			float sum = 0;
			float count = 0;
			float mean_sepal_len = 0;
			for (FloatWritable val : values) {
				sum += val.get();
				count++;
			}
			
			mean_sepal_len = sum / count;
			context.write(key, new FloatWritable(mean_sepal_len));
		}

	}

## Run the Driver

You should see the following output

<img src="/img/hadoop/iris_output.png" width="420"/>

_Header Image - "**Iris**" by Pauline Rosenberg via [Flickr](https://flic.kr/p/6sZzjm)._