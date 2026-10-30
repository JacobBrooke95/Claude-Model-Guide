# Literature review: methods for forecasting Anthropic model-release timing

Prepared 2026-10-30 for a small-sample, nonstationary, multi-signal release-date forecaster (families: Opus, Sonnet, Haiku, Fable, Mythos).

**Verification key**
- **DOI ✓** means the DOI was resolved against Crossref's registry and the title, authors, venue, volume and pages matched what is cited here.
- **arXiv ✓** means the ID was resolved through the arXiv API.
- **Fetched ✓** means the page was opened with WebFetch and the summary below is drawn from it.
- **Unverified** means the item was found in search results, but the URL was not opened or failed to load.

A summary marked "from abstract" is drawn from the verified abstract. A summary marked "standard result" is the paper's well-known headline finding, which I did not re-read in full here.

---

## 1. Small-sample event timing, renewal and recurrent-event models, hierarchical pooling, discrete-time hazards

**1.1 Lindqvist, B. H., Elvebakk, G., & Heggland, K. (2003).** The trend-renewal process for statistical analysis of repairable systems. *Technometrics*, 45(1), 31–44. https://doi.org/10.1198/004017002188618671 (DOI ✓)
- *Finding:* The trend-renewal process (TRP) generalizes both the renewal process and the nonhomogeneous Poisson process. Time is first warped by a cumulative trend function Λ(t), and the warped inter-event gaps are then i.i.d. from a renewal distribution. The model can therefore capture a trend in event rate (such as accelerating cadence) and non-exponential regularity of gaps at the same time.
- *Apply:* This is the most natural parametric backbone for the data. Give each family a TRP with a log-linear (power-law) trend in Λ and a gamma or Weibull renewal distribution, which separates "cadence is speeding up" from "gaps are more regular than Poisson".

**1.2 Cook, R. J., & Lawless, J. F. (2007).** *The Statistical Analysis of Recurrent Events.* Springer. https://doi.org/10.1007/978-0-387-69810-6 (DOI ✓)
- *Finding:* This is the standard reference on gap-time and calendar-time models for recurrent events. It covers renewal and modulated renewal processes, random effects across units, and trend tests. A key point is the distinction between gap-time models (time since last event) and counting-process models (calendar time), along with the correct handling of the right-censored final gap.
- *Apply:* Always include the currently open gap for each family as a right-censored observation. Dropping it biases cadence estimates toward shorter gaps. Use the book's frailty or random-effects formulation as the template for "families as units".

**1.3 Singer, J. D., & Willett, J. B. (1993).** It's about time: Using discrete-time survival analysis to study duration and the timing of events. *Journal of Educational Statistics*, 18(2), 155–195. https://doi.org/10.3102/10769986018002155 (DOI ✓)
- *Finding:* Discrete-time hazard models fit as logistic regressions on a person-period data set. They handle censoring, time-varying covariates and flexible baseline hazards with ordinary GLM tooling. The authors argue the approach is especially transparent when event times are naturally grouped (e.g., by week).
- *Apply:* Expand the data to family×week rows with outcome "released this week". Leak signals, market prices and competitor events then become time-varying covariates in logit h(t). This is the cleanest way to put signals and the cadence baseline in one likelihood.

**1.4 Allison, P. D. (1982).** Discrete-time methods for the analysis of event histories. *Sociological Methodology*, 13, 61–98. https://doi.org/10.2307/270718 (DOI ✓)
- *Finding:* This is the foundational treatment of discrete-time event-history models. It shows the equivalence between the discrete-time hazard likelihood and binary regression on person-periods, and compares logit with complementary log-log links. Under complementary log-log, the coefficients approximate a grouped-time proportional hazards model.
- *Apply:* Use a cloglog link if you want hazard ratios comparable to a continuous-time Cox or renewal baseline. Use logit if you want coefficients that add directly in log-odds alongside likelihood-ratio signals.

**1.5 Cox, D. R. (1972).** Regression models and life-tables. *Journal of the Royal Statistical Society, Series B*, 34(2), 187–202. https://doi.org/10.1111/j.2517-6161.1972.tb00899.x (DOI ✓)
- *Finding:* This paper introduced the proportional hazards model, in which covariates act multiplicatively on an unspecified baseline hazard. It is a standard result and the basis for almost all hazard-regression practice.
- *Apply:* Treat signals as multiplicative hazard shifts on a cadence baseline. With n≈25 events, use a parametric baseline (from 1.1) rather than a semi-parametric one, which would spend too many degrees of freedom.

**1.6 Efron, B., & Morris, C. (1975).** Data analysis using Stein's estimator and its generalizations. *Journal of the American Statistical Association*, 70(350), 311–319. https://doi.org/10.1080/01621459.1975.10479864 (DOI ✓)
- *Finding:* This paper is the classic demonstration (baseball batting averages) that shrinking group estimates toward a common mean beats estimating each group separately in total squared error once there are three or more groups. It is a standard result.
- *Apply:* Five families qualify. Shrink family-level cadence intercepts and trend slopes toward a pooled Anthropic value. Fable and Mythos, with 0–2 observed releases, should be almost entirely pooled predictions.

**1.7 Gelman, A. (2006).** Prior distributions for variance parameters in hierarchical models. *Bayesian Analysis*, 1(3), 515–534. https://doi.org/10.1214/06-BA117A (DOI ✓)
- *Finding:* The paper shows that the inverse-gamma(ε, ε) "noninformative" prior on group-level variance is badly behaved when there are few groups. It recommends half-t or half-Cauchy priors on the group-level SD and weakly informative scaling when the number of groups is small. This is a standard result.
- *Apply:* With only 5 families, the between-family SD is barely identified. Use a half-normal or half-t prior on the SD of family effects in log-gap units, centered so that families differ by a factor of about 1.5–2×, and report how much the forecasts move under alternative scales.

**1.8 Ibrahim, J. G., & Chen, M.-H. (2000).** Power prior distributions for regression models. *Statistical Science*, 15(1), 46–60. https://doi.org/10.1214/ss/1009212673 (DOI ✓; Crossref lists the authors as Chen & Ibrahim, but the paper is conventionally cited as Ibrahim & Chen)
- *Finding:* The power prior raises a historical-data likelihood to a power a₀ ∈ [0, 1], which discounts older or less exchangeable data in a principled way. The paper develops the theory and gives regression examples.
- *Apply:* Model nonstationarity by down-weighting 2023 releases, for example with a₀ ≈ 0.3–0.6 for pre-2024 gaps, as an alternative or complement to an explicit trend term. Choose a₀ by leave-future-out score (5.9) rather than by eye.

**1.9 Adams, R. P., & MacKay, D. J. C. (2007).** Bayesian online changepoint detection. arXiv:0710.3742. https://arxiv.org/abs/0710.3742 (arXiv ✓)
- *Finding:* The paper gives an exact recursive algorithm for the posterior over the "run length" since the last changepoint in a sequence. It allows a model to forget pre-change data automatically as evidence of a regime shift accumulates.
- *Apply:* This is an alternative to a smooth trend. Run it on log-gaps to test whether the 2024–2026 acceleration looks more like a step change than a smooth trend. Epoch's capability-trend breakpoint (7.2) suggests a step is plausible.

**1.10 Gelman, A., Vehtari, A., Simpson, D., et al. (2020).** Bayesian workflow. arXiv:2011.01808. https://arxiv.org/abs/2011.01808 (arXiv ✓)
- *Finding:* The paper sets out an iterative workflow of prior predictive checks, fake-data simulation, model expansion, comparison and sensitivity analysis. Its emphasis is on understanding a family of models rather than selecting a single one.
- *Apply:* Simulate fake release histories from the hierarchical TRP and check that the fitting code recovers the trend and pooling parameters with n≈25 before trusting it on real data.

