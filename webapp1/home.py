import justpy as jp

class Home:
    path = '/'

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        layout = jp.QLayout(a=wp, view="hHh lpR fFf")
        header = jp.QHeader(a=layout)
        toolbar = jp.QToolbar(a=header)

        drawer = jp.QDrawer(a=layout, show_if_above=True, v_mode='left', bordered=True)
        jp.QBtn(a=toolbar, dense=True, flat=True, round=True, icon='menu',
                click=cls.move_drawer, drawer=drawer)
        jp.QToolbarTitle(a=toolbar,text='Instant Dictionary')

        div = jp.Div(a=layout, classes="bg-white-200 h-screen")
        jp.Div(a=div, text='This is the Home Page!', classes='text-4xl m-2')
        jp.Div(a=div, text='''
                Aplikacia Dzefkoviteho typu
                ''', classes='flex justify-center items-center h-screen')
        return wp

    @staticmethod
    def move_drawer(widget, msg):
        if widget.drawer.value:
            widget.drawer.value = False
        else:
            widget.drawer.value = True
