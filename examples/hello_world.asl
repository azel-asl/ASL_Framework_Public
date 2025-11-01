::META
Name: "Hello Workflow"
Version: "v3.2"
Author: "Erwin Layaoen"
Description: "A minimal ASL demo showing how multiple agents interact using ::FLOW and variables."
::END

::INPUT
user: "Raisa"
goal: "understand what ASL does"
::END

::AGENT greet
role: "Guide"
task: |
  Greet {{user}} warmly and explain in one short paragraph that ASL is a language
  for describing how AI agents talk to each other using readable ::BLOCKs instead of code.
output: markdown
::END

::AGENT explain
role: "Teacher"
task: |
  Expand on {{greet}} by describing how each ::BLOCK acts as a function.
  Explain that ::FLOW defines the execution order, and {{variables}} link agent outputs together.
output: markdown
::END

::FLOW
chain: "greet -> explain"
::END

::OUTPUT
format: "markdown"
template: |
  ## ✅ ASL Hello Workflow Result
  {{greet}}

  {{explain}}

  ---
  _Generated automatically using the ASL v3.2 mini-interpreter_
::END

::ASL_CHECKSUM
::END
