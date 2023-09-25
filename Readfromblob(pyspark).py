# Add required imports
import com.microsoft.spark.sqlanalytics
from com.microsoft.spark.sqlanalytics.Constants import Constants
from pyspark.sql.functions import col
 
 
# Read from existing internal table
dfToReadFromTable = (spark.read
                     # If `Constants.SERVER` is not provided, the `<database_name>` from the three-part table name argument
                     # to `synapsesql` method is used to infer the Synapse Dedicated SQL End Point.
                     .option(Constants.SERVER, "hmcl-syn-prac-workspace.sql.azuresynapse.net")
                     # Defaults to storage path defined in the runtime configurations
                     .option(Constants.TEMP_FOLDER, "abfss://azureml@hmclsyndatalake.dfs.core.windows.net/stage")
                     # Three-part table name from where data will be read.
                     .synapsesql("hmcl_dedicated_prac.sales.region")
                     # Column-pruning i.e., query select column values.
                     .select("ID") #can select multiple columns
                     # Push-down filter criteria that gets translated to SQL Push-down Predicates.
                     #.filter(col("Title").contains("E"))
                     # Fetch a sample of 10 records
                     .limit(10))


# Show contents of the dataframe
dfToReadFromTable.show()
