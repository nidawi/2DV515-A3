from models.Page import Page
from models.Score import Score
from typing import List

MAX_ITERATIONS = 20

class Metrics:
  def __init__(self, pages: List[Page]):
    self.__pages = pages
    
    self.__calculate_page_ranks()
    self.__normalize_page_ranks()

  def get_word_frequency_score(self, page: Page, query: List[int]) -> int:
    score = 0

    for word in query:
      score += page.get_word_count(word)
    
    return score

  def get_document_location_score(self, page: Page, query: List[int]) -> int:
    score = 0

    for word in query:
      wordIndex = page.get_word_index(word)
      if wordIndex >= 0:
        score += wordIndex + 1
      else:
        score += 100000
    
    return score

  def normalize_scores(self, scores: List[Score]) -> None:
    """
    Normalizes the scores in the provided list of scores.
    This method assumes that the scores haven't already been normalized.
    """
    minScore = (min(scores, key=lambda x : x.get_location_score())
    .get_location_score())
    maxScore = (max(scores, key=lambda x : x.get_content_score())
    .get_content_score())

    for score in scores:
      contentScore = score.get_content_score()
      locationScore = score.get_location_score()

      score.set_location_score(minScore / max(locationScore, 0.00001))
      score.set_content_score(contentScore / max(maxScore, 0.00001))

  def __calculate_page_ranks(self) -> None:
    for _ in range(0, MAX_ITERATIONS):

      # no need to iterate twice here.
      for page in self.__pages:
        pageRank = self.__iterate_pr(page)
        page.set_page_rank(pageRank)

  def __normalize_page_ranks(self) -> None:
    maxRank = (max(self.__pages, key=lambda x : x.get_page_rank())
      .get_page_rank())
    
    for page in self.__pages:
      pageRank = page.get_page_rank()
      page.set_page_rank(pageRank / (max(maxRank, 0.00001)))

  def __iterate_pr(self, page: Page) -> float:
    pr = 0
    for otherPage in self.__pages:
      if otherPage.has_link_to(page):
        pr += otherPage.get_page_rank() / otherPage.get_num_links()

    pr = (0.85 * pr) + 0.15
    return pr