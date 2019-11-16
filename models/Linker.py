from typing import List
from lib.utils import normalize_path
import io
import os

class Linker:
  def __init__(self, rootFolder: str):
    self.__root = rootFolder
    self.__linkMap = {}
    self.__load_root()

  def get_links_for(self, pageUrl: str) -> List[str]:
    return self.__linkMap[pageUrl]

  def __load_root(self) -> None:
    for root, _, files in os.walk(self.__root):
      for fileName in files:
        filePath = normalize_path(os.path.join(root, fileName))
        fileContents = self.__read_file(filePath)
        self.__linkMap[fileName] = fileContents

  def __read_file(self, file: str) -> List[str]:
    fileContents = []

    with open(file) as reader:
      for _, line in enumerate(reader):
        fileContents.append(line.strip())
    
    return fileContents

  def __len__(self) -> int:
    return len(self.__linkMap)