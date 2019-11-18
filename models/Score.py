from models.Page import Page

# Could make these dynamic in a "proper" system.
# def set_content_mods(...):
# or perhaps delegate this responsiblity somewhere else.
# like a score factory or similar
CONTENT_MOD = 1
LOCATION_MOD = 0.8
PAGERANK_MOD = 0.5
OUTPUT_DECIMAL_COUNT = 2

class Score:
  def __init__(self, page: Page):
    self.__page = page
    self.__contentScore = 0
    self.__locationScore = 0

  def get_content_score(self) -> float:
    return (self.__contentScore * CONTENT_MOD)

  def get_location_score(self) -> float:
    return (self.__locationScore * LOCATION_MOD)

  def get_pagerank_score(self) -> float:
    return (self.__page.get_page_rank() * PAGERANK_MOD)

  def get_weighted_score(self) -> float:
    return (self.get_content_score() +
    self.get_location_score() +
    self.get_pagerank_score())

  def get_page_name(self) -> str:
    """Law-of-demeter respecting alternative. :D"""
    return self.__page.get_name()

  def get_page_url(self) -> str:
    return self.__page.get_url()

  def set_content_score(self, score: float) -> None:
    self.__contentScore = score

  def set_location_score(self, score: float) -> None:
    self.__locationScore = score

  def jsonify(self) -> dict:
    return {
      "name": self.get_page_name(),
      "url": self.get_page_url(),
      "score": round(self.get_weighted_score(), OUTPUT_DECIMAL_COUNT),
      "content": round(self.get_content_score(), OUTPUT_DECIMAL_COUNT),
      "location": round(self.get_location_score(), OUTPUT_DECIMAL_COUNT),
      "pagerank": round(self.get_pagerank_score(), OUTPUT_DECIMAL_COUNT)
    }