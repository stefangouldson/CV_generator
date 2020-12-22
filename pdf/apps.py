from django.apps import AppConfig
import pdfkit

pdfkit.from_string("hello world", "string.pdf")

class PdfConfig(AppConfig):
    name = 'pdf'
