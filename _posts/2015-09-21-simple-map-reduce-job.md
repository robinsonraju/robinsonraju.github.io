---
layout: post
title:  "Writing a simple Mapper and Reducer for Wordcount"
date:   2015-09-21 23:50:11
author:     "Robinson Raju"
categories: Big Data 
header-img: "img/hadoop/words2.jpg"
---

The last blog was about how to run wordcount using the "hadoop-mapreduce-examples.jar" that was automatically available in the VMs. How would it be to really write the Mapper and Reducer for this? I searched a bit for an eclipse plugin to be able to create a MR project through eclipse that would have the template for Mapper and Reducer and I would just write the implementation. Found some plugins (e.g HDT) and some screencasts but didn't take me far. Remembered that there was an eclipse icon in the Cloudera VM. Started the VM, clicked on the icon and viola ! there was a sample project with Stubs for Mapper, Reducer and Driver. Exactly what I needed!

<img src="/img/hadoop/Stubs.png" width="420"/>

Put in the code for Mapper, Reducer and Driver in the Stub classes and ran the Driver. It worked like a charm. Here is the code for it. 

## Mapper
The map method takes key, value and context as inputs. The key represents the name of a document and the value is the contents of the document. For e.g, a record in a file. The map method below uses StringTokenizer to split the record into words, loops through the words and writes a 2-tuple (word, 1) into the context. Each mapper does this and what we get in the end is a list of key-value pairs. 

	import java.io.IOException;
	import java.util.StringTokenizer;

	import org.apache.hadoop.io.IntWritable;
	import org.apache.hadoop.io.LongWritable;
	import org.apache.hadoop.io.Text;
	import org.apache.hadoop.mapreduce.Mapper;

	public class StubMapper extends Mapper<LongWritable, Text, Text, IntWritable> {

		private final static IntWritable one = new IntWritable(1);
		private Text word = new Text();

		@Override
		public void map(LongWritable key, Text value, Context context)
				throws IOException, InterruptedException {

			String line = value.toString();
			StringTokenizer tokenizer = new StringTokenizer(line);
			while (tokenizer.hasMoreTokens()) {
				word.set(tokenizer.nextToken());
				context.write(word, one);
			}

		}
	}


## Reducer
A reducer takes an input of a key and list of values associated with the key, adds the counts and writes the output to the context. 
For e.g, input of (world, 1), (world, 1) gives output as (world, 2). 

	import java.io.IOException;

	import org.apache.hadoop.io.IntWritable;
	import org.apache.hadoop.io.Text;
	import org.apache.hadoop.mapreduce.Reducer;

	public class StubReducer extends
			Reducer<Text, IntWritable, Text, IntWritable> {

		@Override
		public void reduce(Text key, Iterable<IntWritable> values, Context context)
				throws IOException, InterruptedException {

			int sum = 0;
			for (IntWritable val : values) {
				sum += val.get();
			}
			context.write(key, new IntWritable(sum));
		}
	}

## Driver 

	import org.apache.hadoop.fs.Path;
	import org.apache.hadoop.io.IntWritable;
	import org.apache.hadoop.io.Text;
	import org.apache.hadoop.mapreduce.Job;
	import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
	import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
	import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
	import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;

	public class StubDriver {

		public static void main(String[] args) throws Exception {

			/*
			 * Validate that two arguments were passed from the command line.
			 */
			if (args.length != 2) {
				System.out.printf("Usage: StubDriver <input dir> <output dir>\n");
				System.exit(-1);
			}

			/*
			 * Instantiate a Job object for your job's configuration.
			 */
			Job job = new Job();

			/*
			 * Specify the jar file that contains your driver, mapper, and reducer.
			 * Hadoop will transfer this jar file to nodes in your cluster running
			 * mapper and reducer tasks.
			 */
			// job.setJarByClass(StubDriver.class);
			job.setOutputKeyClass(Text.class);
			job.setOutputValueClass(IntWritable.class);

			job.setMapperClass(StubMapper.class);
			job.setReducerClass(StubReducer.class);

			job.setInputFormatClass(TextInputFormat.class);
			job.setOutputFormatClass(TextOutputFormat.class);

			FileInputFormat.addInputPath(job, new Path(args[0]));
			FileOutputFormat.setOutputPath(job, new Path(args[1]));

			/*
			 * Specify an easily-decipherable name for the job. This job name will
			 * appear in reports and logs.
			 */
			job.setJobName("Stub Driver");

			/*
			 * Start the MapReduce job and wait for it to finish. If it finishes
			 * successfully, return 0. If not, return 1.
			 */
			boolean success = job.waitForCompletion(true);
			System.exit(success ? 0 : 1);
		}
	}

## How to Run

	Create an input directory named "input"
	
	Run As > Java Application (give 2 arguments "input" and "output")

Look at the the file 'part-r-00000' in the output directory
	<img src="/img/hadoop/wc-output-eclipse.png" width="320"/>

---

### References

* QuickStart VMs for CDH 5.4.x. (n.d.). Retrieved September 21, 2015, from [http://www.cloudera.com/content/cloudera/en/downloads/quickstart_vms/cdh-5-4-x.html](http://www.cloudera.com/content/cloudera/en/downloads/quickstart_vms/cdh-5-4-x.html)
* WordCount. (n.d.). Retrieved September 21, 2015, from [https://wiki.apache.org/hadoop/WordCount](https://wiki.apache.org/hadoop/WordCount)   

---

_Header Image - "**Words**" by Cayce Newell via [Flickr](https://flic.kr/p/4BsjLY)._