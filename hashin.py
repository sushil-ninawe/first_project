from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col
from pyspark.sql.types import StringType
import hashlib

# Create a Spark session
spark = SparkSession.builder.appName("SHA256 with Pepper").getOrCreate()

# Example data
data = [("Alice", "alice@example.com"),
        ("Bob", "bob@example.com"),
        ("Carol", "carol@example.com")]

columns = ["name", "email"]

df = spark.createDataFrame(data, columns)

# Define the UDF for hashing with pepper
def sha256_with_pepper(value, pepper):
    if value is not None:
        value_with_pepper = f"{value}{pepper}"
        return hashlib.sha256(value_with_pepper.encode('utf-8')).hexdigest()
    else:
        return None

# Register the UDF
pepper = "your_pepper_here"  # Replace with your actual pepper
sha256_udf = udf(lambda x: sha256_with_pepper(x, pepper), StringType())

# Apply the UDF to hash the 'email' column
df = df.withColumn("hashed_email", sha256_udf(col("email")))

# Show the results
df.show(truncate=False)
