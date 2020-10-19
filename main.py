from webCrawler import WebCrawler

url = "www.columbia.edu/~fdc/sample.html"
port = 80

w = WebCrawler(url, port)

w.getContent()
