# Excel Input Data Structure

## Purpose
This Excel file contains detailed sales data provided by different departments.
The data is processed automatically to generate management reports.

---

## Sheet Name
SalesData

---

## Required Columns

| Column Name       | Type     | Required | Description |
|------------------|----------|----------|-------------|
| TransactionID    | Text     | Yes      | Unique transaction identifier |
| TransactionDate  | Date     | Yes      | Date of sale |
| Department       | Text     | Yes      | Department name |
| SalesPerson      | Text     | Yes      | Sales representative |
| ClientID         | Text     | Yes      | Client identifier |
| ClientName       | Text     | Yes      | Client name |
| Product          | Text     | Yes      | Product or service name |
| Quantity         | Integer  | Yes      | Number of units sold |
| UnitPrice        | Decimal  | Yes      | Price per unit |
| Amount           | Decimal  | Yes      | Quantity × UnitPrice |
| Currency         | Text     | Yes      | PLN, EUR, USD |

---

## Optional Columns

| Column Name     | Type    | Description |
|-----------------|---------|-------------|
| Category        | Text    | Product category |
| PaymentMethod   | Text    | Payment type |
| InvoiceNumber   | Text    | Invoice reference |
| Country         | Text    | Client country |
| Notes           | Text    | Additional comments |

---

## Validation Rules

- All required columns must be present
- Quantity must be greater than 0
- UnitPrice must be greater or equal to 0
- Amount must equal Quantity × UnitPrice
- TransactionDate cannot be in the future
- Currency must be one of: PLN, EUR, USD
- TransactionID must be unique within the file

---

## Input Sources

The system supports two Excel input sources:
1. Local file from a predefined directory
2. Excel file received as an email attachment

---

## Error Handling

If validation fails:
- The file is rejected
- No report is generated
- An email with validation errors is sent
