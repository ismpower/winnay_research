# Aluminium heat-capacity crossover: first-pass evidence audit

**Source experiment:** Phillips, *Physical Review* 114, 676 (1959),
DOI `10.1103/PhysRev.114.676`  
**Numerical input:** NIMS `MSP151067.dat`  
**Analysis status:** derived from digitized figure data; no extrapolation

## Source cross-check

The paper and NIMS record agree on the following experimental context:

- sample: 212.64 g polycrystalline aluminium;
- purity: 99.998%, with 0.002% copper reported as the only spectrographically
  detected impurity;
- preparation: vacuum cast, machined, and vacuum annealed at 450 C for 48 h;
- zero-field transition temperature: 1.163 K;
- transition largely completed within 0.001 K;
- normal-state coefficient: `gamma = (1.350 +/- 0.01) mJ mol^-1 K^-2`;
- Debye temperature: `427.7 +/- 1.0 K`;
- calculated zero-temperature critical field: 103.0 gauss.

Figure 4 identifies the zero-field points below `Tc` as superconducting-state
heat capacity and the 300-gauss points as normal-state heat capacity. Since the
paper's calculated critical field is 103.0 gauss at zero temperature and falls
toward zero at `Tc`, the recorded 300-gauss condition suppresses
superconductivity throughout the analyzed range.

The supplied NIMS file is a digitization of Figure 4, with rounded values. The
paper's Table II contains more precise calorimetric values. Therefore the
present results are suitable for locating cues and designing the reproduction,
but Table II should be transcribed and independently checked before a final
thermodynamic result is reported.

## Direct crossover cue

Within the common measured interval from 0.236 K to 1.160 K, piecewise-linear
interpolation gives one heat-capacity equality:

```text
C_zero_field(T_cross) = C_300_gauss(T_cross)
T_cross               = 0.5750651387 K
T_cross / Tc           = 0.4944670152
```

These decimals describe the interpolation result, not experimental precision.
A defensible rounded report is approximately `0.575 K`, or `T/Tc approximately
0.494`. Experimental and digitization uncertainty have not yet been propagated.

## Higher-precision Table II result

Table II was subsequently transcribed as 149 visually checked printed pairs:
91 normal-state and 58 superconducting-state measurements. Using the 57
normal-state adiabatic-demagnetization points and all 58 superconducting points
within their shared measured range gives:

```text
shared range                 = 0.1718 to 1.1526 K
direct sign-change bracket   = 0.5803 to 0.5908 K
piecewise-linear crossover   = 0.5882529231 K
T_cross / Tc                 = 0.5058064687
```

The defensible report is approximately `0.588 K`, or `T/Tc approximately
0.506`. The longer decimal is retained only to make the computation exactly
reproducible.

The Table II result supersedes the NIMS figure-digitization value for numerical
work. Their difference is about `0.013 K`; this demonstrates the information
lost through plotting, digitization, and rounding. It is not evidence for an
additional physical effect.

The Table II partial integrals, still without extrapolation, are:

```text
integral[0.1718 K to T_cross] (C_s-C_n)/T dT = -0.3408985520 mJ mol^-1 K^-1
integral[0.1718 K to 1.1526 K] (C_s-C_n)/T dT = +0.2090197777 mJ mol^-1 K^-1
```

They remain offset partial integrals because the interval from zero to 0.1718 K
is absent. No absolute entropy difference is claimed.

This point is **not** the superconducting transition. The phase transition is
at 1.163 K. The lower crossover means:

```text
below T_cross:  C_s - C_n < 0
above T_cross:  C_s - C_n > 0, up to Tc
```

Because

```text
d(S_s - S_n)/dT = (C_s - C_n)/T,
```

the entropy difference decreases below the crossover and rises above it. Thus
the crossover is the temperature of the most negative `S_s - S_n` only when the
entropy integral uses the proper common zero-temperature reference.

## Truncated entropy calculation

Using exact integration of the piecewise-linear interpolant, but starting only
at the shared measured lower bound of 0.236 K, gives:

```text
integral[0.236 K to T_cross] (C_s-C_n)/T dT = -0.2439448267 mJ mol^-1 K^-1
integral[0.236 K to 1.160 K] (C_s-C_n)/T dT = +0.3287682840 mJ mol^-1 K^-1
```

These are **partial, offset integrals**, not absolute entropy differences. They
exclude the interval from zero to 0.236 K. They must not be used to claim that
entropy fails to balance at `Tc`.

The positive upper partial integral is itself a useful warning: the omitted
low-temperature negative contribution matters. A valid entropy-balance test
must use the more precise Table II data and an explicitly justified treatment
of the unmeasured interval down to zero.

## Additional cue reported by the experiment

Phillips reports that the superconducting electronic heat capacity did not
continue along a single exponential at the lowest reduced temperatures. In the
paper's analysis, the measured value near 0.17 K exceeded the selected
exponential extrapolation by about a factor of four. The author examined
temperature calibration, addenda, and possible trapped normal-state regions and
argued that the departure exceeded the estimated error.

This is a historical experimental observation and model comparison—not evidence
for E3 by itself. It becomes relevant only if a new E3 relation predicts the
curve or crossover before its parameters are fitted to these same data.

## Experimental-error constraints from the paper

- Overall precision was about 0.1% in the liquid-helium region.
- In the adiabatic-demagnetization region, reported precision of heat-input over
  temperature-rise measurements was about 2% for the normal state and for the
  superconducting state above 0.4 K.
- At the lowest superconducting temperatures, reported precision degraded to
  about 20% in the worst cases.
- The addenda correction was reported as 0.6% below 1 K in the normal state;
  in the superconducting state it reached 15% at 0.17 K, 3% at 0.3 K, and 0.2%
  at 1.1 K.
- The temperature scale was a recognized source of systematic uncertainty,
  especially at the lowest temperatures.

These regime-dependent uncertainties forbid treating every digitized point as
having equal precision.

## Next controlled step

1. Preserve the printed table groups and their temperature-scale notes.
2. Calculate entropy balance using measured points plus clearly separated
   low-temperature models.
3. Test sensitivity to interpolation and to the paper's uncertainty bounds.
4. Only afterward define an E3 candidate observable, before comparing with lead
   or niobium.
