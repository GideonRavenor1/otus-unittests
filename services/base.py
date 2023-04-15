from abc import ABC, abstractmethod

from managers.file import MatrixFileManager


class BaseService(ABC):
    file_manager = MatrixFileManager()
    
    @abstractmethod
    def __call__(self) -> None:
        raise NotImplementedError
    