# Research Notes: AI-Assisted Cancer Detection

## Chosen innovation
AI-assisted cancer detection and diagnostic decision support. AI models can analyze patterns in medical data and may help clinicians prioritize or interpret findings. This project uses a public breast-tumor measurement dataset as a small educational demonstration of classification.

## Why it matters
Cancer diagnosis can involve complex imaging and pathology workflows. Machine-learning systems may help identify patterns or prioritize cases, but model output must be assessed in the context of clinical evidence, intended use, workflow, and patient safety.

## Recent real-world research
A 2026 *Nature Medicine* paper, “AI-based chest X-ray prioritization in the lung cancer diagnostic pathway: the LungIMPACT randomized controlled trial,” reports a prospective, multicentre randomized controlled trial investigating whether immediate AI prioritization of chest X-rays affected time to CT and lung-cancer diagnosis. This is an example of evaluating AI as part of a clinical pathway rather than assuming that model accuracy alone proves clinical benefit.

## Regulatory context
The U.S. FDA maintains a public list of AI-enabled medical devices authorized for marketing in the United States. The existence of this list illustrates that healthcare AI products have intended uses and applicable premarket requirements. A classroom prototype is not automatically a cleared or approved medical device.

## Prototype design
- Load a public dataset bundled with scikit-learn.
- Split examples into training and held-out test sets.
- Standardize measurements and train logistic regression.
- Report accuracy and classification metrics.
- Display an example prediction with a clear educational-use warning.

## Evaluation and limitations
The prototype is useful for demonstrating a complete ML workflow, but its single test split is not sufficient evidence for clinical performance. It does not analyze raw images, does not represent a prospective clinical evaluation, and should never be used for real diagnosis. A future academic extension could compare models, examine false negatives and false positives, assess calibration, and study subgroup performance using an appropriately documented dataset.

## Sources
1. UCI Machine Learning Repository: https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic
2. scikit-learn dataset documentation: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html
3. FDA AI-enabled medical devices: https://www.fda.gov/medical-devices/digital-health-center-excellence/artificial-intelligence-enabled-medical-devices
4. Nature Medicine (2026), LungIMPACT randomized controlled trial: https://www.nature.com/articles/s41591-026-04253-5
