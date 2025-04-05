from sedona.spark import SedonaContext
from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder \
    .appName("SedonaExample") \
    .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer") \
    .config("spark.kryo.registrator", "org.apache.sedona.core.serde.SedonaKryoRegistrator") \
    .getOrCreate()

# Recommended way: Register Sedona using SedonaContext
sedona = SedonaContext.create(spark)

# Test Sedona SQL
spark.sql("SELECT ST_Point(1.0, 1.0) AS geom").show()
