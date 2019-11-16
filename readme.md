E	
Implement a basic search engine that index all pages in the Wikipedia dataset (see Datasets page)
Search queries shall only contain single words
Results shall be ranked using the word frequency metric
The user shall input the search queries in a web client, and display the search results returned from the server
Display the top 5 search results with page and rank score
Implement the system using a REST web service where:
 1) client sends a request to a server
 2) the server responds with json data
 3) the json data is decoded and presented in a client GUI
C-D	
It shall be possible to use search queries of more than one word
Results shall be ranked using:
score = word_frequency + 0.8 * document_location
Display the top 5 search results with page and rank score
A-B	
Implement the PageRank algorithm and use it to rank the search results
Run the algorithm for 20 iterations
Results shall be ranked using:
score = word_frequency + 0.8 * document_location + 0.5 * pagerank
Display the top 5 search results with page and rank score