---

## 2. Self- and mutually-exciting processes; competitive launch timing and preannouncements

**2.1 Hawkes, A. G. (1971).** Spectra of some self-exciting and mutually exciting point processes. *Biometrika*, 58(1), 83–90. https://doi.org/10.1093/biomet/58.1.83 (DOI ✓)
- *Finding:* This paper defines point processes whose intensity jumps after each event and then decays. In the multivariate version, events of type j raise the intensity of type i. This is the foundational paper.
- *Apply:* Conceptually, a competitor's frontier release (OpenAI or Google) may raise Anthropic's short-term release hazard. With about 25 Anthropic events, though, a full multivariate Hawkes is not identifiable. Encode the idea as a decaying "days since last competitor frontier release" covariate (e.g., exp(−Δt/τ)) in the discrete hazard, with τ given a prior.

**2.2 Laub, P. J., Taimre, T., & Pollett, P. K. (2015).** Hawkes processes. arXiv:1507.02822. https://arxiv.org/abs/1507.02822 (arXiv ✓). See also **Laub, Lee, Pollett & Taimre (2024)**, *Hawkes Models and Their Applications*, arXiv:2405.10527, https://arxiv.org/abs/2405.10527 (arXiv ✓).
- *Finding:* These are accessible surveys of Hawkes theory, simulation, maximum-likelihood estimation and goodness of fit via time rescaling.
- *Apply:* Use the time-rescaling residual check, which transforms event times by the fitted compensator and tests for unit-rate exponential gaps, as a goodness-of-fit diagnostic for any intensity model, including the TRP.

**2.3 Reinhart, A. (2018).** A review of self-exciting spatio-temporal point processes and their applications. *Statistical Science*, 33(3), 299–318. https://doi.org/10.1214/17-STS629 (DOI ✓)
- *Finding:* The review covers estimation (MLE, EM via branching structure, Bayesian methods) and the identifiability of background versus triggered events. It is a standard reference.
- *Apply:* Use it as a caution. Separating baseline cadence from competitor-triggered launches needs many events, so keep the excitation component small and heavily regularized.

**2.4 Valera, I., & Gomez-Rodriguez, M. (2015).** Modeling adoption and usage of competing products. arXiv:1406.0516 (IEEE ICDM 2015). https://arxiv.org/abs/1406.0516 (arXiv ✓)
- *Finding (from abstract):* The authors model adoption and usage of competing products as temporal point processes in which one product's usage intensity is modulated by competitors'. They fit the model with a convex program.
- *Apply:* This shows precedent for mutually exciting or inhibiting intensities between competing products. It is relevant if you later model user and press attention, but it is not about launch timing itself.

**2.5 Eliashberg, J., & Robertson, T. S. (1988).** New product preannouncing behavior: A market signaling study. *Journal of Marketing Research*, 25(3), 282–292. https://doi.org/10.1177/002224378802500305 (DOI ✓)
- *Finding (from abstract):* In a manager survey, the propensity to preannounce new products was explained by market dominance, company size, competitive attractiveness and customer switching costs.
- *Apply:* Expect exec teases to be strategic signals whose frequency depends on competitive position. Their lead time and reliability should be estimated from Anthropic's own history, not assumed constant across eras (e.g., before and after the IPO filing).

**2.6 Lilly, B., & Walters, R. (1997).** Toward a model of new product preannouncement timing. *Journal of Product Innovation Management*, 14(1), 4–20. https://doi.org/10.1111/1540-5885.1410004 (DOI ✓)
- *Finding (from abstract):* The paper builds a framework for how far in advance firms preannounce, as a function of audience (customers, competitors, complementors) and purpose (building interest, feedback, delaying consumer purchases).
- *Apply:* Model the "teaser → release" lead-time distribution separately by signal audience. A developer-facing signal (an API or cloud catalog entry) likely has a shorter, tighter lead time than a consumer- or investor-facing tease.

**2.7 Bayus, B. L., Jain, S., & Rao, A. G. (2001).** Truth or consequences: An analysis of vaporware and new product announcements. *Journal of Marketing Research*, 38(1), 3–13. https://doi.org/10.1509/jmkr.38.1.3.18834 (DOI ✓)
- *Finding (from abstract):* Using empirical software-industry data and a game-theoretic model, the authors find that some firms strategically announce products well before availability ("vaporware") to deter competitors.
- *Apply:* Exec teases and roadmap statements should carry an explicit probability of slippage. Their likelihood ratios should be smaller than those of hard technical leaks such as model IDs appearing in cloud catalogs.

**2.8 Wu, Y., Balasubramanian, S., & Mahajan, V. (2004).** When is a preannounced new product likely to be delayed? *Journal of Marketing*, 68(2), 101–113. https://doi.org/10.1509/jmkg.68.2.101.27792 (DOI ✓)
- *Finding (from abstract):* Delays beyond a preannounced deadline are explained jointly by the firm's motivation to delay, constraints or opportunities for delay, and development ability.
- *Apply:* When an executive gives a window ("in the coming weeks"), put a right-skewed slip distribution on it. Condition the slip on whether a competitor or corporate constraint (e.g., an IPO calendar) raises the cost of delay.

**2.9 Hendricks, K. B., & Singhal, V. R. (1997).** Delays in new product introductions and the market value of the firm. *Management Science*, 43(4), 422–436. https://doi.org/10.1287/mnsc.43.4.422 (DOI ✓)
- *Finding (from abstract):* In a sample of 101 firms, announcing a delay to a promised introduction cut market value by 5.25% on average, so missing announced dates carries real penalties.
- *Apply:* For a public or soon-public company (after the S-1), stated dates become costlier to miss. This argues for slightly higher reliability of explicit dated commitments after the IPO filing, not for vaguer teases.

**2.10 Sorescu, A., Shankar, V., & Kushwaha, T. (2007).** New product preannouncements and shareholder value: Don't make promises you can't keep. *Journal of Marketing Research*, 44(3), 468–489. https://doi.org/10.1509/jmkr.44.3.468 (DOI ✓)
- *Finding (from abstract):* The authors test agency and signaling hypotheses on software and hardware preannouncements and assess when preannouncements create shareholder value, including the penalties for undelivered promises.
- *Apply:* This supports including a corporate-status regime covariate (private vs. public) that changes the reliability of preannouncement signals.

**2.11 Robertson, T. S., Eliashberg, J., & Rymon, T. (1995).** New product announcement signals and incumbent reactions. *Journal of Marketing*, 59(3), 1–15. https://doi.org/10.1177/002224299505900301 (DOI ✓). Also **Bowman, D., & Gatignon, H. (1995).** Determinants of competitor response time to a new product introduction. *Journal of Marketing Research*, 32(1), 42–53. https://doi.org/10.1177/002224379503200106 (DOI ✓)
- *Finding (from abstracts):* Robertson et al. characterize when incumbents respond to announcement signals. Bowman and Gatignon find that response *speed* depends on market growth, the shares of the reacting and threatening firms, typical development time and the industry's frequency of product changes.
- *Apply:* This is theoretical grounding for a competitor-response covariate. Response speed should be faster in a high-frequency-change industry, so expect a short excitation half-life (weeks, not months). Because a response is bounded by development time, a competitor launch can only pull forward a model that is already near-ready, which argues for an interaction with "gap age".

**2.12 Kohli, C. (1999).** Signaling new product introductions: A framework explaining the timing of preannouncements. *Journal of Business Research*, 46(1), 45–56. https://doi.org/10.1016/S0148-2963(98)00041-1 (DOI ✓; no abstract in Crossref, so the summary is limited)
- *Finding:* The paper offers a conceptual framework for the timing of preannouncements relative to launch.
- *Apply:* Secondary to 2.6 and 2.8. Include it only as background.

---

## 3. Combining forecasts and signals

