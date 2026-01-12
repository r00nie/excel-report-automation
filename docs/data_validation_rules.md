# Data Validation Rules for Excel Input Files

This document defines validation rules for Excel input files used in the Excel Report Automation project. The rules apply to all Excel files regardless of their source (local file or email attachment).

## 1. Required Columns Validation

### 1.1 Required worksheet
- The Excel file **must** contain a worksheet named `SalesData`.
- Missing worksheet results in a critical validation error and stops further processing.

### 1.2 Required columns
The `SalesData` worksheet must contain all of the following columns:
- TransactionID
- TransactionDate
- Department
- SalesPerson
- ClientID
- ClientName
- Product
- Category
- Quantity
- UnitPrice
- Amount
- Currency
- PaymentMethod
- InvoiceNumber
- Country
- Notes

### 1.3 Validation behavior
- Missing one or more required columns → **validation fails**
- Processing is stopped immediately
- Additional (unexpected) columns are allowed and ignored

### 1.4 Error reporting
- List of missing columns
- Error type: `STRUCTURE_ERROR`

## 2. Data Type Validation

Data type validation is performed row by row for all records in the worksheet.

### 2.1 Expected data types

| Column | Expected Type | Additional Rules |
|------|--------------|------------------|
| TransactionID | string | valid UUID |
| TransactionDate | date | valid date |
| Department | string | non-empty |
| SalesPerson | string | non-empty |
| ClientID | string | non-empty |
| ClientName | string | non-empty |
| Product | string | non-empty |
| Category | string | non-empty |
| Quantity | integer | > 0 |
| UnitPrice | float | > 0 |
| Amount | float | > 0 |
| Currency | string | enum |
| PaymentMethod | string | non-empty |
| InvoiceNumber | string | non-empty |
| Country | string | non-empty |
| Notes | string | nullable |

### 2.2 Null and empty value rules
- `null` / `NaN` values are **not allowed** in critical fields
- `Notes` field may be empty or null

**Critical fields:** TransactionID, TransactionDate, Department, Quantity, UnitPrice, Amount, Currency

### 2.3 Validation behavior
- Invalid data type results in a validation error
- Validation continues for all rows
- All errors are collected into a single validation report

### 2.4 Error reporting
Each error should include:
- Row number (Excel row index)
- Column name
- Invalid value
- Expected data type
- Error type: `TYPE_ERROR`

## 3. Business Rules Validation

Business rules ensure logical and domain-specific correctness of the data.

### 3.1 Allowed values (ENUM)
**Department:** Sales, IT, HR, Finance, Marketing  
**Currency:** PLN, EUR, USD

### 3.2 Numeric business rules
- Quantity must be greater than 0
- UnitPrice must be greater than 0
- Amount must be greater than 0

### 3.3 Amount calculation rule
- Amount = Quantity * UnitPrice
- Allowed tolerance: ±0.01
- Difference greater than tolerance results in a validation error

### 3.4 Date consistency
- TransactionDate must not be a future date

### 3.5 Validation behavior
- Each violated rule produces a separate validation error
- Data is not processed further if any business rule fails
- All errors are aggregated into a validation report

### 3.6 Error reporting
Each error should include:
- Row number
- Violated rule description
- Error type: `BUSINESS_RULE_ERROR`

## 4. Validation Execution Order
Validation is executed in the following order:
1. Required columns validation  
2. Data type validation  
3. Business rules validation  

Rules:
- If step 1 fails, validation stops immediately
- If steps 2 or 3 fail, a validation report is generated
- Data is accepted only if all validation steps pass successfully

## 5. Definition of Done
The validation rules are considered complete when:
- All rules are clearly defined and documented
- Rules are independent of data source (local file or email)
- The document can be directly used to implement a Python data validator
