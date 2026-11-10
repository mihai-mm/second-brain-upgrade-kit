#!/usr/bin/env python3
"""Extracts the start of the messages the person wrote in their Claude Code sessions.

It is used to measure, on real work, how many sessions start by re-explaining
context, how many corrections repeat, and how often the agent used outdated
information. See 3-measuring-impact.md.

What it does and doesn't do:
- reads the sessions' .jsonl files (usually in ~/.claude/projects/);
- prints to the screen and nothing else: it writes no files and uses no network;
- considers only the messages written by the person, not the agent's replies
  or tool results.

Examples:
  python3 extract_sessions.py --sessions 30 --messages 3
  python3 extract_sessions.py --sessions 30 --search "I told you|again"
  python3 extract_sessions.py --counts
"""
import argparse
import glob
import json
import os
import re
import statistics
import sys

EDIT_TOOLS = {"Write", "Edit", "MultiEdit", "NotebookEdit"}


def person_texts(row):
    """Returns the texts written by the person in one line of the session."""
    if row.get("type") != "user":
        return []
    if row.get("isMeta") or row.get("isSidechain") or row.get("isCompactSummary"):
        return []
    message = row.get("message")
    if not isinstance(message, dict):
        return []
    content = message.get("content")
    if isinstance(content, str):
        pieces = [content]
    elif isinstance(content, list):
        pieces = [
            b.get("text", "")
            for b in content
            if isinstance(b, dict) and b.get("type") == "text"
        ]
    else:
        return []
    clean = []
    for text in pieces:
        text = text.strip()
        # Texts starting with "<" are system notices or commands, not the person's words.
        if text and not text.startswith("<"):
            clean.append(text)
    return clean


def read_session(path):
    messages = []
    date = ""
    folder = ""
    operations_before_edit = 0
    edit_seen = False
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            for line in f:
                try:
                    row = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if not isinstance(row, dict):
                    continue
                if not date and row.get("timestamp"):
                    date = str(row["timestamp"])[:10]
                if not folder and row.get("cwd"):
                    folder = str(row["cwd"])
                if row.get("type") == "assistant" and not row.get("isSidechain") and not edit_seen:
                    content = (row.get("message") or {}).get("content")
                    if isinstance(content, list):
                        for block in content:
                            if isinstance(block, dict) and block.get("type") == "tool_use":
                                if block.get("name") in EDIT_TOOLS:
                                    edit_seen = True
                                    break
                                operations_before_edit += 1
                messages.extend(person_texts(row))
    except OSError:
        return None
    return {
        "date": date,
        "folder": folder,
        "messages": messages,
        "operations": operations_before_edit if edit_seen else None,
    }


def shorten(text, chars):
    text = " ".join(text.split())
    return text if len(text) <= chars else text[:chars] + " […]"


def main():
    p = argparse.ArgumentParser(description="Start of the person's messages in Claude Code sessions.")
    p.add_argument("--folder", default=os.path.expanduser("~/.claude/projects"),
                   help="where the sessions are (default: ~/.claude/projects)")
    p.add_argument("--project", default="", help="only sessions whose working folder contains this text")
    p.add_argument("--sessions", type=int, default=30, help="how many recent sessions to read (default 30)")
    p.add_argument("--messages", type=int, default=3, help="how many opening messages to print per session (default 3)")
    p.add_argument("--chars", type=int, default=300, help="maximum length of each excerpt (default 300)")
    p.add_argument("--search", default="", help="regular expression: print only the messages that match it")
    p.add_argument("--counts", action="store_true", help="print the numbers only, no text")
    a = p.parse_args()

    session_files = glob.glob(os.path.join(a.folder, "**", "*.jsonl"), recursive=True)
    if not session_files:
        print(f"No sessions found in {a.folder}.")
        print("If you use another agent, or the sessions live elsewhere, move to the five questions in 3-measuring-impact.md.")
        return 0
    session_files.sort(key=os.path.getmtime, reverse=True)

    read = []
    for path in session_files:
        if len(read) >= a.sessions:
            break
        s = read_session(path)
        if not s or not s["messages"]:
            continue
        if a.project and a.project.lower() not in s["folder"].lower():
            continue
        read.append(s)

    if not read:
        print("No sessions with messages from the person match the chosen criteria.")
        return 0

    operations = [s["operations"] for s in read if s["operations"] is not None]
    print(f"Sessions read: {len(read)} (from {read[-1]['date']} to {read[0]['date']})")
    if operations:
        print(f"Agent operations before the first edit to a file: median {statistics.median(operations):g}, "
              f"max {max(operations)}, across {len(operations)} sessions with at least one edit")
    if len(read) < 10:
        print("Warning: fewer than ten sessions, the measure is weak.")

    if a.counts:
        return 0

    if a.search:
        try:
            pattern = re.compile(a.search, re.IGNORECASE)
        except re.error as e:
            print(f"Invalid expression: {e}", file=sys.stderr)
            return 2
        found = 0
        sessions_with_results = 0
        print()
        for s in read:
            matches = [m for m in s["messages"] if pattern.search(m)]
            if not matches:
                continue
            sessions_with_results += 1
            print(f"--- {s['date']} | {s['folder']}")
            for m in matches:
                found += 1
                print(f"  · {shorten(m, a.chars)}")
        print()
        print(f"Messages found: {found}, in {sessions_with_results} sessions out of {len(read)}")
        return 0

    print()
    for s in read:
        after = "no edits" if s["operations"] is None else f"{s['operations']} operations before the first edit"
        print(f"--- {s['date']} | {s['folder']} | {len(s['messages'])} messages | {after}")
        for i, m in enumerate(s["messages"][: a.messages], 1):
            print(f"  {i}. {shorten(m, a.chars)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