**3.1 Clemen, R. T., & Winkler, R. L. (1985).** Limits for the precision and value of information from dependent sources. *Operations Research*, 33(2), 427–442. https://doi.org/10.1287/opre.33.2.427 (DOI ✓)
- *Finding (from abstract and standard result):* Positive dependence among information sources sharply reduces their combined precision and value, and the limiting value of many dependent sources can fall well short of perfect information. Under a normal model with common pairwise correlation ρ, n sources are worth about n/(1+(n−1)ρ) independent sources, which is bounded by 1/ρ.
- *Apply:* This is the formal basis for a dependence discount. Group signals by provenance. For example, a cloud-catalog leak, the codename string it exposed, and the press stories citing that leak form one cluster. Scale the cluster's summed log-likelihood ratios by 1/(1+(n−1)ρ), with ρ ≈ 0.5–0.8 within clusters and ρ ≈ 0 across clusters, and fit ρ by leave-future-out if data permit.

**3.2 Winkler, R. L. (1981).** Combining probability distributions from dependent information sources. *Management Science*, 27(4), 479–488. https://doi.org/10.1287/mnsc.27.4.479 (DOI ✓)
- *Finding:* The paper gives a normal-model Bayesian combination of expert distributions with an explicit error covariance matrix. Optimal weights depend on the inverse covariance and can be negative for highly correlated sources. This is a standard result.
- *Apply:* This is the full-covariance version of 3.1. Do not attempt to estimate a free covariance matrix from n≈25. Use the structured (cluster/ρ) version instead.

**3.3 Domingos, P., & Pazzani, M. (1997).** On the optimality of the simple Bayesian classifier under zero-one loss. *Machine Learning*, 29(2–3), 103–130. https://doi.org/10.1023/A:1007413511361 (DOI ✓)
- *Finding:* Naive Bayes can rank and classify well even when its independence assumption is badly violated, but its probability estimates are then systematically overconfident. This is a standard result.
- *Apply:* Naive-Bayes stacking of signal likelihood ratios will order weeks sensibly but overstate probabilities. Always follow it with a recalibration step (one slope parameter on the logit; see 3.6 and 3.7) fit out of sample.

**3.4 Genest, C., & Zidek, J. V. (1986).** Combining probability distributions: A critique and an annotated bibliography. *Statistical Science*, 1(1), 114–135. https://doi.org/10.1214/ss/1177013825 (DOI ✓)
- *Finding:* This is the classic review of linear versus logarithmic opinion pools. The log pool is "externally Bayesian", meaning that pooling and then updating gives the same result as updating and then pooling. The linear pool preserves marginalization but not external Bayesianity. This is a standard result.
- *Apply:* Because signals arrive over time and you update repeatedly, use a logarithmic or log-linear pool for combining component *probabilities of release-by-date*. Updating is then order-independent.

**3.5 Ranjan, R., & Gneiting, T. (2010).** Combining probability forecasts. *Journal of the Royal Statistical Society, Series B*, 72(1), 71–91. https://doi.org/10.1111/j.1467-9868.2009.00726.x (DOI ✓). Also **Gneiting, T., & Ranjan, R. (2013).** Combining predictive distributions. *Electronic Journal of Statistics*, 7, 1747–1782. https://doi.org/10.1214/13-EJS823 (DOI ✓)
- *Finding (from abstract):* Any non-trivial linear pool of distinct calibrated forecasts is necessarily uncalibrated and lacks sharpness, so recalibration is needed. The authors propose the beta-transformed linear pool.
- *Apply:* If you linearly average the renewal-model CDF with a market-implied CDF, the result will be underconfident. Either use a log pool or apply a two-parameter beta transform, though with n≈25 even two parameters is a lot, so prefer one.

**3.6 Satopää, V. A., Baron, J., Foster, D. P., Mellers, B. A., Tetlock, P. E., & Ungar, L. H. (2014).** Combining multiple probability predictions using a simple logit model. *International Journal of Forecasting*, 30(2), 344–356. https://doi.org/10.1016/j.ijforecast.2013.09.009 (DOI ✓)
- *Finding:* The authors aggregate forecasts by averaging log-odds and then multiplying by an extremizing factor a > 1. In the Good Judgment Project data this simple model outperformed linear averaging. This is a standard result.
- *Apply:* Use the log-odds average with a single extremizing exponent fit by rolling-origin. Expect a > 1 only to the extent that components draw on *different* information. If the market and the leak model see the same leaks, a should be close to 1.

**3.7 Baron, J., Mellers, B. A., Tetlock, P. E., Stone, E., & Ungar, L. H. (2014).** Two reasons to make aggregated probability forecasts more extreme. *Decision Analysis*, 11(2), 133–145. https://doi.org/10.1287/deca.2014.0293 (DOI ✓)
- *Finding (from abstract):* The first reason is that random error compresses averaged probabilities toward 0.5, which affects means but not log-odds means. The second is that each forecaster discounts for their own ignorance of information others hold.
- *Apply:* The first reason disappears if you already pool in log-odds. Only the second (complementary information) justifies extremizing. This is a clear rule: extremize across clusters of independent evidence, never within a cluster.

**3.8 Clemen, R. T. (1989).** Combining forecasts: A review and annotated bibliography. *International Journal of Forecasting*, 5(4), 559–583. https://doi.org/10.1016/0169-2070(89)90012-5 (DOI ✓)
- *Finding:* Across a large literature, combining forecasts reliably improves accuracy, and simple equal-weight averages are hard to beat. This is a standard result.
- *Apply:* Default to equal weights across component models.

**3.9 Claeskens, G., Magnus, J. R., Vasnev, A. L., & Wang, W. (2016).** The forecast combination puzzle: A simple theoretical explanation. *International Journal of Forecasting*, 32(3), 754–762. https://doi.org/10.1016/j.ijforecast.2015.12.005 (DOI ✓). Also **Smith, J., & Wallis, K. F. (2009).** A simple explanation of the forecast combination puzzle. *Oxford Bulletin of Economics and Statistics*, 71(3), 331–355. https://doi.org/10.1111/j.1468-0084.2008.00541.x (DOI ✓)
- *Finding:* "Optimal" weights estimated from data add estimation variance (and, per Claeskens et al., bias once weights are treated as random). This can make them worse than fixed equal weights, which explains why simple averages win in practice. These are standard results.
- *Apply:* With ~25 events, estimated combination weights are mostly noise. Fix equal weights, or shrink estimated weights strongly toward equal, and spend your scarce degrees of freedom on calibration instead.

**3.10 Genre, V., Kenny, G., Meyler, A., & Timmermann, A. (2013).** Combining expert forecasts: Can anything beat the simple average? *International Journal of Forecasting*, 29(1), 108–121. https://doi.org/10.1016/j.ijforecast.2012.06.004 (DOI ✓). Also **Timmermann, A. (2006).** Forecast combinations. In *Handbook of Economic Forecasting* (Vol. 1, pp. 135–196). https://doi.org/10.1016/S1574-0706(05)01004-9 (DOI ✓). And **Wang, X., Hyndman, R. J., Li, F., & Kang, Y. (2023).** Forecast combinations: An over 50-year review. *International Journal of Forecasting*, 39(4), 1518–1547. https://doi.org/10.1016/j.ijforecast.2022.11.005 (DOI ✓)
- *Finding:* On the ECB Survey of Professional Forecasters, sophisticated weighting schemes beat the simple average only occasionally and not robustly. Timmermann and Wang et al. survey when combinations help, including under instability and structural breaks. These are standard results.
- *Apply:* This confirms the default. Treat any fitted weighting as an experiment that must beat equal weights under rolling-origin evaluation (Section 5) by more than its standard error.

