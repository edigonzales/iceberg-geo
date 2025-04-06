import org.apache.sedona.sql.utils.SedonaSQLRegistrator
SedonaSQLRegistrator.registerAll(spark)

val stmt = """
    SELECT ST_Point(1.0, 1.0) as geom;
"""

spark.sql(stmt).show()