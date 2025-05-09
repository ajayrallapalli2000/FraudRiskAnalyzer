# Fraud Risk Analyzer 🔍

**Fraud Risk Analyzer** is a Streamlit-based application that analyzes uploaded documents (.txt, .docx, .pdf) to automatically detect and highlight fraud-related keywords.  

Designed for **audit teams**, this tool leverages **Natural Language Processing (NLP)** and **machine learning techniques such as classification** to accelerate detection of potential fraud, corruption, bribery, and contract risks within unstructured documents.

---

## 🚀 Features

- Upload and process `.txt`, `.docx`, and `.pdf` files
- Highlight fraud risk keywords with **different pastel colors** based on risk category
- Dynamic **multi-category selection** (Fraud, Bribery, Compliance Violation, Contract Risk, Financial Misconduct, Money Laundering, Corruption)
- **Word-by-word** accurate highlighting (no broken spaces)
- **Download highlighted Word document** with original filename preserved
- **Download CSV report** showing occurrence counts for each detected keyword
- Visual **legend** mapping colors to risk categories and keywords
- Intuitive and lightweight **Streamlit UI**

---

## 🛠 Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/yourusername/fraud-risk-analyzer.git
cd fraud-risk-analyzer
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:

```bash
streamlit run app.py
```

---

## 📄 File Structure

```plaintext
fraud-risk-analyzer/
├── app.py                  # Main Streamlit application
├── fraud_keyword_detector.py # Risk categories, keywords, colors
├── requirements.txt         # List of Python dependencies
└── README.md                # Project documentation (this file)
```

---

## 📈 Results
When you run the application and upload a document for analysis:

- The app processes and highlights relevant fraud-related keywords using predefined keyword lists and classification logic
- The text is rendered with color-coded highlights, based on selected risk categories
- A visual legend displays color-category-keyword mapping
- Downloads are generated for:
  - A Word document containing all highlighted content
  - A CSV keyword report listing detected terms and frequency

These outputs help streamline document review, making fraud detection, compliance verification, and audit planning significantly faster and more efficient.

---

## 🧠 Technologies & Techniques Used

- Python, Streamlit, docx2txt, PyMuPDF, NLTK
- NLP for keyword extraction
- Machine learning techniques such as classification for structured fraud risk identification
- Color-based category mapping
- Dynamic multi-category selection and document parsing

---

## 📦 Risk Categories & Colors

| Category | Highlight Color | Example Keywords |
|:---------|:----------------|:-----------------|
| Fraud | Light Red (#FFB6C1) | fraud, embezzlement, kickback, forgery, deception |
| Bribery | Light Orange (#FFD580) | bribe, inducement, gratuity, payoff |
| Compliance Violation | Light Yellow (#FFFF99) | non-compliance, penalty, violation, illegal |
| Contract Risk | Light Blue (#ADD8E6) | breach, lawsuit, dispute, settlement |
| Financial Misconduct | Light Green (#90EE90) | misstatement, manipulation, concealment |
| Money Laundering | Light Teal (#B2DFDB) | laundering, offshore account, shell company |
| Corruption | Light Violet (#E1BEE7) | corruption, collusion, favoritism, nepotism |

---

## 📈 Keyword Occurrence Report

After analyzing the document, you can download a **CSV report** that shows the number of times each fraud-related keyword appears.

Example CSV:

| Keyword | Occurrences |
|:--------|------------:|
| fraud   | 3           |
| breach  | 2           |
| bribery | 1           |

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

Developed by **Ajay Rallapalli** | Northeastern University | Spring 2025
