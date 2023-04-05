# Databricks notebook source
# DBTITLE 1, The Credentials of azure storage to connect
storage_account_name = "relgendy"
storage_account_access_key = "YTQ1cy1bOeU59C/5cp+Fjk+/DKHvr9LlimYMwuB+IU9yUtMzmvAISJy9SH4sRC9z87AyOM5ZTCyX+AStInnX4g=="
container_name = "historicaldata"
file_name = "Project/azure project/AddingYearColumnToCleanedData"
    

# COMMAND ----------

# DBTITLE 1,using spark to access the file path
csv_uri = f"wasbs://{container_name}@{storage_account_name}.blob.core.windows.net/{file_name}"
spark.conf.set(f"fs.azure.account.key.{storage_account_name}.blob.core.windows.net", storage_account_access_key)

# COMMAND ----------

df = spark.read.csv(csv_uri, header=True, inferSchema=True)

# COMMAND ----------

# DBTITLE 1,Data Visualisation
display(df)

# COMMAND ----------

# DBTITLE 0,Results:
# MAGIC %md # From Statistics,it is found that: 
# MAGIC  - Revenue increases through the years with increasing the sales_quantity
# MAGIC  - the max Revenue & Sales quantity were the same in 2019 and 2020 which is 58.7564M and 38.069k. However,increasing the min. Revenue or the min. Sales quantity in 2020 made it the highest range through the years.
# MAGIC  - the relation between the Revenue and the Sales quantity is almost proportional as the increase in sales results in increasing the Revenue.
# MAGIC  

# COMMAND ----------

# DBTITLE 1,the 'year' column here after showing data profile, has a data type of int. So, we convert it to string/date type

from pyspark.sql.functions import col,to_date,date_format

df1=df.withColumn('Year',to_date(col('Year').cast('string'),'yyyy'))
df1 = df1.withColumn('Year', date_format('Year', 'yyyy'))
#df1=df1.drop('Year').withColumnRenamed('Year','year')

# COMMAND ----------

display(df1)
