from abc import ABC, abstractmethod

class Middleman(ABC):
    """
    Middleman is an adapter layer between raw data and SHL UI components.
    It transforms complex Python objects into values that UI components
    can display or use.
    """

    @abstractmethod
    def supports(self, component):
        """
        Returns True if this middleman can handle the given SHLComponent.
        Example: A UserMiddleman may support TEXT_INPUT and DROPDOWN.
        """
        pass

    @abstractmethod
    def to_component_value(self, component, data):
        """
        Converts raw data into a value suitable for the given component.
        Example:
            - Convert a User object into a string for a TEXT_INPUT
            - Convert a list of objects into dropdown options
        """
        pass

    @abstractmethod
    def from_component_value(self, component, value):
        """
        Converts a UI value back into a Python data structure.
        Useful for forms, saving, validation, etc.
        """
        pass
