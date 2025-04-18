# Курс "Хранение и обработка больших данных на платформе Hadoop и Apache Spark",  2025

За основу взят [репозиторий Щербакова Василия](https://github.com/sh-vasily/bigdata-2024)

Для знакомства с дистрибутивом Cloudera Hadoop понадобится:
- [Virtual Box](https://www.virtualbox.org/wiki/Downloads)
- [Виртуальна машина Cloudera QuickStart](https://downloads.cloudera.com/demo_vm/virtualbox/cloudera-quickstart-vm-5.12.0-0-virtualbox.zip)
Cloudera QuickStart VM уже давно не поддерживается. Это очень старая версия, для ознакомления с экостсемой подойдет, для реальной работы - не очень.  

Пример работы с HDFS - часть MapReduce задачи по подсчету слов:
- [Пример работы с hdfs](map-reduce/words-count/execute.sh)

Примеры Hadoop MapReduce, для запуска их на python через Hadoop Streaming нужен реальный кластер, который поднимается в Docker 
- [Развертывание кластера Hadoop](docker) : datanode - 3 шт, namenode, history-server, resourcemanager, nodemanager.
- [Подсчет слов](map-reduce/words-count)
- [Поиск максимальной стоимости акций по секторам](map-reduce/stocks-max). Dataset https://www.kaggle.com/datasets/dinnymathew/usstockprices

Примеры c Apache Spark:
- [Подсчет количества слов с помощью RDD](spark/wordcount-rdd.py)
- [Подсчет количества слов SparkSQL](spark/wordcount-sql.py) - пример как делать не надо
- [Работа с простым json файлом](/spark/dataset-json.py) 
- Исследование данных о лесных пожарах 2012-2021, данные https://data.rcsi.science/data-catalog/datasets/202/
  в Git для примера помещен "малый" набор данных, полный можно скачать и подложить для рассчетов




