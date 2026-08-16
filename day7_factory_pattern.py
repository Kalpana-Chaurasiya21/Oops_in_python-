# Factory Method Pattern
# Provides an interface for creating objects in a superclass, but allows
# subclasses or factory functions to alter the type of objects that will be created.
# Eliminates messy conditional instantiation (e.g., if type == "pdf": return PDFExporter()).

from abc import ABC, abstractmethod


#  Product Interface 
class DocumentExporter(ABC):
    @abstractmethod
    def export(self, content: str) -> str:
        pass


#  Concrete Products 
class PDFExporter(DocumentExporter):
    def export(self, content: str) -> str:
        return f"[PDF Format] Rendering PDF document with content: '{content}'"


class CSVExporter(DocumentExporter):
    def export(self, content: str) -> str:
        return f"[CSV Format] Converting to comma-separated values: '{content}'"


class JSONExporter(DocumentExporter):
    def export(self, content: str) -> str:
        return f"[JSON Format] {{\n  \"data\": \"{content}\"\n}}"


#  Factory Class 
class ExporterFactory:
    """Central factory for managing object creation."""
    
    _exporters = {
        "pdf": PDFExporter,
        "csv": CSVExporter,
        "json": JSONExporter
    }

    @classmethod
    def get_exporter(cls, format_type: str) -> DocumentExporter:
        exporter_class = cls._exporters.get(format_type.lower())
        if not exporter_class:
            raise ValueError(f"Unsupported export format: '{format_type}'. Available: {list(cls._exporters.keys())}")
        return exporter_class()


#  Example Usage 

print("# --- Factory Pattern Demonstration ---")

report_data = "Quarterly Revenue Statistics 2026"

# Request exporters dynamically based on runtime parameters (e.g., user input or API config)
for fmt in ["pdf", "json", "csv"]:
    exporter = ExporterFactory.get_exporter(fmt)
    print(exporter.export(report_data))