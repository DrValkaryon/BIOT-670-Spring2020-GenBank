
from kivy.app import App
from kivy.uix.widget import Widget


class GenBanker(Widget):
    pass


class GenBanker(App):
    def build(self):
        return GenBanker()


if __name__ == '__Kivy_Main__':
    GenBanker().run()