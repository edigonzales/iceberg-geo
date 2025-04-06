from sedona.register import SedonaRegistrator
from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder \
    .appName("SedonaExample") \
    .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer") \
    .config("spark.kryo.registrator", "org.apache.sedona.core.serde.SedonaKryoRegistrator") \
    .getOrCreate()

# Register Sedona SQL functions
SedonaRegistrator.registerAll(spark)

# Test Sedona SQL function
spark.sql("SELECT ST_Point(1.0, 1.0) AS geom").show()
