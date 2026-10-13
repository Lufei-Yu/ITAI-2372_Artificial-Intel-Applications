# AI Healthcare Innovation Demo: Breast Tumor Classification

## Project overview
This beginner-friendly Streamlit application demonstrates how machine learning can classify numeric measurements in a public breast-tumor dataset as **benign** or **malignant**. It is inspired by the broader healthcare innovation of AI-assisted cancer detection and decision support.

The app trains a baseline logistic-regression model, reports held-out test accuracy, displays a confusion matrix and classification report, and lets the user inspect predictions for examples from the test set.

> **Safety notice:** This is a classroom prototype only. It is not clinically validated, is not a medical device, and must not be used to diagnose cancer or make patient-care decisions.

## Innovation and research context
AI is increasingly used in healthcare to support image analysis, diagnostic workflows, and prioritization. For example, the 2026 *Nature Medicine* LungIMPACT randomized controlled trial studied AI-based prioritization of chest X-rays in a lung-cancer diagnostic pathway. The FDA also maintains a list of AI-enabled medical devices authorized for marketing in the United States. These real-world systems require evidence, oversight, and evaluation for their intended use.

This project is a much smaller educational example. It uses measurements already extracted from digitized fine-needle aspirate images; it does **not** read raw X-ray or pathology images and it is not equivalent to a regulated clinical system.

## Data source
The app uses `sklearn.datasets.load_breast_cancer`, which distributes the Wisconsin Diagnostic Breast Cancer dataset. The dataset contains numeric features computed from digitized images of fine-needle aspirates. It is loaded by scikit-learn, so no separate data download is needed.

- UCI dataset page: https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic
- scikit-learn documentation: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html

## Technologies
- Python
- Streamlit
- pandas
- scikit-learn
- Logistic Regression
- StandardScaler
- Train/test split and classification metrics

## Run in Google Colab
You can install the requirements in a Colab cell, but Streamlit needs a tunnel or a hosting service to display its web interface. The simplest option is to run it locally or deploy it using Streamlit Community Cloud after uploading the repository to GitHub...


## Limitations and responsible AI
- The model is for learning only and is not clinically validated.
- One train/test split is not enough to establish safety or clinical usefulness.
- Dataset patterns may not generalize across hospitals, populations, or equipment.
- Real-world use would require rigorous external validation, privacy and security protections, human oversight, workflow assessment, and regulatory review as applicable.
- Never upload real patient information to this demonstration.

## References
1. UCI Machine Learning Repository. *Breast Cancer Wisconsin (Diagnostic) Data Set.* https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic
2. scikit-learn. *load_breast_cancer.* https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html
3. U.S. Food and Drug Administration. *Artificial Intelligence-Enabled Medical Devices.* https://www.fda.gov/medical-devices/digital-health-center-excellence/artificial-intelligence-enabled-medical-devices
4. Woznitza, N. et al. (2026). *AI-based chest X-ray prioritization in the lung cancer diagnostic pathway: the LungIMPACT randomized controlled trial.* Nature Medicine. https://www.nature.com/articles/s41591-026-04253-5
