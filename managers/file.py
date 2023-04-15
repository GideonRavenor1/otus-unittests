import os


class FileManager:
    
    @staticmethod
    def read(filename: str) -> list[int]:
        if not os.path.exists(filename):
            raise FileNotFoundError(f'File {filename} not found')
        
        with open(filename, "r", encoding="utf-8" ) as f:
            arr = f.readline().strip().split()
            return [int(x) for x in arr]
    
    @staticmethod
    def write(filename: str, arr: list[int]) -> None:
        with open(filename, 'w', encoding='utf_8') as f:
            f.write(' '.join(map(str, arr)))
    