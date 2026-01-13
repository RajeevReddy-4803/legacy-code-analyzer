# 🧠 Engineering Reflection

## 🚀 Strategic Learnings
This project reinforced that **source code is the ultimate source of truth** in enterprise environments.

### 1. The Value of Legacy
Legacy code is often viewed as a liability. However, this analysis revealed it as a **proven asset**:
*   It handles edge cases that new specifications often miss.
*   It encodes "tribal knowledge" about business operations that exists nowhere else.

### 2. Discovery over Assumption
The tool revealed unexpected complexity in `validate()` methods.
*   *Initial Assumption*: Validation is simple data checking.
*   *Reality*: Validation in ERPNext drives defining business processes (e.g., auto-creating assets, managing stock levels).

## ⚡ Technical Challenges & Solutions

| Challenge | Impact | Resolution |
| :--- | :--- | :--- |
| **Domain Complexity** | High cognitive load when traversing financial logic. | Focused analysis on "Entity" extraction (`Class`/`Function`) to map the high-level topology first. |
| **Volume of Code** | Determining what is vital vs. utility. | Prioritized the `SalesInvoice` class as the "Root Aggregate" for the domain. |

## 🔮 Future Roadmap
To further enhance business intelligence:
1.  **Dependency Graphing**: Visualizing call chains to identify "hot spots" of activity.
2.  **Rule Extraction**: Using AST parsing to isolate `if/else` clusters representing decision trees.
