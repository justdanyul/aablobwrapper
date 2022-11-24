from aablobwrapper import BlobReader
from csv import reader

connection_string = "https://<storageaccount>.blob.core.windows.net/<container_name>"
credential = "<key>"
container_name = "<container_name>"
blob_name = "<blobname>"

with BlobReader(
    connection_string, credential, container_name, blob_name
) as blob_reader:
    file = blob_reader.get_file_like_object(binary=False)
    csv_reader = reader(file)
    for row in csv_reader:
        print(row)
