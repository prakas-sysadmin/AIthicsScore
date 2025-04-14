import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from bias_checker import check_bias
from privacy_checker import check_privacy
from governance_checker import check_governance
from utils import calculate_final_score
from report_generator import generate_pdf_report
import os

st.set_page_config(page_title="AIthics Score", layout="wide")
st.title("🤖 AIthics Score – Ethical Risk Scoring for AI Models")

# Tabbed layout
tab1, tab2, tab3 = st.tabs(["📁 Upload & Analyze", "📊 Results", "💡 Recommendations"])


def plot_score_pie(bias, privacy, governance):
    labels = ['Bias/Fairness', 'Privacy', 'Governance']
    scores = [bias, privacy, governance]

    fig, ax = plt.subplots()
    ax.pie(scores, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)


with tab1:
    st.header("Upload Dataset & Answer Ethics Questions")
    data_file = st.file_uploader("Upload dataset (CSV)", type=["csv"])

    if data_file:
        df = pd.read_csv(data_file)
        st.write("📊 Data Preview:", df.head())

        st.subheader("Governance Questions")
        q1 = st.radio("1. Do you document model decisions?", ["Yes", "No"])
        q2 = st.radio("2. Do you track model versions?", ["Yes", "No"])
        q3 = st.radio("3. Do you conduct regular bias audits?", ["Yes", "No"])
        q4 = st.radio("4. Is user data collected with consent?", ["Yes", "No"])
        q5 = st.radio("5. Can your model's decisions be explained to end users?", ["Yes", "No"])

        answers = {'q1': q1, 'q2': q2, 'q3': q3, 'q4': q4, 'q5': q5}

        if st.button("🧠 Run Ethical Analysis"):
            bias_score, bias_detail = check_bias(df)
            privacy_score, pii_issues = check_privacy(df)
            governance_score = check_governance(answers)
            total_score = calculate_final_score(bias_score, privacy_score, governance_score)

            # Store in session state
            st.session_state['analysis_done'] = True
            st.session_state['scores'] = {
                'bias': bias_score,
                'privacy': privacy_score,
                'governance': governance_score,
                'total': total_score
            }
            st.session_state['bias_detail'] = bias_detail
            st.session_state['pii_issues'] = pii_issues

            st.success("✅ Analysis completed! Check the 'Results' tab.")

with tab2:
    if st.session_state.get('analysis_done'):
        scores = st.session_state['scores']
        st.markdown(f"### 🎯 Final AIthics Score: {scores['total']}/100")
        st.progress(scores['total'] / 100)

        st.markdown("#### 🔍 Score Breakdown:")
        st.write("**Bias Score:**", scores['bias'], st.session_state['bias_detail'])
        st.write("**Privacy Score:**", scores['privacy'], st.session_state['pii_issues'])
        st.write("**Governance Score:**", scores['governance'])

        st.markdown("#### 📊 Score Distribution:")
        plot_score_pie(scores['bias'], scores['privacy'], scores['governance'])

        if st.button("📄 Download PDF Report"):
            filename = "AIthics_Report.pdf"
            generate_pdf_report(filename, scores, {
                'Bias Details': str(st.session_state['bias_detail']),
                'Privacy Issues': str(st.session_state['pii_issues']),
            })

            with open(filename, "rb") as f:
                st.download_button("Download Report", f, file_name=filename, mime='application/pdf')
            os.remove(filename)
    else:
        st.info("Run an analysis first in the 'Upload & Analyze' tab.")

with tab3:
    st.header("💡 Recommendations to Improve Your AI Ethics Score")

    st.markdown("""
    ### ✅ Reduce Bias
    - Rebalance your dataset using re-sampling or synthetic data generation.
    - Apply tools like [Fairlearn](https://fairlearn.org/) or [AIF360](https://aif360.mybluemix.net/).

    ### ✅ Improve Transparency
    - Use model explainers (e.g., SHAP, LIME).
    - Provide end users with understandable reasons for AI decisions.

    ### ✅ Strengthen Privacy
    - Remove or mask personally identifiable information (PII).
    - Limit data collection to only what's necessary.

    ### ✅ Ensure Strong Governance
    - Track model versions and decision logs.
    - Perform internal audits and share documentation with stakeholders.
    """)

