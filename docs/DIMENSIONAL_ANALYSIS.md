# Dimensional analysis of the first E3 hypothesis

**Status:** living derivation, restart milestone 1  
**Scope:** definitions and dimensional consequences only; no legacy Bruno value

## 1. Geometry

For a sphere of radius `R`:

```text
A = 4 pi R^2
V = (4/3) pi R^3
A/V = 3/R
```

Therefore:

```text
[A]   = L^2
[V]   = L^3
[A/V] = L^-1
```

Define the geometric surface-to-volume density:

```text
beta_geom := A/V = 3/R
```

`beta_geom` is not dimensionless. In SI it has units `m^-1`.

## 2. Entropy density interpretation

Let:

```text
S      = entropy                         [J K^-1]
s_V    = S/V, volumetric entropy density [J K^-1 m^-3]
sigma_A = S/A, surface entropy density    [J K^-1 m^-2]
```

For the same entropy `S` represented over the same region:

```text
s_V / sigma_A = (S/V)/(S/A) = A/V = 3/R
```

This is an exact identity: `S` cancels. It is a geometric conversion between
surface and volume densities, not evidence by itself for entropy collapse.

If a boundary has critical surface capacity `sigma_crit`, its equivalent
volumetric capacity is:

```text
s_crit(R) = sigma_crit A/V = 3 sigma_crit/R
```

Consequently a universal surface capacity implies a radius-dependent
volumetric capacity. It does not imply one universal volumetric threshold.

## 3. Temperature coefficient

The legacy relation was written:

```text
beta_B = kappa T
```

If `beta_B` means `beta_geom = A/V`, then:

```text
[kappa_T] = [beta_geom]/[T] = L^-1 Theta^-1
```

In SI:

```text
[kappa_T] = m^-1 K^-1
```

It cannot be reported only as `K^-1` unless a reference length has first made
beta dimensionless.

## 4. Dimensionless normalization

Introduce an explicitly declared reference length `L_0`:

```text
beta_tilde := L_0 A/V = 3 L_0/R
```

Now `beta_tilde` is dimensionless. A temperature coefficient defined by
`beta_tilde = kappa_tilde T` would have units `K^-1`.

This does not determine `L_0`. The physical model must state why the reference
is a Planck length, system radius, correlation length, mean particle spacing,
or another scale. Selecting a reference because it reproduces a desired number
is not a derivation.

## 5. Proposed entropy-capacity observable

A candidate transition variable is:

```text
eta_S := s_system/s_crit
       = (S_system/V)/(sigma_crit A/V)
       = S_system/(sigma_crit A)
```

`eta_S` is dimensionless. The hypothesized transition condition would be:

```text
eta_S = 1
```

The equality is a hypothesis until `sigma_crit` is independently specified and
the transition is tested on data not used to choose it.

## 6. Decisions established by this derivation

1. `A/V = 3/R` is valid spherical geometry and has inverse-length units.
2. `(S/V)/(S/A)` reduces identically to `A/V`; entropy cancels.
3. A coefficient connecting `A/V` to temperature has units `m^-1 K^-1`.
4. A dimensionless transition criterion requires an explicit normalization.
5. Decay constants, fluence cuts, surface capacities, and temperature
   coefficients must use different symbols.

## 7. Still unresolved

1. What physical observable was the original `beta_B` intended to represent?
2. What boundary capacity `sigma_crit`, if any, applies outside black holes?
3. What physical similarity law could connect cosmic and laser-cooled systems?
4. Which measured transition would falsify or support `eta_S = 1`?

