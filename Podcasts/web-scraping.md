# Episode 12: Web Scraping in Python: Tools, Techniques, and Legality
6/5/2020

https://realpython.com/podcasts/rpp/12/
[Kimberly Fessel](http://kimberlyfessel.com/)

- Natural Language Processing (NLP) - anytime working with text data and converting to numbers to be analyzed
    - Combine data from multiple sources to build a picture of customer journey - take info from search patterns and customer reviews and combining into a holistic picture - it did involve web scraping
- Tutorial by Dr. Fessel, "Officially Legal, Let's Scrape the Web"
- Computer Fraud and Abuse Act - used in many cases and possibly with scraping
    - Aimed at hacking behaviors in the 1980s
    - Law used for cyber bullying and viruses
    - Mirky areas with logging in with PW or someone elses PW
- Good projects w/ web scraping
    - Anything - info on the web
    - Tables of sports data, apartment rentals, various text data for NLP projects
    - Have access to all info on the Internet and able to collect in automated way
- Tool of choice
    - Python's request library to get HTML
    - Look at the page itself and use inspect (in the browser) to see what kind of HTML is creating the page
    - [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) for parsing
    - Get body of web page and then ingest into Beautiful Soup
    - Develop strategy to get text that you want
- Techniques for finding data elements that you want
    - Tricky b/c every website is different
    - Two main approaches:
        1. Looking for unique attributes (e.g., HTML IDs assigned to tags, classes). First thing to try is attributes.
        2. Navigate the DOM (i.e., divs, tree w/ parents and children).
* Real Python has request package tutorial. Request is a python package for requesting data through API and as a scraper.