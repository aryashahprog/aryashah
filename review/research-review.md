# Research paper: author review notes

Review notes for `review/papers/prematurity-brain-cognition.md` and its PDF. This file is not built into the site or the PDF, but the repository is public, so anything written here is publicly visible.

## Provenance

- Every study-specific method and result in the paper comes from the conference poster (`static/research/prematurity-brain-cognition.pdf`). No analyses were rerun.
- The outside references are used for background and interpretation only, and each was checked against PubMed, WHO or ACOG.
- Grant numbers were checked against NIH RePORTER: R01MH130595 (PI Jingyu Liu, Georgia State University) and R34DA061483 (Georgia State University). The poster prints the first as "R01-MH13 0595".
- Figures 2 and 3 are the poster's own embedded result images, extracted at native resolution and cropped to the panel. Figure 3 omits the poster's Picture Vocabulary example screen. Figure 1 is a new schematic of the steps the poster documents.
- Left out of the paper on purpose: the poster's separate sagittal MRI image of the cuneus (its source isn't known), the poster's "Cuneus Develops Differently" cartoon, and the mediation diagram with its path coefficients.

## Mediation: why it is not a Results subsection

The poster's path values don't fit together as one model:

- **Signs:** if gestational age is coded in weeks, the group results imply that a (gestational age to cuneus) should be negative and c (total effect) positive. The poster shows a = 0.23, b = −0.24, c = −1.33 and c′ = −1.27.
- **Percentage:** the reported 4.1% matches a×b/c (about 4.15%), but not (c − c′)/c (about 4.5%).

Until the full model output is checked, the paper mentions the 4.1% figure only in the Discussion. There it is attributed to the poster, and the paper says it needs evaluation using the full model output and longitudinal validation. To restore a mediation subsection, the paper needs:

- the model specification and coding of gestational age
- the indirect-effect test and its confidence interval
- confirmation of the signs of the coefficients

## Questions for the authors

- **Sample:**
  - How was the 3,135-person cohort derived from ABCD?
  - Is it the analytic N for every model, or did the N differ by outcome?
  - What does "Sample Cohort-1" on the poster refer to?
- **Timepoint:** what were the ABCD data release, the study visit and the age range at the MRI and cognitive assessments?
- **Gestational groups:**
  - What full-term cutoff was used, and how were 37- and 38-week births handled?
  - What was the source of gestational age (caregiver report)?
- **Imaging:**
  - What preprocessing and quality control were done?
  - For moo-ICAr: what template, what number and type of components, and what citation?
  - What units is the plotted GM measure in?
  - Were intracranial or total brain volume adjusted for?
- **Models:**
  - Why do group and continuous gestational age appear in the same model?
  - Was age at assessment a covariate?
  - Was family or twin relatedness modelled?
  - What software was used?
- **Multiple comparisons:**
  - What significance threshold and correction were used across the 100 regions and 7 tests?
  - Which are the other four significant regions, and why was the cuneus chosen?
- **Figures:** what do the vertical bars in the GM plot and the box outlines in the vocabulary plot show?
- **Statistics:**
  - The poster prints "p = < 1.77e-3" and "p = < 2.45e-8". The paper shows these as "<". Exact p-values and degrees of freedom would be better.
  - Was the Picture Vocabulary score raw, uncorrected standard or age-corrected? What were the results for the other six NIH Toolbox tests?
- **Other covariates:** were birth weight, multiple birth, neonatal complications or socioeconomic factors considered?
- **Compliance:**
  - an ethics statement (ABCD IRB and local data use approval)
  - the ABCD Data Use Certification and the required ABCD acknowledgement text
  - a data availability statement
- **Venue:** what were the poster's venue and date?
- **Contributions and approval:** author contributions, and review and approval of the paper text by Dawn Jensen, Vince Calhoun and Jingyu Liu.
