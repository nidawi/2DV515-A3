from models.Page import Page
from models.Score import Score
from models.Linker import Linker
from lib.Metrics import Metrics
from lib.utils import normalize_path
from typing import List
import io
import os

# This Indexer has far too many responsibilities.
class Indexer:
  def __init__(self, rootFolder: str, linkMgr: Linker):
    self.__root = rootFolder
    self.__linkMgr = linkMgr
    self.__pages = []
    self.__wordMap = {}
    self.__load_root()
    self.__metrics = Metrics(self.__pages)

  def search_test(self, query: str):
    scores = []
    queryWords = self.__parse_query_string(query)

    for page in self.__pages:
      # create and calculate scores
      pageScore = Score(page)
      wordFreq = self.__metrics.get_word_frequency_score(page, queryWords)
      docLoc = self.__metrics.get_document_location_score(page, queryWords)
      
      pageScore.set_content_score(wordFreq)
      pageScore.set_location_score(docLoc)
      scores.append(pageScore)

    # normalize scores
    self.__metrics.normalize_scores(scores)

    # generate results
    relevantScores = list(filter(lambda x : x.get_content_score() > 0, scores))

    # sort list
    relevantScores.sort(key=lambda x : x.get_weighted_score(), reverse=True)
    
    return relevantScores[0:5]

  def __load_root(self) -> None:
    """Loads all files in the root folder."""
    # loop through all files and load them as separate pages
    for root, _, files in os.walk(self.__root):
      for fileName in files:
        filePath = normalize_path(os.path.join(root, fileName))
        newPage = Page(fileName)

        if self.__linkMgr is not None:
          pageLinks = self.__linkMgr.get_links_for(fileName)
          newPage.add_links(pageLinks)

        self.__read_file(filePath, newPage)
        self.__pages.append(newPage)

  def __read_file(self, path: str, page: Page) -> None:
    """Reads the given file and fills the provided page with the words contained."""
    # todo: better naming for this method
    fileContents = open(path).read().strip()
    for word in fileContents.split():
      page.add_word(self.__get_word_id(word))

  def __get_word_id(self, word: str) -> int:
    if word in self.__wordMap:
      return self.__wordMap[word]
    else:
      _id = len(self.__wordMap)
      self.__wordMap[word] = _id
      return _id
  
  def __get_word_id_no_add(self, word: str) -> int:
    if word in self.__wordMap:
      return self.__wordMap[word]
    else:
      return -1

  def __parse_query_string(self, query: str) -> List[int]:
    """Parses a query string and returns a list of int representations."""
    # could make this more complex later.
    queryWords = list(map(
      lambda x : self.__get_word_id_no_add(x),
      query.strip().split()))

    return queryWords

  # override some internals
  def __len__(self) -> int:
    return len(self.__pages)