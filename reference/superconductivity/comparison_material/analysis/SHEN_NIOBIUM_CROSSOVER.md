# Shen 1965 niobium heat-capacity crossover audit

**Source:** Y. L. Shen, *Low Temperature Heat Capacities of Vanadium,
Niobium and Tantalum*, UCRL-16117 (1965)  
**Relevant graph:** Figure 11, PDF page 35 (printed page 27)  
**Status:** presentation-derived graphical bracket, not tabulated calorimetry

## What Figure 11 contains

Figure 11 plots the superconducting electronic heat capacity
`Ces/(gamma Tc)` against `Tc/T` for three niobium samples. Shen obtains the
electronic contribution by subtracting the stated lattice expression from the
measured total superconducting heat capacity.

The thesis states that the three samples share the empirical relation

```text
Ces/(gamma Tc) = 7.0 exp(-1.46 Tc/T)
```

only for `2 < Tc/T < 6`. At lower temperatures the samples separate and Shen
discusses an additional low-energy contribution whose magnitude depends on
sample purity.

## Equality construction

If the superconducting- and normal-state lattice heat capacities are equal,
then

```text
Cs = Cn  <=>  Ces = gamma T
             <=>  Ces/(gamma Tc) = T/Tc = 1/(Tc/T).
```

The equality can therefore be located by comparing the plotted Figure 11
curve with `1/(Tc/T)`. Visual inspection at high-resolution gives a
conservative sign-change bracket:

```text
1.55 <= Tc/T <= 1.65
0.606 <= T/Tc <= 0.645
```

The bracket midpoint is `T/Tc = 0.626`, with half-bracket width `0.020`.
That midpoint is only a convenient locator. It is not assigned the status of
a measured best-fit value, and no point-by-point capacities have been invented.

This graphical bracket does not contain the higher-precision aluminum result
`T/Tc = 0.5058064687` from Phillips Table II.

## Why the printed exponential is not the result

Solving the printed exponential relation against `T/Tc` gives

```text
T/Tc  = 0.5904138592
Tc/T  = 1.693727179
```

The root is outside the stated domain `2 < Tc/T < 6`. It is retained in the
machine-readable summary as an extrapolation sensitivity check and rejected
as either a measurement or a valid fit-derived crossover.

## Sample and interpretation boundaries

- Figure 11 combines Nb I, Nb II, and Nb III near the crossover; the samples
  are not interchangeable at the much lower temperatures where their curves
  separate.
- Shen's historical interpretation explicitly considers two energy gaps. It
  must not be silently relabeled as a modern single-gap result.
- The heat-capacity samples have `Tc` near 9.1-9.3 K, unlike the previously
  examined relaxation sample with `Tc = 5.4 K`. Cross-experiment comparison is
  therefore made first in reduced temperature.
- This result is a figure-derived cue. A numerical calorimetry table would
  supersede it.

## Weak-coupling BCS baseline

The weak-coupling BCS crossover is `t* = 0.5147917503` (`e3_core/bcs.py`,
`docs/BCS_BASELINE.md`). The niobium graphical bracket `0.606 <= T/Tc <= 0.645`
lies above it and does not contain it; the summary records this under
`comparison`.

Niobium is not a weak-coupling superconductor, and strong-coupling corrections
are not modelled in this repository. A simple strong-coupling approximation
that only enlarges the gap (the alpha model, explored outside the repository on
2026-11-03) moves the crossover upward but did not reach the bracket for
`Delta(0)/(k_B Tc)` up to 2.0. The offset is therefore not explained here.
Before it is treated as a cue, it needs a tabulated source rather than a
figure, a check of the lattice-subtraction assumption, and Shen's two-gap
interpretation taken into account.
