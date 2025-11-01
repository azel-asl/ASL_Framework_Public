🌍 **The world’s first human-readable language for orchestrating AI agents — turning intent into structured, auditable behavior.**

# 🧠 ASL Framework v3.2  
**Agentic Spec Loop™ — A Human-Readable DSL for AI Agent Orchestration**  
© 2025 Erwin Layaoen | AZEL™ Studio | Patent Pending  

> **ASL (Agentic Spec Loop™)** is a plain-English **Domain-Specific Language (DSL)** for auditable AI workflows across any industry — built for non-coders to design, test, and automate multi-agent systems using readable, executable text blocks.

---

## 🔍 About This Repository
This repository hosts the official **ASL Core Syntax Language v3.2** reference implementation.  
ASL lets anyone design, test, and run **multi-agent LLM workflows** using simple readable blocks instead of code.  
Each `.asl` file describes how agents think, communicate, and pass data across a defined flow.

---

## 🚀 Quick Start (Hello Workflow Demo)

### 1️⃣ Open the Interpreter Prompt  
📄 [`docs/ASL_v3.2_InterpreterPrompt.txt`](docs/ASL_v3.2_InterpreterPrompt.txt)  
Copy the entire text into ChatGPT, Claude, or Gemini.  
This turns the model into an **ASL interpreter** that understands `::BLOCKS`, variables, and flows.

### 2️⃣ Run the Hello World Example  
📄 [`examples/hello_world.asl`](examples/hello_world.asl)  
Paste the file’s content into the same chat session.  
You’ll see each block execute in order and produce structured output.

---

## ✅ ASL Hello Workflow Result
```
Hello Raisa — I’m your AI Guide.  
ASL is a language for coordinating multiple AI agents through readable blocks instead of code.

Each block (::AGENT greet, ::AGENT explain) runs in sequence using the ::FLOW chain.  
Variables like {{user}} connect outputs between agents, and ::OUTPUT defines the final display.
```

---

## ⚙️ Core Language Blocks

| Block | Purpose |
|------|----------|
| `::META` | Program metadata (name, version, author) |
| `::INPUT` | Defines parameters and variables |
| `::AGENT` | Role + task definition for an AI agent |
| `::FLOW` | Execution order (`A → B → C`) |
| `::OUTPUT` | Final output formatting |
| `::ASL_CHECKSUM` | Integrity validation across execution logs |

---

## 🧠 Why ASL Matters
ASL provides a **universal, human-readable orchestration layer** for any domain—  
from trading bots and creative assistants to healthcare and enterprise automation.  
It abstracts complex code into transparent, auditable specs that LLMs can execute directly.

---

## 🧾 Licensing
**Free for research and educational use.**  
**Commercial use requires a license.**  
Contact `licensing@azelstudio.com` for terms.  
*(© 2025 Erwin Layaoen | AZEL™ Studio | Patent Pending)*

---

## 🧱 Version History
- **v3.2 — October 2025:** Formal EBNF spec, lexer/parser reference, runtime update, and Hello Workflow example.  
- Earlier versions (v1–v3.1) covered base syntax and EdgeEngine example logic.

---

## 🏷 Repository Tags
To mark official releases:
```bash
git tag -a v3.2 -m "Official ASL v3.2 reference release"
git push origin v3.2
```

---

## ⚖️ Patent Notice
Protected under U.S. Provisional Patent Applications (Filed Oct 28, 2025):  
- **ASL_Core_Syntax™** — “Block-Based Language for Agentic AI Workflows”  
- **ASL_HYPER™ Engine** — “Multi-Format Content Transformation Engine”  

Filed as a Continuation-in-Part (CIP) within the **Agentic Spec Loop™** patent family.  
No prior published system defines a plain-English, block-delimited, executable language for AI reasoning.

---

Created by: **Erwin Layaoen**  
Company: **AZEL™ Studio**  
🌐 [stan.store/ErwinLayaoen](https://stan.store/ErwinLayaoen) 📧 elayaoen@me.com  

> “ASL turns human reasoning into code-free, auditable AI execution — the missing language layer for the agentic era.”
