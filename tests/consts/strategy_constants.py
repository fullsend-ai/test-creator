"""Formatted strategy Markdown fixtures for the overflow-marker fetch-failure gate."""

from scripts.strategy_source import OVERFLOW_MARKER

STRATEGY_WITH_UNFETCHED_ATTACHMENT = f"""# TEST-999: Overflow strategy

## Metadata

- **Type**: Feature
- **Status**: Open

## Description

The full strategy {OVERFLOW_MARKER} and is stored as an attachment: {{{{TEST-999-strategy.md}}}}.
The TL;DR is shown below for quick reference.
"""

STRATEGY_WITHOUT_AC = """# TEST-998: Strategy without acceptance criteria

## Metadata

- **Type**: Feature
- **Status**: Open

## Description

h3. Risks

The strategy has no acceptance criteria section.
"""
