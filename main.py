import justpy as jp

from webapp1.home import Home
from webapp1.about import About
from webapp1.dictionary import Dictionary

jp.Route(Home.path, Home.serve)
jp.Route(About.path, About.serve)
jp.Route(Dictionary.path, Dictionary.serve)


jp.justpy(port=8001)