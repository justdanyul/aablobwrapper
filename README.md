# aablobwrapper

For convenience, this module provide some wrappers for the Azure append blob writer. It implements the write function of the object and a context manager, allowing for you to easily use things like the CVS package, or simply appending to an append blob directly.

## Installation

```bash
pip install aablobwrapper
```


## Examples

```python
import csv
from aablobwrapper import SyncBlobAppender

connection_string = "https://<storageaccount>.blob.core.windows.net/<container_name>"
credential = "<key>"
container_name = "<container_name>"
blob_name = "<blobname>"

appender = SyncBlobAppender(connection_string, credential, container_name, blob_name, binary=False)
csv_writer = csv.writer(appender)
csv_writer.writerow(["write", "some", "data"])
```
for more examples, for example, to see how to use context managers or how to use the async version, see the examples folder.


