import csv, asyncio
from aablobwrapper import AsyncBlobAppender


async def main():
    connection_string = (
        "https://<storageaccount>.blob.core.windows.net/<container_name>"
    )
    credential = "<key>"
    container_name = "<container_name>"
    blob_name = "<blobname>"

    appender = AsyncBlobAppender(
        connection_string, credential, container_name, blob_name, binary=False
    )

    # ensure the blob exists. If you want to overwrite the existing blob, incase one
    # exist, use the argument: overwrite_existing=True
    await appender.create_append_blob()
    csv_writer = csv.writer(appender)

    await csv_writer.writerow(["write", "some", "data"])
    await appender.close()


asyncio.run(main())
