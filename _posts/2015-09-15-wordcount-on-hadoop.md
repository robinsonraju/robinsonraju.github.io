---
layout: post
title:  "Running Hadoop WordCount example"
date:   2015-09-15 22:50:11
author:     "Robinson Raju"
categories: Big Data 
header-img: "img/hadoop/words.jpg"
---

### Create Sample files
```
echo "Hello world in HDFS" > /home/cloudera/testfile1
```

```
echo "Hadoop word count example in HDFS" > /home/cloudera/testfile2
```

### Create directory for the input files on the HDFS file system (type) 
```
hdfs dfs -mkdir /user/cloudera/input
```

### Copy the files from local filesystem to the HDFS filesystem 
```
hdfs dfs -put /home/cloudera/testfile1 /user/cloudera/input
```

```
hdfs dfs -put /home/cloudera/testfile2 /user/cloudera/input
```

### Run the Hadoop WordCount example
```
hadoop jar hadoop-mapreduce-examples.jar wordcount /user/cloudera/input /user/cloudera/output
```

### After completion view the output directory 
```
hdfs dfs -ls /user/cloudera/output
```

### Check the output file to see the results 
```
hdfs dfs -cat /user/cloudera/output/part-r-00000
```

---
_Header Image - "**n1atsigns2 (Network graph of people on twitter connecting to the topics of Big Data, infochimps or Hadoop)**" by Philip Kromer via [Flickr](https://flic.kr/p/8R7PyB)_