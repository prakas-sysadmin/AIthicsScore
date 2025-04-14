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
```

### 2. Check python version

```bash
python3 -V
```
![image](https://github.com/user-attachments/assets/95b9935c-3f78-48aa-aac6-b02415fa7cf2)


### 3. Create/Setup python virtual environment by the below command.

```bash
python3 -m venv venv
```
![image](https://github.com/user-attachments/assets/b35deac3-a896-4919-8198-3c450cf56946)


### 4. Enable/Activate the python virtual environment

```bash
source venv/bin/activate
```
![image](https://github.com/user-attachments/assets/f163205e-54e9-41d9-9449-6fddf36af51a)


### 5. Check pip version

```bash
pip -V
```
![image](https://github.com/user-attachments/assets/d115ad8e-028a-4aec-b2a0-5820d64ff810)


### 6. Install Python liberies like (pandas fairlearn presidio-analyzer scikit-learn matplotlib fpdf shap lime joblib streamlit).

```bash
pip install pandas fairlearn presidio-analyzer scikit-learn matplotlib fpdf shap lime joblib streamlit 
```

### 7. Finally run project by below commands

```bash
streamlit run app.py
```
![image](https://github.com/user-attachments/assets/ff314c50-b11c-42a5-9946-8e0e8283978f)

### 8. Finally the our UI is working!
![image](https://github.com/user-attachments/assets/8f77062e-920a-44e1-bd77-f625851d6d42)

### 9. Uploaded a Datasets in CSV Format.
![image](https://github.com/user-attachments/assets/670ed80f-7d48-4673-aaac-15e9b480713d)

![image](https://github.com/user-attachments/assets/68a85912-7968-4f01-9f50-d86bac35fcc4)

![image](https://github.com/user-attachments/assets/ea10240b-8047-4975-b801-89f9892e1b21)

### 10. Now its showing our scores.
![image](https://github.com/user-attachments/assets/bc164c27-c4ce-42e4-95ab-8b0b221205c8)

![image](https://github.com/user-attachments/assets/5ceb4406-69f9-49c4-b6a3-fe7373a7fa61)

![image](https://github.com/user-attachments/assets/d47b7950-f438-47f6-bacb-889627a97a92)







