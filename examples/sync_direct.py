import csv
from aablobwrapper import SyncBlobAppender

connection_string = "https://<storageaccount>.blob.core.windows.net/<container_name>"
credential = "<key>"
container_name = "<container_name>"
blob_name = "<blobname>"

appender = SyncBlobAppender(connection_string, credential, container_name, blob_name, binary=False)
csv_writer = csv.writer(appender)
csv_writer.writerow(["write", "some", "data"])
