from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
import time
import argparse

file_paths = ['hdfs:/user/ebrahimi/file1G.txt', 'hdfs:/user/ebrahimi/file5G.txt', 'hdfs:/user/ebrahimi/file10G.txt']


def delete_punctuation(x):
    new_str = str() + x
    for each in '''!()-[]{.};:'"\,<>/?@#$%^&*_~`|’“”…—–''':
        new_str = new_str.replace(each, "")
    return new_str.strip()


def validate_args(args):
    if not (args.hdfs_input and args.hdfs_output):
        raise Exception("enter path of files")
    else:
        return f"hdfs:{args.hdfs_input}", f"hdfs:{args.hdfs_output}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--hdfs_input", help="path of input hdfs file")
    parser.add_argument("--hdfs_output", help="path of output hdfs file")
    input_path, output_path = validate_args(parser.parse_args())

    # conf = SparkConf().setAppName("app_sh")
    # sparkContent = SparkContext(conf=conf)
    spark = SparkSession.builder.appName("wordcount_sh").getOrCreate()
    sparkContent = spark.sparkContext

    text_rdd = sparkContent.textFile(input_path)
    start_time = time.time()
    print("start map-reduce actions")
    words = text_rdd.flatMap(lambda line: line.split(" ")).filter(lambda x: x.strip())
    words = words.map(delete_punctuation).map(lambda x: x.lower())
    result = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a+b).sortBy(lambda a: a[1], ascending=False)
    print(f"map-reduce actions done in: {time.time() - start_time}(seconds) ")
    result.saveAsTextFile(output_path)
