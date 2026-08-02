
==============================================================================
CATEGORY A — SI-defined exact. Not recomputable; checked vs definition.
==============================================================================
  Since the 2019 SI redefinition, c, h and k_B are fixed numerical
  values that DEFINE the metre, kilogram and kelvin. There is no
  experiment or formula that yields them; a 'disagreement' here is
  simply a rounded transcription.

-- c  (defined exactly as 299 792 458 m/s)
  independent result : 299792458 m/s
              repo value     rel. error   verdict
               299792458      +0.0000%   EXACT MATCH   [57 files]
               300000000      +0.0692%   LOW PRECISION   [40 files]
               299792458      +0.0000%   EXACT MATCH   [6 files]

-- k_B  (defined exactly as 1.380649e-23 J/K)
  independent result : 1.380649e-23 J/K
              repo value     rel. error   verdict
            1.380649e-23      +0.0000%   EXACT MATCH   [79 files]
               1.381e-23      +0.0254%   LOW PRECISION   [1 file]

-- hbar = h/(2*pi), h defined exactly
  independent result : 1.054571818e-34 J*s
              repo value     rel. error   verdict
         1.054571817e-34      -0.0000%   EXACT MATCH   [45 files]
           1.0545718e-34      -0.0000%   match (rounding)   [10 files]

==============================================================================
CATEGORY B — measured. Checked against CODATA 2018 / IAU.
==============================================================================

-- G  (CODATA 2018: 6.67430(15)e-11, rel. unc. 2.2e-5)
  independent result : 6.6743e-11 m^3/kg/s^2
              repo value     rel. error   verdict
              6.6743e-11      +0.0000%   EXACT MATCH   [87 files]
                6.67e-11      -0.0644%   LOW PRECISION   [1 file]

-- M_sun  (IAU nominal 1.98847e30 kg)
  independent result : 1.98847e+30 kg
              repo value     rel. error   verdict
             1.98847e+30      +0.0000%   EXACT MATCH   [18 files]
              1.9885e+30      +0.0015%   match (rounding)   [3 files]
               1.989e+30      +0.0267%   LOW PRECISION   [6 files]

-- m_p  (CODATA 2018)
  independent result : 1.672621924e-27 kg
              repo value     rel. error   verdict
         1.672621924e-27      +0.0000%   EXACT MATCH   [1 file]
           1.6726219e-27      -0.0000%   match (rounding)   [2 files]

==============================================================================
CATEGORY C — derived. Recomputed from formula.
==============================================================================

-- Planck length:   l_P = sqrt(hbar*G/c^3)
  independent result : 1.616255024e-35 m
              repo value     rel. error   verdict
            1.616255e-35      -0.0000%   match (rounding)   [36 files]

-- Planck mass:     m_P = sqrt(hbar*c/G)
  independent result : 2.176434343e-08 kg
              repo value     rel. error   verdict
             2.17651e-08      +0.0035%   match (rounding)   [15 files]

-- Planck temperature: T_P = sqrt(hbar*c^5/G)/k_B
  independent result : 1.416784162e+32 K
              repo value     rel. error   verdict
            1.416808e+32      +0.0017%   match (rounding)   [7 files, named t_planck]

-- Planck TIME (what the name 't_planck' should hold):
     t_P = sqrt(hbar*G/c^5)
  independent result : 5.391246448e-44 s
  value stored under that name : 1.416808e+32
  ratio = 2.628e+75  -> the variable holds a TEMPERATURE,
  not a time. Misuse as a time is wrong by ~76 orders of magnitude.

==============================================================================
CATEGORY D — the GW150914 chain.
==============================================================================

-- Schwarzschild radius:  R_s = 2*G*M/c^2   (M = 62 M_sun)
  independent result : 183107.0417 m
              repo value     rel. error   verdict
                  183000      -0.0585%   LOW PRECISION   [Bruno Constant Note.txt]

-- Hawking temperature:   T_H = hbar*c^3/(8*pi*G*M*k_B)
  independent result : 9.951731982e-10 K
              repo value     rel. error   verdict
                 1.2e-08   +1105.8203%   *** MISMATCH ***   [Bruno Constant Note.txt / FINAL_ANALYSIS]
  -> implied mass for T_H = 1.2e-8 K : 5.14 M_sun (not 62)

