*As an initial warning, this is the first time that I have ever made anything in Python. Do not expect miracles.*

## Assignment Checklist
### E
1. ~~Implement a basic search engine that index all pages in the Wikipedia dataset~~
2. ~~Search queries shall only contain single words~~
3. ~~Results shall be ranked using the word frequency metric~~
4. ~~The user shall input the search queries in a web client, and display the search results returned from the server~~
5. ~~Display the top 5 search results with page and rank score~~
6. Implement the system using a REST web service where:
    1. ~~client sends a request to a server~~
    2. ~~the server responds with json data~~
    3. ~~the json data is decoded and presented in a client GUI~~
### C-D
1. ~~It shall be possible to use search queries of more than one word~~
2. ~~Results shall be ranked using: score = word_frequency + 0.8 * document_location~~
3. ~~Display the top 5 search results with page and rank score~~
### A-B
1. ~~Implement the PageRank algorithm and use it to rank the search results~~
2. ~~Run the algorithm for 20 iterations~~
3. ~~Results shall be ranked using: Score = word_frequency + 0.8 * document_location + 0.5 * pagerank~~
4. ~~Display the top 5 search results with page and rank score~~

### GUI Appearance & Execution Examples
> Note: While I am no designer by any means, this GUI could have been made prettier with more time. You said that appearance does not matter, and this fulfils all functional requirements so I deem it as "good enough", but no more than that.

> Furthermore, the performance is not optimized. The final version that I show during the exam may differ if I find the time to do more optimization.

#### Single-word query: "nintendo"
![Single-word query: "nintendo"](https://i.gyazo.com/95446babacc07d96e55533136b86dd28.png)

### Single word query: "c++"
![Single word query: "c++"](https://i.gyazo.com/4c65992721b3e86e072c7762ca9b91b5.png)

#### Multi-word query: "java programming"
![Multi-word query: "java programming"](https://i.gyazo.com/417a3f51b8c543e10b8f48fb2d0bd243.png)

#### Multi-word query: "super mario"
![Multi-word query: "super mario"](https://i.gyazo.com/f97feae5c81615178268fc8f31276978.png)