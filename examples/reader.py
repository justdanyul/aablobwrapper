from aablobwrapper import BlobReader
from csv import reader

connection_string = "https://<storageaccount>.blob.core.windows.net/<container_name>"
credential = "<key>"
container_name = "<container_name>"
blob_name = "<blobname>"

blob_reader = BlobReader(connection_string, credential, container_name, blob_name, binary=False)
file = blob_reader.get_file_like_object()
csv_reader = reader(file)
for row in csv_reader:
    print(row)

file.close()
