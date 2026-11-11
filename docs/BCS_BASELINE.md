# Weak-coupling BCS baseline

**Status:** established physics, implemented in `e3_core/bcs.py` and tested in
`e3_core/tests/test_bcs.py`. This is the baseline any E3 superconductivity claim
must beat. It contains no E3 assumption.

## 1. Scope and units

The baseline is the weak-coupling limit of BCS theory for an isotropic s-wave
gap with constant normal-state density of states `N(0)` per spin, taken in the
limit `hbar omega_D / (k_B Tc) -> infinity`. Strong-coupling corrections, which
are larger for metals such as Nb or Pb than for Al, are outside this model.

All quantities are reduced and dimensionless:

```text
t     = T/Tc
x     = xi/(k_B Tc)          single-particle energy measured from the Fermi level
delta = Delta(T)/(k_B Tc)
E     = sqrt(x^2 + delta^2)
y     = delta^2
```

The normal-state Sommerfeld coefficient is `gamma = (2 pi^2/3) N(0) k_B^2`
(two spin directions). Heat capacities and entropies are reported in units of
`gamma Tc`. In these units the normal state has `C_n/(gamma Tc) = S_n/(gamma Tc) = t`.

## 2. Cutoff-free gap equation

The BCS gap equation is `1/lambda = int_0^{omega_D} tanh(E/2T)/E dxi`. Subtracting
the same equation evaluated at `Tc` (where `Delta = 0`) eliminates `lambda`:

```text
F(y, t) := int_0^inf [ tanh(E/(2t))/E - tanh(x/2)/x ] dx = 0.
```

The integrand decays like `-y/(2x^3)`, so the integral converges and the
cutoff can be taken to infinity. At `t = 0`, `tanh(E/(2t))` is replaced by `1`.

**Tail used in code.** For `x >= X = 100` and `t <= 1`, both hyperbolic tangents
equal `1` to double precision, and

```text
int_X^inf (1/E - 1/x) dx = -ln((X + E_X)/(2X)),   E_X = sqrt(X^2 + y).
```

**Hand check.** `d/dx [asinh(x/delta) - ln x] = 1/E - 1/x`, and
`asinh(x/delta) - ln x -> ln(2/delta)` as `x -> inf`.

`F` decreases strictly in `y` (below) and `F(0, t) = ln(1/t) >= 0`, so for each
`0 <= t <= 1` there is exactly one root `y(t) >= 0`, with `y(1) = 0`.

## 3. Derivatives of F

With `u = E/(2t)`:

```text
dF/dy = int_0^inf (u sech^2 u - tanh u)/(16 t^3 u^3) dx      (< 0)
dF/dt = -(1/(2 t^2)) int_0^inf sech^2(E/(2t)) dx             (< 0)
dy/dt = -(dF/dt)/(dF/dy)                                     (implicit function theorem)
```

The `dF/dy` integrand is negative because `tanh u > u sech^2 u` for `u > 0`
(equivalently `sinh(2u) > 2u`). For `u < 1e-2` it is evaluated from its Taylor
series `(-1/24 + u^2/30 - 17 u^4/840 + O(u^6))/t^3` to avoid cancellation; the
next terms are `+31 u^6/2835 - 691 u^8/124740` (checked symbolically, and
against the direct formula in the tests). Its tail beyond
`X` is `-1/(2 E_X (E_X + X))`, which is the `y`-derivative of the tail in
section 2. At `t = 0` the integrand is `-1/(2E^3)`.

## 4. Entropy and heat capacity

The quasiparticle entropy, summed over spin and both signs of `xi`, is

```text
S_s = 4 N(0) k_B int_0^inf s(E/T) dxi,
s(z) = -f ln f - (1-f) ln(1-f) = ln(1 + e^{-z}) + z f,    f = 1/(e^z + 1).
```

Using `int_0^inf s(z) dz = pi^2/6`, the `delta = 0` case gives `S_n = gamma T`.
In reduced units:

```text
S_s/(gamma Tc) = (6/pi^2) int_0^inf s(E/t) dx.
```

Since `ds/dz = -z f(1-f)` and `dE/dt = (1/(2E)) dy/dt`, differentiating gives

```text
C_s/(gamma Tc) = t d(S_s/(gamma Tc))/dt
               = (6/pi^2) (1/t) int_0^inf f(1-f) [E^2/t - (1/2) dy/dt] dx,
               with f = f(E/t).
```

At `t = 1` this is the superconducting-side limit `t -> 1^-`, because it uses
the superconducting branch's `dy/dt`.

## 5. Closed-form checks used in tests

These follow from the equations above and are compared against the numerics:

| Quantity | Closed form | Value |
|---|---|---|
| `Delta(0)/(k_B Tc)` | `pi exp(-gamma_E)` | 1.7638769... |
| `dF/dy` at `y = 0, t = 1` | `-7 zeta(3)/(8 pi^2)` | -0.1065696... |
| `dy/dt` at `t = 1^-` | `-8 pi^2/(7 zeta(3))` | -9.383539... |
| jump `(C_s - C_n)/(gamma Tc)` at `Tc` | `12/(7 zeta(3))` | 1.426127... |
| `int_0^1 (C_s - C_n)/(gamma Tc t) dt` | `0` (entropies agree at `0` and `Tc`) | 0 |
| `int_0^1 (C_s - C_n)/(gamma Tc) dt` | `(3/4) exp(-2 gamma_E)` (condensation energy `N(0) Delta_0^2/2`) | 0.2364276... |

`gamma_E` is the Euler-Mascheroni constant and `zeta(3)` is Apery's constant.

**Hand check of the jump.** At `t = 1`, `y = 0`, `int_0^inf f(1-f) dx = f(0) = 1/2`,
and the `E^2/t` term reproduces the normal value `1`. The extra term is
`(6/pi^2)(1/2)(1/2)(8 pi^2/(7 zeta(3))) = 12/(7 zeta(3))`.

**Hand check of the condensation energy.** `int_0^Tc (C_s - C_n) dT = U_n(0) - U_s(0)`,
because the internal energies agree at `Tc`. That difference is `N(0) Delta_0^2/2`.
Dividing by `gamma Tc^2 = (2 pi^2/3) N(0) k_B^2 Tc^2` gives
`(3/(4 pi^2)) (pi e^{-gamma_E})^2 = (3/4) e^{-2 gamma_E}`.

## 6. Heat-capacity crossover

`heat_capacity_crossover()` returns the reduced temperature `t*` in `(0, 1)`
where `C_s = C_n`, i.e. where `C_s/(gamma Tc) = t`. It is found by bisection on
`g(t) = C_s/(gamma Tc) - t`, which is negative near `t = 0` and equal to
`12/(7 zeta(3)) > 0` at `t = 1`. The test checks that `g` has exactly one sign
change on a fine grid. This is a numerical result with no closed form.

Comparing `t*` with experiment assumes the superconducting and normal lattice
heat capacities are equal, so that the total-heat-capacity crossing equals the
electronic one. It also assumes weak coupling.
