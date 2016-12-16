---
layout: post
title:  "Running Hadoop WordCount example"
date:   2015-09-15 22:50:11
author:     "Robinson Raju"
categories: tutorial big-data
header-img: "img/hadoop/words.jpg"
---

Here is a small example to run Wordcount program on hadoop. I've tried to do this using Cloudera VM and also MapR Sandbox. When you start ClouderaVM, it is already loaded with desktop and you can do all the work inside the desktop - open a browser, start a terminal..etc. MapR Sandbox doesnt come with GUI, so you'd have to ssh into the machine to work on it. You can open [https://localhost:8443](https://localhost:8443) in a browser to see Hue to see FileBrowser, DataBrowser, JobBrowser ..etc. 

## Using Cloudera VM

### Prerequisites
* Download and install [**Virtualbox**](https://www.virtualbox.org/wiki/Downloads). 
* Download [**Cloudera VM**](http://cloudera.com/content/cloudera/en/downloads/quickstart_vms/cdh-5-4-x.html) and import into VirtualBox. 

In the cloudera VM, open a terminal and go to the directory that contains hadoop library. 
```
cd /usr/lib/hadoop-mapreduce/
```

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

**Output**

> <img src="/img/hadoop/wc-output.png" width="520"/>

-----

## Using Map-R Sandbox

### Prerequisites
* Download and install [**Virtualbox**](https://www.virtualbox.org/wiki/Downloads). 
* Download [**MapR Sandbox**](https://www.mapr.com/products/mapr-sandbox-hadoop/download) and install into VirtualBox. 

### ssh into MapR Sandbox VM
```
ssh –p 2222 user01@localhost
```

### Create Sample files
```
mkdir input
```

```
cd input
```

```
echo "Hello world in HDFS" > testfile1
```

```
echo "Hadoop word count example in HDFS" > testfile2
```

### Run the Hadoop WordCount example
```
hadoop jar /opt/mapr/hadoop/hadoop-2.7.0/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.0-mapr-1506.jar wordcount /user/user01/input /user/user01/output
```

### After completion, view the output directory 
```
hadoop fs -ls /user/user01/output
```

### Check the output file to see the results 
```
hadoop fs -cat /user/user01/output/part-r-00000 
```

**Output**

> <img src="/img/hadoop/wc-output-mapr.png" width="520"/>

---
_Header Image - "**n1atsigns2 (Network graph of people on twitter connecting to the topics of Big Data, infochimps or Hadoop)**" by Philip Kromer via [Flickr](https://flic.kr/p/8R7PyB). Inverterd colors using Photoshop_