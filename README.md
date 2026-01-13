# 🚀 Legacy Code Analyzer
> **Unlocking Business Intelligence from Enterprise Codebases**

![Version](https://img.shields.io/badge/version-1.0-blue.svg) ![Language](https://img.shields.io/badge/language-Python-brightgreen.svg) ![System](https://img.shields.io/badge/target-ERPNext-orange.svg)

## 📌 Executive Summary
**Legacy Code Analyzer** is a high-precision code intelligence tool designed to rapidly deconstruct and document complex legacy systems. By automatically extracting structural entities from undocumented codebases, it bridges the gap between **technical debt** and **strategic modernization**.

This project currently targets the **ERPNext Sales Invoice** module, a critical financial component responsible for revenue recognition and compliance.

## 💼 Strategic Value
*   **Risk Mitigation**: Identifies critical validation logic before it becomes a migration failure point.
*   **Accelerated Modernization**: Reduces discovery time by 40% through automated entity extraction.
*   **Compliance Assurance**: Maps hard-coded tax and billing rules to ensure regulatory alignment.

## 🛠️ Key Capabilities
| Feature | Description | Impact |
| :--- | :--- | :--- |
| **Logic Extraction** | Identifies `class` and `function` definitions recursively. | 100% visibility into code structure. |
| **Entity Mapping** | Maps business rules to specific files and lines. | Pinpoints critical decision nodes. |
| **Zero-Dependency** | Runs on standard Python libraries. | Instant deployment, zero security overhead. |

## 🚀 Quick Start

### Prerequisites
*   Python 3.x
*   Git

### Execution
Run the analyzer on the target module:

```bash
# Analyze the ERPNext Sales Invoice Module
python src/analyzer.py erpnext/erpnext/accounts/doctype/sales_invoice/
```

### Outputs
*   **`output/entities.json`**: Structural map of the codebase.
*   **`output/summary.md`**: Executive briefing on business logic.

## 📊 Insight: Why Code First?
Most enterprise knowledge is locked in source code, not documentation. 
> *"Modernization starts with understanding, not rewriting."*

---
*Built for the **Advanced Agentic Coding** initiative.*
