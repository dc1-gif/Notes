from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label


class Main(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=10, spacing=10, **kwargs)
        self.lists = {"game": [], "shopping": [], "book": []}

        self.spinner = Spinner(text="game", values=list(self.lists),
                               size_hint_y=None, height=120)
        self.entry = TextInput(hint_text="items separated by commas",
                               multiline=False, size_hint_y=None, height=120)
        add_btn = Button(text="Add", size_hint_y=None, height=120)
        done_btn = Button(text="Done (remove)", size_hint_y=None, height=120)
        self.output = Label(text="", halign="left", valign="top")
        self.output.bind(size=lambda w, s: setattr(w, "text_size", s))

        add_btn.bind(on_press=self.add)
        done_btn.bind(on_press=self.done)

        for w in (self.spinner, self.entry, add_btn, done_btn, self.output):
            self.add_widget(w)

    def items(self):
        return [i.strip() for i in self.entry.text.split(",") if i.strip()]

    def add(self, *args):
        self.lists[self.spinner.text].extend(self.items())
        self.entry.text = ""
        self.show()

    def done(self, *args):
        current = self.lists[self.spinner.text]
        missing = []
        for item in self.items():
            if item in current:
                current.remove(item)
            else:
                missing.append(item)
        self.entry.text = ""
        self.show(f"Not in list: {', '.join(missing)}" if missing else "")

    def show(self, msg=""):
        text = "\n".join(f"{k}: {v}" for k, v in self.lists.items())
        self.output.text = text + ("\n\n" + msg if msg else "")


class ListApp(App):
    def build(self):
        return Main()


ListApp().run()
