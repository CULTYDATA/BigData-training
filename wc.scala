val data = spark.read.textFile("...path to leo").as[String]
val words = data.flatMap(value => value.split("\\s+"))
val groupedWords = words.groupByKey(_.toLowerCase)
val counts = groupedWords.count()
counts.show()