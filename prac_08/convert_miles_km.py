from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesConverter(App):
    """MilesConverter is a Kivy App for converting distance from miles to kilometers."""
    miles_text = StringProperty()

    def build(self):
        """Build and initialize the Kivy app."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_m_km_solution.kv')
        return self.root

    def get_valid_miles(self):
        """Get valid miles."""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0

    def handle_increment(self, change):
        """Handle increment."""
        value = self.get_valid_miles() + change  # change can be 1 for increase or -1 for decrease.
        self.root.ids.input_miles.text = str(value)
        self.handle_calculation()

    def handle_calculation(self):
        """Handle calculation."""
        value = self.get_valid_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)


MilesConverter().run()
