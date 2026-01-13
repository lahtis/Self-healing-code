from shl.middleman.base import Middleman

class MiddlemanManager:
    """
    Manages all registered Middleman instances.
    Responsible for selecting the correct Middleman for a given SHLComponent.
    """

    def __init__(self):
        self.middlemen = []

    # -------------------------
    # Registration
    # -------------------------
    def register(self, middleman: Middleman):
        """
        Register a Middleman instance.
        """
        self.middlemen.append(middleman)

    # -------------------------
    # Middleman selection
    # -------------------------
    def get_middleman_for(self, component):
        """
        Returns the first Middleman that supports the given component.
        """
        for m in self.middlemen:
            if m.supports(component):
                return m
        return None

    # -------------------------
    # Data → UI
    # -------------------------
    def to_component_value(self, component, data):
        """
        Converts raw data into a UI value using the appropriate Middleman.
        """
        middleman = self.get_middleman_for(component)
        if middleman:
            return middleman.to_component_value(component, data)
        return None

    # -------------------------
    # UI → Data
    # -------------------------
    def from_component_value(self, component, value):
        """
        Converts UI value back into Python data using the appropriate Middleman.
        """
        middleman = self.get_middleman_for(component)
        if middleman:
            return middleman.from_component_value(component, value)
        return value
