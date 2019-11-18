from models.Score import Score
from timeit import default_timer as timer
from typing import List

COUNT_ID = "count"
START_ID = "start"
DEFAULT_QUERY_COUNT = 5

class Query:
  """Represents a query."""
  def __init__(self, query: str):
    self.__queryString = query
    self.__startTime = timer()
    self.__endTime = 0
    self.__scoresResult = []
  
  def get_query_time(self) -> float:
    return round((self.__endTime - self.__startTime), 3)

  def get_result_count(self) -> int:
    return len(self.__scoresResult)

  def get_results(self, **opt) -> List[Score]:
    start = self.__get_start(opt)
    end = self.__get_count(opt) + start

    return self.__scoresResult[start:end]

  def _add_result(self, results: List[Score]) -> None:
    self.__endTime = timer()
    self.__scoresResult = results

  def jsonify(self, **opt) -> {}:
    start = self.__get_start(opt)
    count = self.__get_count(opt)
    results = self.get_results(start=start, count=count)
    mappedResults = map(lambda x : x.jsonify(), results)
    
    return {
      "query": self.__queryString,
      "time": self.get_query_time(),
      "total": self.get_result_count(),
      "pages": list(mappedResults)
    }

  def __get_count(self, params: dict) -> int:
    if COUNT_ID in params:
      return params[COUNT_ID]
    else:
      return DEFAULT_QUERY_COUNT

  def __get_start(self, params: dict) -> int:
    if START_ID in params:
      return params[START_ID]
    else:
      return 0

  def __len__(self) -> int:
    return self.get_result_count()