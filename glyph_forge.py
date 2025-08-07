#!/usr/bin/env python3
"""
glyph_forge.py - Utility to create new Zoran glyph definitions.

This script allows you to quickly forge new glyph JSON files within the
repository. It accepts the glyph name, triad elements, function, and description,
then writes the JSON file in the appropriate glyph domain directory under
`glyphs/`.
"""

import json
import os
import argparse

def create_glyph(domain, name, triad, function, description):
    """Create a glyph JSON file in the specified domain directory."""
    glyph = {
        "triad": triad,
        "function": function,
        "description": description
    }
    # Ensure domain directory exists inside glyphs
    directory = os.path.join("glyphs", domain.lower())
    os.makedirs(directory, exist_ok=True)

    filename = os.path.join(directory, f"{name.upper()}.json")
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(glyph, f, ensure_ascii=False, indent=4)

    print(f"Created {filename}")

def parse_args():
    parser = argparse.ArgumentParser(description="Forge a new Zoran glyph JSON file.")
    parser.add_argument("domain", help="Domain of the glyph (e.g. art, ethique, sciences)")
    parser.add_argument("name", help="Glyph name (e.g. CIMNODE)")
    parser.add_argument("-t", "--triad", nargs=3, required=True,
                        help="Three elements of the glyph triad (e.g. Alpha Beta Gamma)")
    parser.add_argument("-f", "--function", required=True, help="Function of the glyph")
    parser.add_argument("-d", "--description", required=True, help="Description of the glyph")
    return parser.parse_args()

def main():
    args = parse_args()
    create_glyph(args.domain, args.name, args.triad, args.function, args.description)

if __name__ == "__main__":
    main()
