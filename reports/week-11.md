# Semester Week 11 Progress Report

## Completed Work

Set up the Python environment with a virtual environment and requirements.txt. Integrated the OpenAI API (model gpt-6-luna) with the key loaded from .env. Implemented src/llm_client.py with an ask() function and src/main.py as the command-line entry point. Made the first successful request and verified error handling for a missing key and an invalid key. Added setup and usage documentation to README.md.

## Important Commits

- Commit hash: 3468491
- Description: Add first working LLM request with error handling
- Link: https://github.com/amanzhol10/css4007-ai-agents-final/commit/HASH1

- Commit hash: 0cda8e3
- Description: Document setup and usage
- Link: https://github.com/amanzhol10/css4007-ai-agents-final/commit/HASH2

## Current Functionality

The program takes a question from the command line, sends it to the LLM and prints the answer. Missing configuration, API failures and empty answers produce a clear error message instead of a crash. The model does not use tools yet, so it cannot know real course data.

## Problems Encountered

The first pip install in the new virtual environment appeared to hang and was interrupted with a keyboard interrupt, so no packages were installed.

## Solutions

I re-ran the installation with python -m pip install -r requirements.txt and waited for the first slow start to finish, then verified the imports.

## What I Learned

How the chat completions request is built from a system and a user message, why secrets are loaded from environment variables, and why all API errors are wrapped into one custom exception so the rest of the application handles failures in one place.

## Next Week

Implement the main project functions: the course data file, get_course_info, list_deadlines and days_until, with input validation and the first tests.
