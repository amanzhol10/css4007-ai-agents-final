# Project Proposal — Semester Week 10

## Project Title

Course Deadlines Assistant: an LLM agent with tools

## Problem Description

Students have to look up course information (credits, exam dates, deadlines) across several places and calculate remaining time by hand. The application answers such questions in natural language. The LLM decides which tool to call, the tool returns data, and the answer is built from that data. This is important because it saves time and reduces missed deadlines, and the answers are grounded in real data instead of model guesses.

## Target Users

University students who need quick answers about their courses, exams and deadlines.

## Selected Difficulty

C

## Expected Functionality

- Answer questions about a course: title, credits, exam date.
- List the deadlines of a course.
- Calculate how many days remain until a date.
- Return a clear message when a course does not exist.
- Validate tool arguments before execution.
- Log every tool call with its arguments and result.

## Proposed Functions

1. get_course_info(course_id: str) -> dict
   Purpose: return title, credits and exam date of a course.
   Input: course ID, for example "AI101".
   Output: dict with title, credits, exam_date, or {"error": "Course not found"}.
   Dependencies: local JSON file data/courses.json.

2. list_deadlines(course_id: str) -> dict
   Purpose: return all deadlines of a course in chronological order.
   Input: course ID.
   Output: dict with a list of dates, or an error.
   Dependencies: local JSON file data/courses.json.

3. days_until(date: str) -> dict
   Purpose: calculate days from today to a given date.
   Input: date in YYYY-MM-DD format.
   Output: dict with the number of days, or an error for an invalid date.
   Dependencies: Python datetime module.

4. validate_arguments(tool_name: str, args: dict) -> bool
   Purpose: check tool arguments before execution.
   Input: tool name and arguments from the LLM.
   Output: True, or an exception with a clear message.
   Dependencies: tool schemas.

5. run_agent(user_question: str) -> str
   Purpose: main loop: send the question to the LLM, execute requested tools, return the final answer.
   Input: user question.
   Output: answer text.
   Dependencies: LLM client, tools, logger.
## Proposed Agent Tools

Exposed to the LLM: get_course_info, list_deadlines, days_until.
- get_course_info: the model cannot know real course data, so it must fetch it.
- list_deadlines: needed for questions about deadlines of a course.
- days_until: LLMs make mistakes in date arithmetic and do not know today's date, so a tool gives an exact result.
validate_arguments and run_agent are internal and are not exposed to the LLM.

## Model Selection

OpenAI API, model gpt-6-luna (GPT-6 Luna, small cost-efficient model with function calling support). The agent calls the API with tool schemas; the API key is read from the OPENAI_API_KEY environment variable. Automated tests use a mocked LLM client, so they do not call the API.

## Architecture

User question
   -> run_agent
   -> LLM (receives question and tool schemas)
   -> LLM requests a tool call (name + arguments)
   -> validate_arguments
   -> tool execution (get_course_info / list_deadlines / days_until)
   -> logger records the call and result
   -> tool result returned to the LLM
   -> LLM writes the final answer
   -> Answer to the user

## Example Requests

1. "When is the AI101 exam?" -> get_course_info("AI101")
2. "How many days until the next deadline in ML201?" -> list_deadlines("ML201"), then days_until(date)
3. "How many credits does CS999 have?" -> get_course_info("CS999") returns an error, the answer says the course was not found

## Evaluation Plan

At least 8 automated tests with a mocked LLM client: tool selection for each tool, argument validation (missing and wrong-type arguments), unknown course, invalid date, tool error handling, final answer uses tool result, logging of every call. Plus a manual check with the real model on the three example requests.

## Weekly Milestones

Week 10: fork, proposal, repository setup.
Week 11: connect the LLM, first working request, README.
Week 12: implement get_course_info, list_deadlines, days_until; data file; first tests.
Week 13: LLM tool selection and real tool execution.
Week 14: complete tool-calling workflow, tool error handling.
Week 15: argument validation, failure handling, logging, more tests.
Week 16: run the full test suite, record results, fix failures, update docs.
Week 17: final README, AI usage statement, demonstration and defense.

For each function give its name, purpose, inputs, outputs, and dependencies. For C/A identify model-callable tools and their purpose; D may write “Not applicable — D level”. Give at least three example requests and milestones for Weeks 10–17.
