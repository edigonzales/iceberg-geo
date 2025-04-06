from sedona.spark import SedonaContext
from pyspark.sql import SparkSession
from pyspark.sql.types import StringType
from pyspark.sql.functions import lit

# Create Spark session
spark = SparkSession.builder \
    .appName("SedonaExample") \
    .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer") \
    .config("spark.kryo.registrator", "org.apache.sedona.core.serde.SedonaKryoRegistrator") \
    .config("spark.sql.extensions", "org.apache.sedona.sql.SedonaSqlExtensions") \
    .config("spark.sql.catalog.local", "org.apache.iceberg.spark.SparkCatalog") \
    .config("spark.sql.catalog.local.type", "hadoop") \
    .config("spark.sql.catalog.local.warehouse", "file:///Users/stefan/tmp/lakehouse") \
    .getOrCreate()

# Register Sedona using SedonaContext
sedona = SedonaContext.create(spark)

# Create an empty DataFrame with the schema you want
empty_rdd = spark.sparkContext.emptyRDD()
empty_df = spark.createDataFrame(empty_rdd, "id STRING, geom GEOMETRY")

# Write the empty DataFrame to create the Iceberg table
(empty_df.write
    .format("iceberg")
    .mode("overwrite")  # Use 'append' if you don't want to overwrite existing tables
    .option("write.format.default", "parquet")
    .option("format-version", "3")
    .saveAsTable("local.myschema.geotable"))
