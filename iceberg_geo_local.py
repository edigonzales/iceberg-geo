from sedona.spark import SedonaContext
from pyspark.sql import SparkSession

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

# Recommended way: Register Sedona using SedonaContext
sedona = SedonaContext.create(spark)

stmt = """
    CREATE TABLE local.myschema.geotable (id string, geom geometry)
    USING iceberg
    TBLPROPERTIES('format-version'='3');
"""

# Test Sedona SQL
spark.sql(stmt).show()
