#!/usr/bin/env python3
"""List all Claude Code sessions with metadata and conversation excerpts."""

import json
import os
from datetime import datetime

PROJECTS_DIR = os.path.expanduser('~/.claude/projects')
CURRENT_SESSION = os.environ.get('CLAUDE_SESSION_ID', '')


def extract_messages(jsonl_path, max_messages=4):
    messages = []
    try:
        with open(jsonl_path, encoding='utf-8') as f:
            for line in f:
                try:
                    obj = json.loads(line)
                    if obj.get('type') not in ('user', 'assistant'):
                        continue
                    msg = obj.get('message', {})
                    role = msg.get('role', '')
                    content = msg.get('content', '')
                    text = ''
                    if isinstance(content, str):
                        text = content.strip()
                    elif isinstance(content, list):
                        for c in content:
                            if isinstance(c, dict) and c.get('type') == 'text':
                                text = c.get('text', '').strip()
                                break
                    if text:
                        messages.append({'role': role, 'text': text[:400]})
                    if len(messages) >= max_messages:
                        break
                except Exception:
                    continue
    except Exception:
        pass
    return messages


def main():
    if not os.path.isdir(PROJECTS_DIR):
        print(json.dumps([]))
        return

    sessions = []
    for project_name in os.listdir(PROJECTS_DIR):
        project_path = os.path.join(PROJECTS_DIR, project_name)
        if not os.path.isdir(project_path):
            continue

        for fname in os.listdir(project_path):
            if not fname.endswith('.jsonl'):
                continue

            uuid = fname[:-6]

            # Skip current session
            if CURRENT_SESSION and uuid == CURRENT_SESSION:
                continue

            fpath = os.path.join(project_path, fname)
            try:
                stat = os.stat(fpath)
            except OSError:
                continue

            size_kb = round(stat.st_size / 1024, 1)
            modified = datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M')
            modified_ts = stat.st_mtime

            dir_path = os.path.join(project_path, uuid)
            has_dir = os.path.isdir(dir_path)

            messages = extract_messages(fpath)

            sessions.append({
                'uuid': uuid,
                'project': project_name,
                'file': fpath,
                'dir': dir_path if has_dir else None,
                'size_kb': size_kb,
                'modified': modified,
                'modified_ts': modified_ts,
                'messages': messages,
            })

    sessions.sort(key=lambda x: x['modified_ts'], reverse=True)
    # Remove the ts field (internal use only)
    for s in sessions:
        del s['modified_ts']

    print(json.dumps(sessions, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
