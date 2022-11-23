import csv
from aablobwrapper import SynchBlobAppender

connection_string = "https://<storageaccount>.blob.core.windows.net/<container_name>"
credential = "<key>"
container_name = "<container_name>"
blob_name = "<blobname>"

with SynchBlobAppender(
    connection_string, credential, container_name, blob_name
) as appender:
    csv_writer = csv.writer(appender)
    csv_writer.writerow(["write", "some", "data"])