-- Bekenstein-Hawking entropy: S = k_B*c^3*A/(4*G*hbar),  A = 16*pi*(GM/c^2)^2
  independent result : 5.567028847e+57 J/K
              repo value     rel. error   verdict
         7.009474411e+54     -99.8741%   *** MISMATCH ***   [Entropy Collapse Test 1.8/1.9/2.1]
         8.095718474e+50    -100.0000%   *** MISMATCH ***   [as coded in Gw150914 Entropy Test.py]
  -> mass implied by S = 7.0095e54 (via S = 4*pi*G*M^2*k_B/(hbar*c)) : 2.200 M_sun

==============================================================================
CATEGORY E — kappa, all five values.
==============================================================================
  Formula asserted by the framework:  beta_B = A/V = 3/R = kappa * T
  Two derivations appear in the corpus.

-- Planck route:  kappa = 3/(l_P * T_P)   [reduces to 3*k_B/(hbar*c)]
  independent result : 1310.109734 K^-1
              repo value     rel. error   verdict
                    1313      +0.2206%   LOW PRECISION   [19 files]
                    1366      +4.2661%   *** MISMATCH ***   [22 files]

-- GW route:      kappa = 3/(R_s * T_H)   [reduces to 12*pi*k_B/(hbar*c)]
  independent result : 16463.32446 K^-1
              repo value     rel. error   verdict
                    1366     -91.7028%   *** MISMATCH ***   [22 files]
                    1313     -92.0247%   *** MISMATCH ***   [19 files]
  NOTE: R_s*T_H = hbar*c/(4*pi*k_B) -- mass cancels. Ratio to Planck
  route = 12.5663706144 = 4*pi exactly. Not an independent check.

-- kappa = 0.001005  ('Chajar Constant', tangency threshold)
     Used as: T_tangent = T_planck * 0.001005  -> DIMENSIONLESS multiplier.
     Not a K^-1 quantity. No formula in corpus derives it.
     T_planck * 0.001005 = 1.42387e+29 K
     VERDICT: different physical quantity sharing the name. Not comparable.

-- kappa = 1340e-6 K^-1 s^-1  ('laboratory', BRUNO_CONSTANT_KAPPA)
     Units carry s^-1, inconsistent with beta_B = kappa*T.
     No derivation or experimental method anywhere in corpus.
     VERDICT: NOT RECOMPUTABLE -- no formula given. Unverifiable.

-- kappa = 1.23456789e-23  (engine / parser trees, 32 files)
     Digit sequence 1-2-3-4-5-6-7-8-9. No formula, no units.
     VERDICT: PLACEHOLDER. Not a physical value.

-- f_S = 1.66345592659651e-36  ('previously computed entropy contribution')
     Added to T_H and to r_s in two scripts. No derivation in corpus.
     VERDICT: NOT RECOMPUTABLE -- provenance absent.

==============================================================================
CATEGORY F — dimensional consistency of the governing equation.
==============================================================================
  beta_B = A/V = 3/R = kappa*T
    [3/R]     = m^-1
    [kappa*T] = K^-1 * K = dimensionless
  m^-1 != dimensionless  ->  the equation cannot balance.
  Consequence: kappa's value tracks the length unit.
    R in metre     : kappa =     16463.3245 K^-1
    R in kilometre : kappa =  16463324.4619 K^-1
    R in centimetre: kappa =       164.6332 K^-1
  No unit choice is privileged by the framework, so no value is determinate.

==============================================================================
ADDENDUM — Planck-unit literals dated by CODATA release
==============================================================================
  The three Planck literals sit just outside what G's uncertainty
  (u_r = 2.2e-5, halved to 1.1e-5 under a square root) permits. That is
  not rounding -- it dates them.

  Planck length  l_P: repo = 1.616255e-35
      CODATA 2010: 1.616199e-35   (+3.46e-05)
      CODATA 2014: 1.616229e-35   (+1.61e-05)
      CODATA 2018: 1.616255e-35   (+0.00e+00)  <== MATCHES

  Planck mass    m_P: repo = 2.17651e-08
      CODATA 2010: 2.17651e-08   (+0.00e+00)  <== MATCHES
      CODATA 2014: 2.17647e-08   (+1.84e-05)
      CODATA 2018: 2.176434e-08   (+3.49e-05)

  Planck temp    T_P: repo = 1.416808e+32
      CODATA 2010: 1.416833e+32   (-1.76e-05)
      CODATA 2014: 1.416808e+32   (+0.00e+00)  <== MATCHES
      CODATA 2018: 1.416784e+32   (+1.69e-05)

  VERDICT: three different CODATA vintages (2018, 2010, 2014) coexist
  in the same corpus -- and in some cases the same script.
