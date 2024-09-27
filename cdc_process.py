WITH entitlement_changes AS (
    SELECT
        empid,
        enttl_type,
        enttl_value,
        date_provision AS date_start,
        LEAD(date_provision, 1) OVER (PARTITION BY empid, enttl_type ORDER BY date_provision) AS next_date_provision
    FROM
        entitlements
)
SELECT
    empid,
    enttl_type,
    enttl_value,
    date_start,
    CASE
        WHEN next_date_provision IS NOT NULL THEN DATE_SUB(next_date_provision, 1)
        ELSE NULL
    END AS date_end
FROM
    entitlement_changes
ORDER BY
    empid, enttl_type, date_start;





Pyspark implementation 

from pyspark.sql import SparkSession
from pyspark.sql import Window
from pyspark.sql.functions import col, lead, date_sub

# Initialize Spark session
spark = SparkSession.builder.appName("Entitlement Lineage").getOrCreate()

# Sample data
data = [
    (123, 'credit_enntl', 'level_40', '2023-01-01'),
    (123, 'credit_enntl', 'level_50', '2023-01-31'),
    (123, 'credit_enntl', 'level_40', '2023-02-15')
]

# Create DataFrame
columns = ['empid', 'enttl_type', 'enttl_value', 'date_provision']
entitlements_df = spark.createDataFrame(data, columns)

# Convert date_provision to DateType
entitlements_df = entitlements_df.withColumn('date_provision', col('date_provision').cast('date'))

# Define window specification
window_spec = Window.partitionBy('empid', 'enttl_type').orderBy('date_provision')

# Use lead function to get the next date_provision
entitlements_with_lead = entitlements_df.withColumn(
    'next_date_provision', lead('date_provision', 1).over(window_spec)
)

# Subtract one day from the next_date_provision to get the date_end
entitlements_with_dates = entitlements_with_lead.withColumn(
    'date_end', date_sub(col('next_date_provision'), 1)
).withColumnRenamed('date_provision', 'date_start')

# Select the relevant columns and order the results
result_df = entitlements_with_dates.select(
    'empid', 'enttl_type', 'enttl_value', 'date_start', 'date_end'
).orderBy('empid', 'enttl_type', 'date_start')

# Show the result
result_df.show()
