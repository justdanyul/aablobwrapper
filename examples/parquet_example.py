from aablobwrapper import SyncBlobAppender, BlobReader
import pandas as pd

connection_string = "https://<storageaccount>.blob.core.windows.net/<container_name>"
credential = "<key>"
container_name = "<container_name>"
blob_name = "<blobname>"

d = {"first_column": [1, 2], "second_column": [3, 4]}
data_frame = pd.DataFrame(data=d)

appender = SyncBlobAppender(
    connection_string, credential, container_name, blob_name, binary=True
)

data_frame.to_parquet(appender, compression="gzip")

blob_reader = BlobReader(
    connection_string, credential, container_name, blob_name, binary=True
)

df = pd.read_parquet(blob_reader.get_file_like_object())
print(df)
