from pyspark import SparkContext, SparkConf


file_paths = ['hdfs:/user/ebrahimi/file1G.txt', 'hdfs:/user/ebrahimi/file5G.txt', 'hdfs:/user/ebrahimi/file10G.txt']


def delete_punctuation(x):
    new_str = str() + x
    for each in '''!()-[]{.};:'"\,<>/?@#$%^&*_~`|’“”…—–''':
        new_str = new_str.replace(each, "")
    return new_str.strip()


if __name__ == "__main__":
    conf = SparkConf().setAppName("app_sh")
    sparkContent = SparkContext(conf=conf)
    text_rdd = sparkContent.textFile(file_paths[0])
    words = text_rdd.flatMap(lambda line: line.split(" ")).filter(lambda x: x.strip())
    words = words.map(delete_punctuation).map(lambda x: x.lower())
    words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a+b).collect()
