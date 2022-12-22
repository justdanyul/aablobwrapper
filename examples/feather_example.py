from aablobwrapper import SyncBlobAppender, BlobReader
import pandas as pd

connection_string = "https://<storageaccount>.blob.core.windows.net/<container_name>"
credential = "<key>"
container_name = "<container_name>"
blob_name = "<blobname>"

d = {"first_column": [1, 2], "second_column": [3, 4]}
data_frame = pd.DataFrame(data=d)

appender = SyncBlobAppender(connection_string, credential, container_name, blob_name)
data_frame.to_feather(appender)

blob_reader = BlobReader(connection_string, credential, container_name, blob_name)
df = pd.read_feather(blob_reader.get_file_like_object())
print(df)
