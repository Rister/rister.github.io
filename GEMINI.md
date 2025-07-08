<!--
This file helps Gemini understand your project's context.
By providing structured information, you can guide Gemini to give more relevant and accurate responses.
You can include details about your project's goals, coding style, and important commands.
-->

# Gemini Project Configuration

This document provides guidelines and context for Gemini when assisting with this project.

## Project Overview

<!--
Describe your project here. What are its goals? What is the target audience?
This helps Gemini understand the bigger picture and provide more relevant assistance.
-->

This is a personal blog and portfolio website built with Pelican, a static site generator in Python.

## Coding Style and Conventions

<!--
Specify your coding style and conventions here. For example:
- Use black for Python code formatting.
- Follow PEP 8 guidelines.
- Use a specific naming convention for variables and functions.
-->

- Use `uv` for python project and dependency management.
- Use `ruff` for Python code formatting and linting, with extensive rules for PEP-8, docstrings, isort, etc.
- Follow PEP 8 guidelines.

## Important Commands

<!--
List frequently used commands for your project here. For example:
- `npm install`: Install dependencies
- `npm test`: Run tests
- `npm run build`: Build the project

This helps Gemini quickly execute common tasks.
-->

- `uv sync`: Install/sync project dependencies.
- `uv run ruff check .`: Run linting checks.
- `uv run ruff format .`: Format code.
- `pelican content -s pelicanconf.py`: Build the site
- `pelican content -s publishconf.py`: Build the site for publishing
- `python -m pytest`: Run tests

## Project Structure

<!--
Explain the key directories and files in your project.
This helps Gemini navigate the codebase more effectively.
Example:
- `src/`: Contains all source code.
- `tests/`: Unit and integration tests.
- `docs/`: Project documentation.
-->

- `content/`: Contains reStructuredText and Markdown files for posts and pages.
- `pelicanconf.py`: Main Pelican configuration file.
- `publishconf.py`: Configuration for publishing, extends `pelicanconf.py`.
- `themes/`: Custom themes for the Pelican site.
- `output/`: Generated static site files.
- `pelican/plugins/humans/`: Custom Pelican plugin.
- `test_humans.py`: Tests for the custom Pelican plugin.

## Custom Instructions

<!--
Use this section for any specific instructions or preferences not covered above.
For example, you might tell Gemini to:
- Prioritize certain types of changes (e.g., performance over readability).
- Avoid modifying specific files or directories.
- Always ask for confirmation before making significant changes.
-->

- Always make changes in a git branch.
    - Create a new git branch for a new unit of work.
- Always ask for confirmation before making significant changes.
- When suggesting code, provide examples that are directly applicable to the project's existing codebase.
- Maintain a tidy code base.
    - Ensure code is clear and avoids obfuscation or esoteric techniques.
    - Use docstrings for full documentation of modules, classes, and functions/methods.
    - Use other comments to clarify smaller, non-obvious, confusing, or non-intuitive sections of code.
    - Create comments to group code in a logical fashion.