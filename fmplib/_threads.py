from sniffio import AsyncLibraryNotFoundError, current_async_library

try:
    print(current_async_library())
except AsyncLibraryNotFoundError:
    print("No Context")
    pass