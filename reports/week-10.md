# Semester Week 10 Progress Report

## Completed Work
Forked the instructor repository to my account and cloned it locally. Chose level C and the project topic: Course Deadlines Assistant, an LLM agent with tools. Wrote the full project proposal: problem, target users, functions, agent tools, architecture, example requests, evaluation plan and milestones for Weeks 10-17. Selected the model (OpenAI API, gpt-6-luna) and set up .env.example with .env excluded by .gitignore.

## Important Commits

- Commit hash: edb9af1
- Description: Add project proposal (reports/proposal.md)
- Link: https://github.com/amanzhol10/css4007-ai-agents-final/commit/HASH

## Current Functionality

The application code is not implemented yet. The repository is forked, the proposal passes the npm run proposal check, and the planned tools (get_course_info, list_deadlines, days_until) and the agent architecture are specified.

## Problems Encountered

npm run proposal reported that Selected Difficulty must begin with D, C, or A even though the field contained the letter C. Also, several OpenAI models I first considered turned out to be deprecated.

## Solutions

I read the validation script and found that it requires a Latin letter; the character I typed was the Cyrillic C from the Russian keyboard layout. Retyping it with the English layout fixed the check. For the model I checked the current OpenAI model list and chose gpt-6-luna instead of deprecated models.

## What I Learned

How LLM tool calling works: the model receives tool schemas, chooses a tool and arguments, my code validates and executes it, and the result goes back to the model for the final answer. I also learned why date arithmetic should be done by a tool and why tests should use a mocked LLM client instead of real API calls.

## Next Week

Set up the development environment, connect the OpenAI API with the key from .env, make the first working LLM request, add basic documentation in the README, and commit the working prototype.
