streaming_jar=/opt/hadoop-3.3.6/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar
scripts_path=/scripts/words-count
output_path=/output-words

rm -r -f $output_path
hdfs dfsadmin -safemode leave
hdfs dfs -rm -r $scripts_path
hdfs dfs -rm -r -f $output_path
hdfs dfs -mkdir -p $scripts_path
hdfs dfs -put $scripts_path/* $scripts_path
hadoop jar $streaming_jar -file $scripts_path/reducer.py -file $scripts_path/mapper.py -mapper $scripts_path/mapper.py -reducer $scripts_path/reducer.py -input $scripts_path/input.txt -output $output_path
hdfs dfs -cat $output_path/part-00000
hdfs dfs -get $output_path/part-00000 $output_path/output.txt