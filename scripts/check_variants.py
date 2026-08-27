#!/usr/bin/env python3
"""Check that all theme variants stay structurally in sync.

Verifies that every variant defines the same style keys, the same
syntax keys, the same number of players, no null color values, and
only well-formed hex colors. Run after any edit to the theme file.
"""

import json
import pathlib
import re
import sys

HEX = re.compile(r'^#[0-9a-fA-F]{6}([0-9a-fA-F]{2})?$')


def main():
    path = pathlib.Path(__file__).resolve().parent.parent / 'themes' / 'tokyo-night.json'
    themes = json.loads(path.read_text())['themes']
    errors = []

    ref = themes[0]
    ref_keys = set(ref['style'])
    ref_syntax = set(ref['style']['syntax'])
    ref_players = len(ref['style']['players'])

    for t in themes:
        name, style = t['name'], t['style']
        for label, have, want in [
            ('style keys', set(style), ref_keys),
            ('syntax keys', set(style['syntax']), ref_syntax),
        ]:
            for k in sorted(want - have):
                errors.append(f'{name}: missing {label[:-1]} {k}')
            for k in sorted(have - want):
                errors.append(f'{name}: extra {label[:-1]} {k} not in {ref["name"]}')
        if len(style['players']) != ref_players:
            errors.append(f'{name}: {len(style["players"])} players, want {ref_players}')
        for k, v in style.items():
            if v is None:
                errors.append(f'{name}: {k} is null')
            elif isinstance(v, str) and v.startswith('#') and not HEX.match(v):
                errors.append(f'{name}: {k} has malformed color {v}')

    for e in errors:
        print(e)
    print(f'{len(themes)} variants, {len(ref_keys)} style keys, '
          f'{len(ref_syntax)} syntax keys, {ref_players} players: '
          + ('FAIL' if errors else 'OK'))
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
