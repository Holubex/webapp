import justpy as jp

from webapp1.home import Home
from webapp1.about import About

jp.Route(Home.path, Home.serve)
jp.Route(About.path, About.serve)



jp.justpy(port=8001)