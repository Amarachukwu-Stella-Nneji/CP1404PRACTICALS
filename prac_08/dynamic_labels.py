from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """DynamicLabelsApp is a Kivy App for creating labels."""

    def build(self):
        """Build the Kivy app."""
        layout = BoxLayout(orientation='vertical')
        names = ['Alice', 'Bob', 'Charlie', 'David']
        for name in names:
            label = Label(text=name)
            layout.add_widget(label)
        return layout


DynamicLabelsApp().run()
