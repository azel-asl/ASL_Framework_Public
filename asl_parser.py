# ===========================================================
# ASL Parser and Runtime v3.2 — Reference Implementation
# © 2025 Erwin Layaoen | AZEL™ Studio | Patent Pending
# ===========================================================

import re, hashlib, json
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Callable

@dataclass
class Block:
    name: str
    attributes: Dict[str, Any] = field(default_factory=dict)
    body: List[Any] = field(default_factory=list)

class ASLLexer:
    def __init__(self, source: str):
        self.source = source.splitlines()
        self.tokens = []
    def tokenize(self):
        for line in self.source:
            if line.strip().startswith("::"):
                self.tokens.append(("BLOCK", line.strip()))
            elif ":" in line:
                key, val = line.split(":", 1)
                self.tokens.append(("ATTR", (key.strip(), val.strip())))
            else:
                self.tokens.append(("TEXT", line.strip()))
        return self.tokens

class ASLParser:
    def __init__(self, tokens): self.tokens = tokens
    def parse(self) -> List[Block]:
        blocks, current = [], None
        for ttype, value in self.tokens:
            if ttype == "BLOCK" and value.startswith("::END"):
                if current: blocks.append(current); current = None
            elif ttype == "BLOCK":
                current = Block(name=value.replace("::", ""), attributes={}, body=[])
            elif ttype == "ATTR" and current:
                k, v = value
                current.attributes[k] = v
            elif current:
                current.body.append(value)
        return blocks

class ASLRuntime:
    def __init__(self, llm_provider: Optional[Callable] = None):
        self.llm = llm_provider
        self.state = {}
        self.log = []
    def execute(self, blocks: List[Block]):
        for block in blocks:
            self.log.append(f"Executing {block.name}")
            if block.name == "OUTPUT":
                print("\n".join(block.body))
            if "task" in block.attributes and self.llm:
                prompt = block.attributes["task"]
                self.state[block.name] = self.llm(prompt)
        checksum = hashlib.sha256("".join(self.log).encode()).hexdigest()
        print(f"[Checksum] {checksum[:16]}")

class ASL:
    @staticmethod
    def run(source: str, llm: Optional[Callable] = None):
        lexer = ASLLexer(source)
        parser = ASLParser(lexer.tokenize())
        blocks = parser.parse()
        runtime = ASLRuntime(llm)
        runtime.execute(blocks)
        return runtime.state

if __name__ == "__main__":
    demo = """
::META
Name: Demo
::END
::OUTPUT
Hello from ASL v3.2
::END
"""
    ASL.run(demo)
