# Aluminum relaxation comparison

This reference isolates an exploratory comparison between two independently measured
features of superconducting aluminum:

- Phillips (1959) heat-capacity equality at `T/Tc = 0.5058064686597585`.
- Norowski et al. quasiparticle relaxation in aluminum nanowires with `Tc = 1.3 K`.

The normalized Phillips point maps to `0.6575484092576861 K` in the nanowire sample.
Norowski et al. describe agreement with electron-phonon cooling above about `0.7 K`
and faster relaxation below it. Because `0.7 K` is a prose-level regime boundary and
has no fitted breakpoint uncertainty, proximity to `0.6575 K` is a cue for further
testing, not confirmation of a shared transition.

`fig2_relaxation_curves.tsv` contains exact values decoded from the authors' `Fig_2.opj`:
six experimental wire-length series and the electron-phonon reference curve. Values in
the relaxation column are microseconds, as labeled in Figure 2 and Supplemental Figure
S14. `alignment_result.json` records constants, normalization, interpolation brackets,
and the calculated ratios. Rebuild both with:

```bash
python3 scripts/analyze_aluminum_relaxation_alignment.py
```

The script never digitizes plotted pixels. It reads a lossless long-form extraction of
the Origin project from the gitignored raw-data directory.
