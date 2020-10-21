import argparse

from webCrawler import WebCrawler


argParser = argparse.ArgumentParser()
argParser.add_argument('--url', type=str, required=True,
                        help='Página a ser varrida')
argParser.add_argument('--port', type=int, required=False, default=80,
                        help='Porta de acesso')

args = argParser.parse_args()

w = WebCrawler(args.url, args.port)

w.getContent()
