from typing import List

class Page:
  def __init__(self, url):
    self.__url = url
    self.__wordIds = []
    self.__pageRank = 1.0
    self.__links = set()
  
  def get_name(self) -> str:
    return self.__url

  def get_url(self) -> str:
    return "/wiki/%s" % self.__url

  def get_words(self) -> List[int]:
    return self.__links

  def get_page_rank(self) -> float:
    return self.__pageRank

  def get_num_links(self) -> int:
    return len(self.__links)

  def get_word_count(self, wordId: int) -> int:
    # we sum together 1's for every word in our wordlist that matches the requested wordid
    # python is so cool
    return sum(1 for word in self.__wordIds if word == wordId)

  def get_word_index(self, wordId: int) -> int:
    if wordId in self.__wordIds:
      return self.__wordIds.index(wordId)
    else:
      return -1

  def set_page_rank(self, score: float) -> None:
    self.__pageRank = score

  def add_word(self, wordId: int) -> None:
    # add duplicates so that we can count them
    # is there a better solution?
    self.__wordIds.append(wordId)

  def add_links(self, links: List[str]) -> None:
    # Is there a better way to do this?
    for link in links:
      self.__links.add(link)

  def has_link_to(self, page: 'Page') -> bool:
    return page.get_url() in self.__links

  def has_word(self, wordId: int) -> bool:
    return wordId in self.__wordIds

  def has_any_word(self, wordIds: List[int]) -> bool:
    # we check if any word in our wordlist matches any word in the requested wordlist
    return any(wordId in self.__wordIds for wordId in wordIds)
  
  def has_all_words(self, wordIds: List[int]) -> bool:
    return all(wordId in self.__wordIds for wordId in wordIds)

  # overwrite things
  def __len__(self) -> int:
    return len(self.__wordIds)

  def __hash__(self):
    return hash(self.__url)

  def __repr__(self):
    return "Page: %s (%d)" % (self.__url, len(self))

  def __eq__(self, value):
    if isinstance(value, Page):
      return ((self.get_name() == value.get_name())
      and (len(self) == len(value)))
    else:
      return False
