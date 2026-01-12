# Źródła plików Excel dla projektu Excel Report Automation

## 1. Plik lokalny
- Ścieżka: `examples/sales_data.xlsx`
- Excel generowany skryptem `python-service/app/generate_excel.py`
- Dane testowe dla różnych departamentów (Sales, IT, HR, Finance, Marketing)
- Zawiera kolumny:
  - TransactionID, TransactionDate, Department, SalesPerson, ClientID, ClientName
  - Product, Category, Quantity, UnitPrice, Amount, Currency
  - PaymentMethod, InvoiceNumber, Country, Notes

## 2. Załącznik email
- Format: Excel (.xlsx)
- Wysyłany na skrzynkę projektową
- Automatycznie pobierany przez workflow n8n
- Excel powinien mieć kolumny zgodne z lokalnym plikiem
