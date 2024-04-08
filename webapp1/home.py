import justpy as jp
from webapp1 import layout

class Home:
    path = '/'

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)

        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-white-200 h-screen")
        jp.Div(a=div, text='This is the Home Page!', classes='text-4xl m-2')
        jp.Div(a=div, text='''
                Aplikacia Dzefkoviteho typu
                ''', classes='flex justify-center items-center h-screen')
        return wp