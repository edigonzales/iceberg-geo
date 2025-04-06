import org.apache.sedona.sql.utils.SedonaSQLRegistrator
SedonaSQLRegistrator.registerAll(spark)

val stmt = """
    CREATE TABLE local.myschema.geotable (id string, geom geometry)
    USING iceberg
    TBLPROPERTIES('format-version'='3');
"""

spark.sql(stmt).show()