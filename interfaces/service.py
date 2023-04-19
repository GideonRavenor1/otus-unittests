from typing import Protocol


class IService(Protocol):
    
    def __call__(self) -> None:
        ...
