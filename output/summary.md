## ERPNext Sales Invoice – Analysis Summary

Sales Invoice is a core financial document in ERPNext
responsible for customer billing and accounting impact.

Key findings:
- Business logic is concentrated in the SalesInvoice class
- Validation rules are implemented inside validate() methods
- Conditional logic handles taxes, discounts, and posting rules

Why this matters:
Sales Invoice directly affects revenue, tax compliance,
and financial reporting. Any modernization effort must
preserve this logic accurately.
