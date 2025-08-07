# zoran-glottal-glyphs

This repository contains a curated collection of Zoran glyph definitions
organized by domain. Each glyph is defined as a simple JSON file with a
triad, function, and description. These glyphs are intended to be used
by the Zoran IA framework and other mimetic agents.

## Repository structure

- `glyphs/` – top-level directory grouping glyphs by domain.
  - `art/` – contains glyphs related to artistic expression (e.g., `ARTNODE`).
  - `ethique/` – contains glyphs related to ethics and moral reasoning (e.g., `ETHNODE`).
  - `sciences/` – contains glyphs related to scientific discovery and inquiry (e.g., `QUANTNODE`).
- `glottal_grammar.master.json` – combined grammar file listing all registered glyphs.
- `glyph_forge.py` – utility script to create new glyph JSON files.

## Using glyphs

Each glyph JSON file follows this structure:

```json
{
    "triad": ["Alpha", "Beta", "Gamma"],
    "function": "Describe the role of the glyph here",
    "description": "A longer description of the glyph and its mimetic purpose."
}
```

You can forge a new glyph by running:

```bash
python glyph_forge.py <domain> <name> -t Triad1 Triad2 Triad3 -f "Function" -d "Description"
```

For example:

```bash
python glyph_forge.py sciences QUANTNODE -t Theta Iota Kappa \
    -f "Scientific innovation and quantum inquiry interface" \
    -d "Mimetic quantum science glyph enabling quantum reasoning, uncertainty modelling and scientific exploration."
```

This will generate a file at `glyphs/sciences/QUANTNODE.json`.

## Contributing

Contributions are welcome! Feel free to submit pull requests adding new
glyphs, improving documentation or extending the forge script. Please
follow the existing JSON structure for new glyphs.

## License

This project is licensed under the [MIT License](LICENSE).
