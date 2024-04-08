import inspect

import justpy as jp

from webapp1.home import Home
from webapp1.about import About
from webapp1.dictionary import Dictionary
from webapp1 import page


imports = list(globals().values())

for obj in imports:
    if inspect.isclass(obj):
        if issubclass(obj, page.Page) and obj is not page.Page:
            jp.Route(obj.path, obj.serve)


# jp.Route(Home.path, Home.serve)
# jp.Route(About.path, About.serve)
# jp.Route(Dictionary.path, Dictionary.serve)


jp.justpy(port=8001)