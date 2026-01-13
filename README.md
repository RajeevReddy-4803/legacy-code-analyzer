# Legacy Code Analyzer – ERPNext Sales Invoice

## What This Project Does
This project is a simple code intelligence tool that
extracts classes and functions from a legacy enterprise
codebase.

## Why This Matters
Legacy systems contain critical business logic that is
often undocumented. Understanding this logic is essential
before modernization or migration.

## Target System
ERPNext – Sales Invoice module

## How to Run
```bash
python src/analyzer.py erpnext/accounts/doctype/sales_invoice/
```

Output

output/entities.json – extracted entities

output/summary.md – business understanding

Learnings

Most ERPNext business rules are embedded directly in code
rather than documentation.
