# iceberg-geo

## Scala

### Einfacher Geo-Test

```
spark-shell \
  --conf spark.serializer=org.apache.spark.serializer.KryoSerializer \
  --conf spark.kryo.registrator=org.apache.sedona.core.serde.SedonaKryoRegistrator \
  --packages org.apache.sedona:sedona-spark-shaded-3.5_2.12:1.7.1,org.datasyslab:geotools-wrapper:1.7.1-28.5
```

```
:load sedona_test.scala
```

Wenn der Code ein zweites Mal ausfgeführt wird, erscheinen Warnungen, weil die Funktionen ein zweites Mal registriert werden wollen. -> Könnte man in ein init.scala auslagern o.ä.


### Iceberg-Geo lokal

```
spark-shell \
  --conf spark.serializer=org.apache.spark.serializer.KryoSerializer \
  --conf spark.kryo.registrator=org.apache.sedona.core.serde.SedonaKryoRegistrator \
  --conf spark.sql.catalog.local=org.apache.iceberg.spark.SparkCatalog \
  --conf spark.sql.catalog.local.type=hadoop \
  --conf spark.sql.catalog.local.warehouse=file:///Users/stefan/tmp/lakehouse \
  --packages org.apache.sedona:sedona-spark-shaded-3.5_2.12:1.7.1,org.datasyslab:geotools-wrapper:1.7.1-28.5,org.apache.iceberg:iceberg-spark-runtime-3.5_2.12:1.7.1
```



## Python

```
python -m venv .venv
```

```
source .venv/bin/activate
```

```
pip install apache-sedona geopandas
```

pyspark --packages org.apache.sedona:sedona-spark-shaded-3.5_2.12:1.7.1,org.datasyslab:geotools-wrapper:1.7.1-28.5
```