**3.11 Yao, Y., Vehtari, A., Simpson, D., & Gelman, A. (2018).** Using stacking to average Bayesian predictive distributions (with discussion). *Bayesian Analysis*, 13(3), 917–1007. https://doi.org/10.1214/17-BA1091 (DOI ✓). Also **Hoeting, J. A., Madigan, D., Raftery, A. E., & Volinsky, C. T. (1999).** Bayesian model averaging: A tutorial. *Statistical Science*, 14(4), 382–417. https://doi.org/10.1214/ss/1009212519 (DOI ✓)
- *Finding:* Bayesian model averaging weights models by posterior probability and asymptotically picks one model when none is true (the "M-open" setting). Stacking instead chooses weights that maximize the leave-one-out predictive log score and performs better in that setting. These are standard results.
- *Apply:* All the candidate models (TRP, changepoint, market-implied) are wrong. If you fit weights at all, use stacking on leave-future-out log scores, not BMA. Only do this once there are about 40 or more scored forecast origins, and otherwise use equal weights (3.9).

**3.12 Jose, V. R. R., Grushka-Cockayne, Y., & Lichtendahl, K. C. (2014).** Trimmed opinion pools and the crowd's calibration problem. *Management Science*, 60(2), 463–475. https://doi.org/10.1287/mnsc.2013.1781 (DOI ✓)
- *Finding:* Trimming the most extreme forecasts (exterior trimming) helps when individual forecasts are overconfident. Trimming the middle (interior trimming) helps when they are underconfident. This is a standard result.
- *Apply:* When pooling several prediction markets (Polymarket, Kalshi, Manifold) on the same question, consider interior-trimmed or median pooling. Long-dated markets tend to be underconfident (4.4, 4.5).

**3.13 Turner, B. M., Steyvers, M., Merkle, E. C., Budescu, D. V., & Wallsten, T. S. (2014).** Forecast aggregation via recalibration. *Machine Learning*, 95(3), 261–289. https://doi.org/10.1007/s10994-013-5401-4 (DOI ✓)
- *Finding:* Recalibrating individual forecasts (e.g., with a linear-in-log-odds transform) before or after aggregation improves aggregate accuracy over raw averaging. This is a standard result.
- *Apply:* Recalibrate each input (market, signal model, cadence model) on its own track record before pooling.

**3.14 Allard, D., Comunian, A., & Renard, P. (2012).** Probability aggregation methods in geoscience. *Mathematical Geosciences*, 44(5), 545–581. https://doi.org/10.1007/s11004-012-9396-3 (DOI ✓)
- *Finding:* The paper reviews linear, log-linear and generalized log-linear pooling. In log-linear pools, weights need not sum to 1: weights summing to less than 1 discount redundant sources, and weights summing to more than 1 express complementary information. This is a standard result.
- *Apply:* This gives a single formalism for both the dependence discount (3.1) and extremizing (3.6). log-odds(p) = log-odds(prior) + Σ wₖ·log LRₖ, with Σw within a cluster below 1 and across-cluster weights at or above 1.

**3.15 Morris, P. A. (1977).** Combining expert judgments: A Bayesian approach. *Management Science*, 23(7), 679–693. https://doi.org/10.1287/mnsc.23.7.679 (DOI ✓). Also **Clemen, R. T., & Winkler, R. L. (1999).** Combining probability distributions from experts in risk analysis. *Risk Analysis*, 19(2), 187–203. https://doi.org/10.1111/j.1539-6924.1999.tb00399.x (DOI ✓)
- *Finding:* Morris treats expert judgments as data with a likelihood, which is the "supra-Bayesian" approach. Clemen and Winkler's review concludes that simple mathematical rules usually perform about as well as complex ones. These are standard results.
- *Apply:* Treat each signal type as data with an empirically estimated likelihood ratio, P(signal | release within k days) / P(signal | not). This is exactly the supra-Bayesian view.

---

## 4. Prediction markets: accuracy, biases and thin markets

**4.1 Wolfers, J., & Zitzewitz, E. (2004).** Prediction markets. *Journal of Economic Perspectives*, 18(2), 107–126. https://doi.org/10.1257/0895330041371321 (DOI ✓)
- *Finding:* This survey finds markets generally aggregate information well and often beat polls and experts. It also flags the favourite–longshot bias, thin-market manipulation risk and contract-design issues. This is a standard result.
- *Apply:* Treat markets as one strong but biased input, not ground truth.

**4.2 Manski, C. F. (2006).** Interpreting the predictions of prediction markets. *Economics Letters*, 91(3), 425–429. https://doi.org/10.1016/j.econlet.2006.01.004 (DOI ✓). Also **Wolfers, J., & Zitzewitz, E. (2006).** Interpreting prediction market prices as probabilities. NBER Working Paper 12200. https://doi.org/10.3386/w12200 (DOI ✓)
- *Finding:* Manski shows that with risk-neutral, budget-constrained traders holding heterogeneous beliefs, the price need not equal the mean belief and only partially bounds it. Wolfers and Zitzewitz reply that under plausible (e.g., log) utility the price approximates the mean belief closely. These are standard results.
- *Apply:* Price is an approximately unbiased probability only under assumptions. Recalibrate empirically (4.5) rather than assuming p_market = p_true.

**4.3 Snowberg, E., & Wolfers, J. (2010).** Explaining the favorite–long shot bias: Is it risk-love or misperceptions? *Journal of Political Economy*, 118(4), 723–746. https://doi.org/10.1086/655844 (DOI ✓)
- *Finding:* In horse-race betting, the favourite–longshot bias is better explained by probability misperception (overweighting small probabilities) than by risk-loving preferences. This is a standard result.
- *Apply:* Low-priced "release by [near date]" contracts on AI markets are likely overpriced. Shade sub-10% contracts down.

**4.4 Page, L., & Clemen, R. T. (2013).** Do prediction markets produce well-calibrated probability forecasts? *Economic Journal*, 123(568), 491–513. https://doi.org/10.1111/j.1468-0297.2012.02561.x (DOI ✓; author PDF fetched ✓: https://people.duke.edu/~clemen/bio/Published%20Papers/45.PredictionMarkets-Page&Clemen-EJ-2013.pdf)
- *Finding (fetched):* Using about 500,000 Intrade transactions, the authors find markets reasonably calibrated near expiration but significantly biased for events farther away (stronger beyond 100 days), with prices pulled toward 50%. They attribute this to time discounting: capital tied up in contracts earns no interest, so favourite buyers abstain.
- *Apply:* For long-dated contracts such as "Opus 6 by end of Q2 2027", apply stronger extremizing (a recalibration slope above 1) the longer the time to resolution.

**4.5 Le, N. A. (2026).** Decomposing crowd wisdom: Domain-specific calibration dynamics in prediction markets. arXiv:2602.19520 (preprint). https://arxiv.org/abs/2602.19520 (fetched ✓)
- *Finding (fetched):* Across about 292 million Kalshi and Polymarket trades and about 327,000 contracts, the mean calibration slope (in logit) rises from 0.99 within one hour of resolution to 1.32 beyond one month. Prices are underconfident and compressed toward 0.5 at long horizons. Calibration varies by domain and trade size.
- *Apply:* This is a directly usable default: logit(p) = b(h)·logit(p_market), with b ≈ 1.0 when resolution is under a day away, rising to about 1.3 beyond a month. It is an unrefereed preprint, so treat these as prior values and update on AI-market data.

**4.6 Bürgi, C., Deng, W., & Whelan, K. (2025).** Makers and takers: The economics of the Kalshi prediction market. UCD Centre for Economic Research WP25/19; CESifo WP 12122. https://www.ucd.ie/economics/t4media/WP2025_19.pdf (fetched ✓)
- *Finding (fetched):* Kalshi prices are informative and become more accurate as markets approach closing. There is a clear favourite–longshot bias: buyers of contracts under 10¢ lose over 60% of their stake. The bias appears in every volume quintile and every year from 2021 to 2025, though it shrinks over time.
- *Apply:* This confirms down-weighting cheap contracts. Higher volume did not fix the bias, so liquidity filters address manipulation risk but not this bias.

