# AIthicsScore

**Ethical Risk Scoring for AI Solutions**  
[GitHub Repository](https://github.com/prakas-sysadmin/AIthicsScore.git)

AIthicsScore is a toolkit for evaluating the ethical risks associated with AI/ML models. It leverages a variety of libraries to assess fairness, explainability, data privacy, and more to generate an ethical score for AI systems. This project aims to help developers, data scientists, and organizations build responsible and transparent AI systems.

---

## 🚀 Features

- ⚖️ Fairness analysis with [Fairlearn](https://fairlearn.org/)
- 🔍 Privacy risk detection using [Presidio](https://microsoft.github.io/presidio/)
- 🧠 Model explainability with SHAP and LIME
- 📊 Visual analytics using Matplotlib
- 📝 Automated scoring reports in PDF
- 📈 Streamlit-based interactive UI

---

## 🔧 Setup Instructions

Follow these steps to get the project up and running:

### 1. Clone the Repository

```bash
git clone https://github.com/prakas-sysadmin/AIthicsScore.git
cd AIthicsScore


### 2. Check python version

```bash
python3 -V

### 3. Create/Setup python virtual environment by the below command.

```bash
python3 -m venv venv

### 4. Enable/Activate the python virtual environment

```bash
source venv/bin/activate

### 5. Check pip version

```bash
pip -V

### 6. Install Python liberies like (pandas fairlearn presidio-analyzer scikit-learn matplotlib fpdf shap lime joblib streamlit).

```bash
pip install pandas fairlearn presidio-analyzer scikit-learn matplotlib fpdf shap lime joblib streamlit 


### 7. Finally run project by below commands

```bash
streamlit run app.py

![image](https://github.com/user-attachments/assets/ff314c50-b11c-42a5-9946-8e0e8283978f)
