Processing ASL v3.2 Workflow — “Hello Workflow”

> Generated automatically using the ASL v3.2 mini-interpreter

---

## 📋 Parsing Blocks

**META**
- Name: Hello Workflow  
- Version: v3.2  
- Author: Erwin Layaoen

**INPUT**
- user: "Raisa"  
- goal: "understand what ASL does"

**FLOW**
- Execution chain: `greet → explain`

---

## ⚙️ Executing Agents

### 🤖 Agent `greet`
**Role:** Guide

Hi Raisa! **ASL (Agentic Spec Language)** is a human-readable way to describe how AI agents collaborate and pass information. Instead of code, you use simple `::BLOCK` syntax to define agents, their roles, tasks, and how data flows—making multi-agent workflows easy to design and audit.

---

### 🤖 Agent `explain`
**Role:** Teacher

Each `::BLOCK` has a purpose. `::AGENT` blocks define roles and tasks; the `::FLOW` block orchestrates execution (sequence, parallel, or conditional). The `{{variable}}` system lets outputs from one agent (e.g., `{{greet}}`) feed others automatically, creating a clean, no-code data pipeline.

---

## ✅ Final Output

Hi Raisa! **ASL (Agentic Spec Language)** is a human-readable way to describe how AI agents collaborate and communicate. You define agents, roles, tasks, and flows with `::BLOCKS`. The `::FLOW` chain (here, `greet → explain`) runs agents in order, and `{{variables}}` pass results between them, enabling powerful, transparent multi-agent systems that are easy to maintain.