**4.7 Walker, A. (2026).** The price is (almost) right: A calibration analysis of Polymarket pricing data. Princeton University senior thesis. https://theses-dissertations.princeton.edu/entities/publication/d5708372-5ea3-4252-b669-7f9cee07387c (fetched ✓; undergraduate work, lower evidentiary weight)
- *Finding (fetched):* Polymarket shows genuine skill (Brier skill score 0.398), with a recalibration slope of 1.112 indicating underconfidence (a favourite–longshot pattern). The bias grows with horizon and appears across domains.
- *Apply:* This independently corroborates 4.5's direction and magnitude for Polymarket.

**4.8 Sirolly, A., Ma, H., Kanoria, Y., & Sethi, R. (2025).** Network-based detection of wash trading. SSRN working paper 5714122. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5714122 (SSRN link from co-author Sethi's Substack, fetched ✓; the SSRN page itself failed to load, so unverified). Figures come from Fortune coverage (fetched ✓): https://fortune.com/2025/11/07/polymarket-wash-trading-inflated-prediction-markets-columbia-research
- *Finding (as reported):* Wash trading averaged an estimated 25% of Polymarket volume over three years, peaking around 60% in Dec 2024. Wallets showing wash-trading-consistent activity were 14% of all wallets. Shares were about 45% in sports and 17% in elections.
- *Apply:* Never use raw Polymarket volume as a liquidity or confidence weight. Use order-book depth or the cost to move the price instead.

**4.9 Clinton, J. D., & Huang, T. (2025).** Prediction markets? The accuracy and efficiency of $2.4 billion in the 2024 presidential election. Vanderbilt University working paper. The primary paper URL was **not located (unverified)**. Findings are as reported by DL News (fetched ✓): https://www.dlnews.com/articles/markets/polymarket-kalshi-prediction-markets-not-so-reliable-says-study
- *Finding (as reported):* Across about 2,500 political markets, accuracy was PredictIt ≈93%, Kalshi ≈78% and Polymarket ≈67%. Higher volume did not mean higher accuracy. Same-question prices diverged across platforms, and 58% of Polymarket's national presidential markets showed negative serial correlation, consistent with overreaction.
- *Apply:* Cross-platform disagreement is informative. Pool platforms (3.12), and smooth market prices over a few days before use to strip overreaction noise.

**4.10 Page-level evidence on AI and Anthropic markets specifically.** "PSA: Predictions markets often have very low liquidity; be careful citing them." LessWrong, 2026-03-16. https://lesswrong.com/posts/SrtoF6PcbHpzcT82T/psa-predictions-markets-often-have-very-low-liquidity-be (fetched ✓; an informal post, not peer reviewed)
- *Finding (fetched):* For several Anthropic-related markets, it would have cost tens to hundreds of dollars to move Polymarket prices by 15+ points. Kalshi spreads were about 40¢ wide, and a Manifold market saw near-zero trading for a week. A comment cites Polymarket Brier improving with volume (about 0.09 at $10k, about 0.02 at $1M+).
- *Apply:* Anthropic release markets are probably thin. Require a minimum depth, for example the dollar cost to move the price 5 points, before a market enters at full weight, and otherwise shrink it toward the model.

**4.11 Atanasov, P., Rescober, P., Stone, E., Swift, S. A., et al. (2017).** Distilling the wisdom of crowds: Prediction markets vs. prediction polls. *Management Science*, 63(3), 691–706. https://doi.org/10.1287/mnsc.2015.2374 (DOI ✓)
- *Finding (from abstract):* In 261 geopolitical events, markets beat simple averages of polls. However, team polls beat markets once aggregated with temporal decay, performance weighting and recalibration.
- *Apply:* Temporal decay (weighting recent information more) plus recalibration is a validated recipe. Apply it to your own signal stream as well as to market inputs.

**4.12 Servan-Schreiber, E., Wolfers, J., Pennock, D. M., & Galebach, B. (2004).** Prediction markets: Does money matter? *Electronic Markets*, 14(3), 243–251. https://doi.org/10.1080/1019678042000245254 (DOI ✓). Also **Hanson, R., & Oprea, R. (2009).** A manipulator can aid prediction market accuracy. *Economica*, 76(302), 304–314. https://doi.org/10.1111/j.1468-0335.2008.00734.x (DOI ✓)
- *Finding:* Servan-Schreiber et al. found play-money and real-money markets about equally accurate on NFL games. Hanson and Oprea show theoretically that manipulators can raise accuracy by subsidizing informed traders. These are standard results.
- *Apply:* Manifold (play money) is not automatically inferior, but its AI-release markets may have too few informed traders. Weight by the market's own track record on resolved AI-release questions when you can compute one.

---

## 5. Proper scoring, calibration with few events, and honest backtesting

**5.1 Gneiting, T., & Raftery, A. E. (2007).** Strictly proper scoring rules, prediction, and estimation. *Journal of the American Statistical Association*, 102(477), 359–378. https://doi.org/10.1198/016214506000001437 (DOI ✓)
- *Finding:* This is the definitive treatment of proper scoring rules (log, Brier, CRPS, interval scores) and why only proper rules reward honest forecasts. This is a standard result.
- *Apply:* Use the log score as the primary criterion, since it is the most sensitive to tail errors and the most relevant for "surprise" releases. Use Brier at fixed horizons as the interpretable secondary measure. Use CRPS on the full release-date CDF.

**5.2 Gneiting, T., Balabdaoui, F., & Raftery, A. E. (2007).** Probabilistic forecasts, calibration and sharpness. *Journal of the Royal Statistical Society, Series B*, 69(2), 243–268. https://doi.org/10.1111/j.1467-9868.2007.00587.x (DOI ✓)
- *Finding:* The paper sets out the paradigm of "maximize sharpness subject to calibration" and the PIT-histogram diagnostics for predictive distributions. This is a standard result.
- *Apply:* For each forecast origin, record the PIT value F(actual release date). Across about 25 releases, check that the PIT values are roughly uniform, which works better than binned reliability at this n.

**5.3 Murphy, A. H. (1973).** A new vector partition of the probability score. *Journal of Applied Meteorology*, 12(4), 595–600. https://doi.org/10.1175/1520-0450(1973)012<0595:ANVPOT>2.0.CO;2 (DOI ✓). Also **Brier, G. W. (1950).** Verification of forecasts expressed in terms of probability. *Monthly Weather Review*, 78(1), 1–3. https://doi.org/10.1175/1520-0493(1950)078<0001:VOFEIT>2.0.CO;2 (DOI ✓)
- *Finding:* The Brier score decomposes into reliability, resolution and uncertainty. This is a standard result.
- *Apply:* Report all three for each horizon. Use the bias-corrected version (5.4), because the naive version is biased at this sample size.

**5.4 Ferro, C. A. T., & Fricker, T. E. (2012).** A bias-corrected decomposition of the Brier score. *Quarterly Journal of the Royal Meteorological Society*, 138(668), 1954–1960. https://doi.org/10.1002/qj.1924 (DOI ✓)
- *Finding (from abstract):* In finite samples, the standard Murphy decomposition overestimates reliability error and underestimates uncertainty. An exactly unbiased decomposition is unattainable, but the authors propose one with smaller bias.
- *Apply:* With only dozens of evaluated forecasts, use this decomposition. Otherwise you will "see" miscalibration that is just small-sample bias.

**5.5 Dimitriadis, T., Gneiting, T., & Jordan, A. I. (2021).** Stable reliability diagrams for probabilistic classifiers. *PNAS*, 118(8), e2016191118. https://doi.org/10.1073/pnas.2016191118 (DOI ✓). Also **Bröcker, J., & Smith, L. A. (2007).** Increasing the reliability of reliability diagrams. *Weather and Forecasting*, 22(3), 651–661. https://doi.org/10.1175/WAF993.1 (DOI ✓)
- *Finding:* The CORP method replaces arbitrary binning with isotonic (PAV) regression, which gives stable, optimally binned reliability curves and a score decomposition, with resampling-based consistency bands. Bröcker and Smith introduce consistency bars showing how far a perfectly calibrated forecaster's diagram would scatter at a given n. These are standard results.
- *Apply:* Use CORP for the 7/30/90-day reliability diagrams and always draw consistency bands. At n≈25–100 binary outcomes, the bands will be wide, and that width is the honest message.

**5.6 Tashman, L. J. (2000).** Out-of-sample tests of forecasting accuracy: An analysis and review. *International Journal of Forecasting*, 16(4), 437–450. https://doi.org/10.1016/S0169-2070(00)00065-0 (DOI ✓). Also **Bergmeir, C., & Benítez, J. M. (2012).** On the use of cross-validation for time series predictor evaluation. *Information Sciences*, 191, 192–213. https://doi.org/10.1016/j.ins.2011.12.028 (DOI ✓)
- *Finding:* Tashman recommends rolling-origin evaluation (many forecast origins, updating as data arrive) across multiple horizons over a single holdout, and stresses avoiding information leakage. Bergmeir and Benítez study blocked cross-validation for time series. These are standard results.
- *Apply:* Use weekly forecast origins from 2024 onward. At each origin, refit using only data available then, including signals with their *original* timestamps, and score P(release ≤ 7/30/90 days) per family. Leakage from later-known leak dates is the biggest backtest risk here.

**5.7 Diebold, F. X., & Mariano, R. S. (1995).** Comparing predictive accuracy. *Journal of Business & Economic Statistics*, 13(3), 253–263. https://doi.org/10.1080/07350015.1995.10524599 (DOI ✓). Also **Harvey, D., Leybourne, S., & Newbold, P. (1997).** Testing the equality of prediction mean squared errors. *International Journal of Forecasting*, 13(2), 281–291. https://doi.org/10.1016/S0169-2070(96)00719-4 (DOI ✓)
- *Finding:* Diebold and Mariano give a test of equal expected loss between two forecasters with HAC variance for serially correlated loss differentials. Harvey, Leybourne and Newbold provide a small-sample correction (a bias-adjusted statistic with t critical values) that matters at small n. These are standard results.
- *Apply:* Weekly origins with 30- or 90-day horizons create heavily overlapping, autocorrelated loss differentials. Use the HLN-corrected DM test with HAC lag at least h−1 periods, and expect low power.

**5.8 Giacomini, R., & White, H. (2006).** Tests of conditional predictive ability. *Econometrica*, 74(6), 1545–1578. https://doi.org/10.1111/j.1468-0262.2006.00718.x (DOI ✓)
- *Finding:* The paper tests equal predictive ability of *forecasting methods*, including estimation uncertainty under rolling windows. It is valid for nested models and nonstationary data where DM-type tests are not. This is a standard result.
- *Apply:* This is the appropriate test when comparing "hierarchical TRP with signals" against "TRP alone", which are nested and refit on rolling windows.

**5.9 Bürkner, P.-C., Gabry, J., & Vehtari, A. (2020).** Approximate leave-future-out cross-validation for Bayesian time series models. *Journal of Statistical Computation and Simulation*, 90(14), 2499–2523. https://doi.org/10.1080/00949655.2020.1783262 (DOI ✓). Also **Vehtari, A., Gelman, A., & Gabry, J. (2017).** Practical Bayesian model evaluation using leave-one-out cross-validation and WAIC. *Statistics and Computing*, 27(5), 1413–1432. https://doi.org/10.1007/s11222-016-9696-4 (DOI ✓)
- *Finding:* Leave-future-out (LFO) cross-validation, made cheap with Pareto-smoothed importance sampling and occasional refits, is the time-series analogue of LOO. Ordinary LOO is invalid for forecasting evaluation. These are standard results.
- *Apply:* Use LFO expected log predictive density (elpd) to choose the power-prior a₀, the trend form and stacking weights. Do not use ordinary LOO or WAIC, which leak future information.

**5.10 Graf, E., Schmoor, C., Sauerbrei, W., & Schumacher, M. (1999).** Assessment and comparison of prognostic classification schemes for survival data. *Statistics in Medicine*, 18(17–18), 2529–2545. https://doi.org/10.1002/(SICI)1097-0258(19990915/30)18:17/18<2529::AID-SIM274>3.0.CO;2-5 (DOI ✓)
- *Finding:* The paper defines a Brier score for survival predictions under right censoring, using inverse-probability-of-censoring weighting, and its time-integrated version (the integrated Brier score, IBS). This is a standard result.
- *Apply:* At any evaluation date, some families' "next release" is still pending, which is censoring. Use the inverse-probability-of-censoring-weighted Brier or IBS rather than silently dropping open questions, which would bias evaluation toward short gaps.

**5.11 Lerch, S., Thorarinsdottir, T. L., Ravazzolo, F., & Gneiting, T. (2017).** Forecaster's dilemma: Extreme events and forecast evaluation. *Statistical Science*, 32(1), 106–127. https://doi.org/10.1214/16-STS588 (DOI ✓)
- *Finding:* Evaluating forecasts only on cases where the event occurred (or was extreme) rewards forecasters who always predict the event, even with proper scores. Weighted scoring rules are the fix. This is a standard result.
- *Apply:* Do not evaluate only "the weeks before each release". Score every origin, including long stretches where the right answer was "not yet".

**5.12 Bailey, D. H., Borwein, J. M., López de Prado, M., & Zhu, Q. J. (2016/2017).** The probability of backtest overfitting. *Journal of Computational Finance*, 20(4), 39–69. https://doi.org/10.21314/JCF.2016.322 (DOI ✓)
- *Finding:* The paper defines the probability of backtest overfitting (PBO) using combinatorially symmetric cross-validation (CSCV). This is the probability that the configuration selected as best in-sample ranks below the median out of sample, and it rises quickly with the number of configurations tried. This is a standard result.
- *Apply:* Keep a log of every model variant tried (priors, trend forms, signal sets, kernels). Compute PBO over that set using the per-origin log scores as the "returns" matrix. If PBO exceeds about 0.3, fall back to the simplest pre-registered model.

---

## 6. Reference-class forecasting and superforecasting practice

**6.1 Kahneman, D., & Lovallo, D. (1993).** Timid choices and bold forecasts: A cognitive perspective on risk taking. *Management Science*, 39(1), 17–31. https://doi.org/10.1287/mnsc.39.1.17 (DOI ✓)
- *Finding:* The paper introduces the inside-view versus outside-view distinction. Forecasts built from case specifics (the inside view) are systematically optimistic, while statistics from a reference class of similar cases (the outside view) correct this. This is a standard result.
- *Apply:* The cadence model is the outside view and the signals are the inside view. Start from the former and let signals shift it through calibrated likelihood ratios, not by narrative override.

**6.2 Flyvbjerg, B. (2006).** From Nobel Prize to project management: Getting risks right. *Project Management Journal*, 37(3), 5–15. https://doi.org/10.1177/875697280603700302 (DOI ✓). Also **Flyvbjerg, B. (2008).** Curbing optimism bias and strategic misrepresentation in planning: Reference class forecasting in practice. *European Planning Studies*, 16(1), 3–21. https://doi.org/10.1080/09654310701747936 (DOI ✓)
- *Finding:* These papers operationalize reference-class forecasting in three steps: pick a reference class, build the empirical distribution of outcomes, and position the case within it. They also document that "strategic misrepresentation" (deliberate optimism) compounds cognitive bias. These are standard results.
- *Apply:* Exec teases are subject to strategic misrepresentation (see 2.7 and 2.8). Positioning a family within its reference class means using its gap-age percentile, which the hazard model already does.

**6.3 Lovallo, D., Clarke, C., & Camerer, C. (2012).** Robust analogizing and the outside view: Two empirical tests of case-based decision making. *Strategic Management Journal*, 33(5), 496–512. https://doi.org/10.1002/smj.962 (DOI ✓)
- *Finding:* Forecasts built from several similarity-weighted analogous cases ("robust analogizing") outperform forecasts built from a single analogy or intuition. This is a standard result.
- *Apply:* For thin families (Fable, Mythos), build the reference class from several analogues: other Anthropic families, and new product lines at OpenAI and Google. Similarity-weight them, which is in effect the hierarchical prior with a competitor tier.

**6.4 Buehler, R., Griffin, D., & Ross, M. (1994).** Exploring the "planning fallacy": Why people underestimate their task completion times. *Journal of Personality and Social Psychology*, 67(3), 366–381. https://doi.org/10.1037/0022-3514.67.3.366 (DOI ✓)
- *Finding:* People predict their own completion times optimistically even when they know past tasks overran. Focusing on past experience reduces the bias. This is a standard result.
- *Apply:* Insiders' public timing hints are planning-fallacy-prone. Estimate the empirical slip distribution of Anthropic's (and competitors') stated windows and apply it.

**6.5 Tetlock, P. E., & Gardner, D. (2015).** *Superforecasting: The Art and Science of Prediction.* Crown. ISBN 978-0-8041-3669-3. Publisher page: https://www.penguinrandomhouse.com/books/227815/superforecasting-by-philip-e-tetlock-and-dan-gardner/9780804136709/ (unverified; found in search, not fetched)
- *Finding:* The book distills Good Judgment Project practice: start from the outside view, decompose the question, update frequently in small increments, keep score with Brier, and aggregate and extremize team forecasts. This is a standard result.
- *Apply:* This maps directly onto the system: base rate, then incremental likelihood-ratio updates, then Brier tracking, then extremized pooling.

**6.6 Mellers, B., Ungar, L., Baron, J., et al. (2014).** Psychological strategies for winning a geopolitical forecasting tournament. *Psychological Science*, 25(5), 1106–1115. https://doi.org/10.1177/0956797614524255 (DOI ✓). Also **Mellers, B., Stone, E., Murray, T., et al. (2015).** Identifying and cultivating superforecasters as a method of improving probabilistic predictions. *Perspectives on Psychological Science*, 10(3), 267–281. https://doi.org/10.1177/1745691615577794 (DOI ✓)
- *Finding:* Probabilistic-reasoning training (which includes reference-class use), teaming and tracking top performers each improved accuracy in the Good Judgment Project. These are standard results.
- *Apply:* When you add judgmental overrides, record them as separate forecasts and score them. Keep an override only if it beats the model under rolling-origin evaluation.

---

## 7. Forecasting AI progress and release timing

**7.1 Rahman, R. (2024).** The pace of large-scale model releases is accelerating. Epoch AI Data Insight, 2024-06-19. https://epoch.ai/data-insights/large-scale-model-releases (fetched ✓)
- *Finding (fetched):* The number of models over 10²³ training FLOP grew from 0 (2017) to 3 (2020), 36 (2022) and 205 confirmed in 2024, plus 126 likely ones.
- *Apply:* This is industry-level evidence that release intensity is trending up, which justifies a time-trend or changepoint term rather than a stationary renewal process.

**7.2 Edelman, Y., & Lee, J. (2025).** AI capabilities progress has sped up. Epoch AI Data Insight, 2025-12-23. https://epoch.ai/data-insights/ai-capabilities-progress-has-sped-up/ (fetched ✓; the page notes it has been superseded by a later Epoch analysis)
- *Finding (fetched):* Frontier Epoch Capabilities Index growth roughly doubled, from about 8 to about 15 points per year, with a breakpoint near April 2024. The bootstrap CI on the breakpoint runs from Mar 2023 to Aug 2024, with a 1.3–3.1× speedup.
- *Apply:* This supports a regime break around 2024 in the cadence model. Use it to set a prior on the changepoint location (1.9) or the power-prior discount (1.8) for 2023 data.

**7.3 Sevilla, J., Heim, L., Ho, A., Besiroglu, T., Hobbhahn, M., & Villalobos, P. (2022).** Compute trends across three eras of machine learning. arXiv:2202.05924 (IJCNN 2022). https://arxiv.org/abs/2202.05924 (arXiv ✓). Also **Cottier, B., Rahman, R., et al. (2024).** The rising costs of training frontier AI models. arXiv:2405.21015. https://arxiv.org/abs/2405.21015 (arXiv ✓)
- *Finding (from abstracts):* Training compute doubled about every 6 months in the deep-learning era, with a separate large-scale era from late 2015. Frontier training cost grew about 2.4× per year since 2016 (90% CI 2.0–2.9×).
- *Apply:* Rising cost per flagship run argues that *flagship* (Opus-class) gaps need not shrink as fast as total release counts. Allow family-specific trend slopes, partially pooled, rather than one shared acceleration.

**7.4 Kwa, T., West, B., Becker, J., et al. (2025).** Measuring AI ability to complete long software tasks. arXiv:2503.14499 (NeurIPS 2025). https://arxiv.org/abs/2503.14499 (arXiv ✓)
- *Finding (from abstract):* The 50%-task-completion time horizon of frontier models has doubled roughly every 7 months since 2019, possibly faster in 2024.
- *Apply:* This is a capability trend, not a release-timing one. It is useful only as a possible covariate, such as "capability gap since last release", and it is subject to the small-n trend-fitting cautions in 7.7.

**7.5 Mühlbacher, P., Scoblic, P., & Aldred, W. (2023).** Exploring Metaculus's AI track record. EA Forum / Metaculus, 2023-05-01. https://forum.effectivealtruism.org/posts/e9htD7txe8RDdcehm/exploring-metaculus-s-ai-track-record (fetched ✓)
- *Finding (fetched):* On 64 resolved binary AI questions, the Community Prediction scored a Brier of 0.207 and the Metaculus Prediction 0.182, against 0.25 for always predicting 50%. On 88 continuous AI questions, CRPS was 0.096 against a 0.172 baseline. The authors note AI questions may be intrinsically harder, and they did not analyze directional bias.
- *Apply:* This is a realistic benchmark. Crowd skill on AI questions is real but modest, so a well-built release model should aim to beat Brier ≈0.2 on 30-day binaries. Treat community forecasts as one input.

**7.6 Forecasting Research Institute (2025).** What did forecasters get right and wrong in the largest existential risk forecasting tournament? 2025-09-02. https://forecastingresearch.substack.com/p/what-did-forecasters-get-right-and (fetched ✓). This summarizes FRI's report "Assessing Near-Term Accuracy in the Existential Risk Persuasion Tournament".
- *Finding (fetched):* Both superforecasters and domain experts *underestimated* AI progress, and superforecasters did so more. Across four benchmarks, they gave the realized outcomes an average of 9.7% versus 24.6% for experts. For IMO gold by July 2025, the figures were 2.3% versus 8.6%.
- *Apply:* Outside-view reasoning anchored on historical cadence systematically under-predicted AI speed in 2022–25. This is direct justification for trend terms and for down-weighting old gaps, and for checking whether your backtest shows the same "too slow" bias (e.g., PIT mass piled near 0).

**7.7 titotal (2025).** A deep critique of AI 2027's bad timeline models. *Timeline Topography Tales* (Substack), 2025-06-19. https://titotal.substack.com/p/a-deep-critique-of-ai-2027s-bad-timeline (fetched ✓). The authors' reply, "Response to titotal's critique of our AI 2027 timelines model", is at https://aifuturesnotes.substack.com/p/response-to-titotals-critique-of (unverified; found in search, not fetched).
- *Finding (fetched):* The critique argues that the "superexponential" curve has a finite-time singularity independent of its starting point, and that its 10%-per-doubling parameter was given no uncertainty. With about 11 METR data points, different three-parameter curves fit equally well but diverge sharply. Backcasts were also inconsistent with the authors' own estimates.
- *Apply:* This is the cautionary tale for your trend term. With about 25 events, a log-linear trend in log-gap is the most structure the data can support. Do not fit accelerating-acceleration curves, and always show how forecasts change across trend forms.

**7.8 Karger, E., Bastani, H., Yueh-Han, C., Jacobs, Z., Halawi, D., Zhang, F., et al. (2024).** ForecastBench: A dynamic benchmark of AI forecasting capabilities. arXiv:2409.19839. https://arxiv.org/abs/2409.19839 (arXiv ✓)
- *Finding (from abstract):* On 200 sampled questions, expert human forecasters outperformed the best LLM (p < 0.001).
- *Apply:* If you use an LLM to read press or leak text and emit probabilities, treat it as a signal *extractor* (classifying whether a signal is present and its type), not as a calibrated forecaster. Calibrate its outputs like any other signal.

**7.9 Grace, K., Stewart, H., Sandkühler, J. F., et al. (2024/2025).** Thousands of AI authors on the future of AI. arXiv:2401.02843; *Journal of Artificial Intelligence Research*, 84 (2025). https://arxiv.org/abs/2401.02843 (arXiv ✓)
- *Finding (from abstract):* Aggregate expert forecasts for AI milestones moved substantially earlier between survey waves only one year apart. For example, the 50% date for machines outperforming humans on every task moved 13 years earlier.
- *Apply:* Expert expectations about AI timing are themselves nonstationary. Do not freeze a prior elicited long ago, and re-elicit or re-fit regularly.

**7.10 Armstrong, S., Bostrom, N., & Shulman, C. (2016).** Racing to the precipice: A model of artificial intelligence development. *AI & Society*, 31(2), 201–206. https://doi.org/10.1007/s00146-015-0590-y (DOI ✓). Also **Han, T. A., Pereira, L. M., Santos, F. C., & Lenaerts, T. (2020).** To regulate or not: A social dynamics analysis of an idealised AI race. *Journal of Artificial Intelligence Research*, 69, 881–921. https://doi.org/10.1613/jair.1.12225 (DOI ✓)
- *Finding:* These are game-theoretic models of AI development races. Competitive pressure (more teams, and more information about rivals' progress) pushes developers to move faster and cut safety. Han et al. analyze when racing behavior is the evolutionarily stable outcome. These are standard results.
- *Apply:* This is theoretical support for a competitor-release excitation term (2.1) and for treating known rival progress (e.g., a competitor's leaked imminent release) as a signal for Anthropic's hazard. The empirical size of the effect must come from your own data, with strong shrinkage.

---

## 8. Ranked method recommendations for this forecaster

1. **Baseline: hierarchical trend-renewal model on log inter-release gaps, with the open gap right-censored.** Use log(gap) ~ Normal or Gamma with mean α_f + β_f·(calendar time). Partially pool α_f and β_f across the five families with half-normal or half-t priors on the between-family SDs (1.1, 1.6, 1.7). Down-weight pre-2024 gaps with a power prior (a₀ chosen by leave-future-out elpd, 1.8, 5.9), or compare against a 2024 changepoint version (1.9, 7.2). Fable and Mythos forecasts will be mostly pooled, so say so. Restrict the trend to log-linear (7.7).
2. **Integrate signals in a weekly discrete-time hazard.** Use logit h_{f,w} = logit(baseline hazard from rec. 1) + Σ_k w_k·L_k·K_k(w − t_k), where L_k is the empirical log likelihood ratio for signal type k and K_k is its lead-time kernel, estimated from historical signal-to-release lags (1.3, 1.4, 3.15). Put strong shrinkage priors on the w's, because there are only about 25 events.
3. **Pool in log-odds with an explicit dependence discount, then recalibrate once.** Cluster signals by provenance (catalog leak, string, and press echo form one cluster). Within a cluster, scale the summed log-LRs by 1/(1+(n−1)ρ), starting at ρ ≈ 0.6. Across clusters, use weight 1, or a single extremizing exponent a ≥ 1 fitted out of sample (3.1, 3.6, 3.7, 3.14). Finish with a single logit-slope recalibration, because naive Bayes is overconfident (3.3, 3.13).
4. **Treat markets as a biased, partly redundant forecaster.** Recalibrate with logit(p) = b(h)·logit(p_mkt), with b ≈ 1.0 when resolution is under a day away and b ≈ 1.3 beyond a month (4.4, 4.5, 4.7). Shade contracts under 10¢ down (4.3, 4.6). Weight by order-book depth, not volume (4.8, 4.10), and pool platforms by median (3.12, 4.9). Crucially, put the market in the *same dependence cluster* as public leaks once a leak is public, so the same information is not counted twice.
5. **Combine component forecasts with fixed equal weights in a log pool.** The components are the cadence baseline, the signal hazard and the recalibrated market. Allow at most one fitted parameter (the extremizing or recalibration exponent). Move to stacking on leave-future-out log scores only after about 40 or more scored origins (3.4, 3.8–3.11).
6. **Evaluate by rolling origin with timestamp-honest replay.** Use weekly origins from 2024 onward, with each signal entering only at its original public date. Score with the log score (primary), Brier at 7/30/90 days, CRPS or PIT on the release-date CDF, and a censoring-weighted Brier or IBS for open gaps. Use the Ferro–Fricker decomposition, CORP reliability with consistency bands, and score *all* origins, not just pre-release ones (5.1–5.6, 5.10, 5.11).
7. **Guard against overfitting.** Pre-register a small model grid and log every variant tried. Compute PBO via CSCV, and above about 0.3 revert to the simplest model. Compare nested models with the Giacomini–White test and non-nested ones with HLN-corrected Diebold–Mariano with HAC (lag ≥ h−1), and treat p-values as indicative given low power (5.7, 5.8, 5.12).
8. **Encode inside-view structure as small, shrunk covariates, not bespoke models.**
   - Exec teases and stated windows carry an empirical right-skewed slip distribution (2.7, 2.8, 6.4).
   - A competitor frontier release adds a decaying excitation covariate exp(−Δt/τ), with a prior half-life of a few weeks, interacting with gap age. Do not fit a full Hawkes model (2.1, 2.11, 7.10).
   - IPO or S-1 status is a regime indicator with a weak prior that changes the reliability of dated commitments (2.9, 2.10).
   - Check the outside view against OpenAI and Google cadences as a second-tier reference class (6.1, 6.3, 7.6).

---

## Items dropped or not verified
- **Clinton & Huang (2025):** the primary paper was not found online. Only the press-reported findings are used, and they are labelled as such.
- **Sirolly et al. (2025):** the SSRN page would not load. Figures are from Fortune.
- **Tetlock & Gardner** publisher page and the **AI 2027 authors' response**: URLs were found in search but not fetched.
- **Lovallo & Kahneman (2003)** "Delusions of success" (HBR) was omitted because it was not verified. Kahneman & Lovallo (1993) covers the same idea.
- I found **no peer-reviewed study that specifically forecasts frontier-model release dates or measures the accuracy of prediction markets on AI-release questions**. The closest evidence is 7.5 (Metaculus AI questions in general) and the informal liquidity evidence in 4.10. Your own backtest will be the first real evidence on that question.
