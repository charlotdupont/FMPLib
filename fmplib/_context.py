import asyncio
import traceback
from typing import Any, Callable, Optional


class AsyncContextManager:
    def __init__(self):
        self._loop = None





class AsyncContextManagerr:
    def __init__(self, create_loop_callable: Callable[[], Optional[asyncio.AbstractEventLoop]] | None = None, *args, **kwargs):
        self._loop = None
        self._create_loop_callable = create_loop_callable
        self._create_loop_args = args
        self._create_loop_kwargs = kwargs

    def __enter__(self):
        try:
            self._loop = asyncio.get_running_loop()
        except RuntimeError:
            if self._create_loop_callable:
                self._loop = self._create_loop_callable(*self._create_loop_args, **self._create_loop_kwargs)
            else:
                self._loop = asyncio.new_event_loop()
                asyncio.set_event_loop(self._loop)

        return self

    def __exit__(self, exc_type: Optional[BaseException], exc_val: Optional[BaseException], exc_tb: Optional[Any]) -> None:
        print(6)
        if self._loop and self._loop != asyncio.get_running_loop():
            self._loop.close()

            print(5)
            # Log or handle the exception if needed
            if exc_type:
                print(f"Exception occurred: {exc_type}, {exc_val}")
                # Access traceback through traceback module
                traceback.print_exception(exc_type, exc_val, exc_tb)
