Agentic AI Data Analysis Demo

Overview

This project demonstrates a schema-driven, tool-using LLM agent that analyzes structured data safely and transparently.
The agent accepts natural-language questions, decides on an appropriate action, executes controlled data queries, and returns explainable, trustworthy results.

The design mirrors how modern data intelligence platforms (like Alation) apply AI agents on top of structured enterprise data.

⸻

Key Capabilities
	•	Agentic decision-making
Natural language → action selection (run_query, inspect_schema, refuse)
	•	Schema awareness
The agent reasons strictly within a profiled dataset schema
	•	Safe tool execution
Read-only SQL queries enforced against a known table
	•	Explainability by design
Every answer includes:
	•	Method (how it was computed)
	•	Data usage
	•	Data quality caveats
	•	Hallucination resistance
Invalid or unsupported questions are refused with context

⸻

Dataset
	•	Source: MapleStory monster statistics (CSV)
	•	Rows: 7,260
	•	Table name: data
	•	Example columns:
	•	name
	•	level
	•	exp
	•	boss
	•	HP, MP
	•	exp_div_hp

The dataset intentionally includes missing values and duplicates to surface real-world data quality considerations.

⸻

User Question
   ↓
Schema Validation (hard guardrail)
   ↓
LLM Decision Layer
   ↓
Tool Execution (SQL / metadata)
   ↓
Results + Explainability

Core Components
	•	schema.py – authoritative dataset metadata
	•	tools.py – controlled execution tools
	•	llm.py – LLM reasoning (decision + SQL generation)
	•	agent.py – orchestration, validation, enforcement
	•	explain.py – explainability metadata generation