class FormEngine:
    """
    FormEngine orchestrates:
        - SHLComponent creation
        - UI widget creation via UIAdapter
        - Localization via LanguageManager
        - Data transformation via MiddlemanManager

    It is the glue layer that builds dynamic forms from SHL components.
    """

    def __init__(self, adapter, language_manager, middleman_manager):
        self.adapter = adapter
        self.language_manager = language_manager
        self.middleman_manager = middleman_manager

        # Stores mapping: component_id → widget instance
        self.widgets = {}

    # -------------------------
    # Form creation
    # -------------------------
    def create_component(self, component):
        """
        Creates a UI widget for the given SHLComponent and stores it.
        """
        widget = self.adapter.create_widget(component)
        self.widgets[component.component_id] = widget
        return widget

    def create_form(self, components):
        """
        Creates a full form from a list of SHLComponent objects.
        Returns a dict: {component_id: widget}
        """
        form = {}
        for comp in components:
            form[comp.component_id] = self.create_component(comp)
        return form

    # -------------------------
    # Data → UI
    # -------------------------
    def fill_form(self, data, components):
        """
        Uses MiddlemanManager to fill UI widgets with data.
        """
        for comp in components:
            widget = self.widgets.get(comp.component_id)
            if not widget:
                continue

            value = self.middleman_manager.to_component_value(comp, data)
            if value is None:
                continue

            # Apply value depending on widget type
            if hasattr(widget, "setText"):
                widget.setText(str(value))
            elif hasattr(widget, "value"):
                widget.value = value
            elif hasattr(widget, "options"):
                widget.options = value

            # Framework-specific update
            if hasattr(widget, "update"):
                widget.update()

    # -------------------------
    # UI → Data
    # -------------------------
    def extract_form_data(self, components):
        """
        Reads values from UI widgets and converts them back to Python data.
        """
        result = {}

        for comp in components:
            widget = self.widgets.get(comp.component_id)
            if not widget:
                continue

            # Extract raw value
            if hasattr(widget, "text"):
                raw = widget.text()
            elif hasattr(widget, "value"):
                raw = widget.value
            else:
                raw = None

            # Convert via Middleman
            converted = self.middleman_manager.from_component_value(comp, raw)
            result[comp.component_id] = converted

        return result

    # -------------------------
    # Language refresh
    # -------------------------
    def refresh_language(self, components):
        """
        Reapplies localization to all widgets.
        """
        for comp in components:
            widget = self.widgets.get(comp.component_id)
            if widget:
                self.adapter.refresh_widget(widget, comp)
