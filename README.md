# 🛡️ SpamShield AI — Email Spam Detector

A powerful, full-featured spam email detection system built with **Python**, **Streamlit**, and **scikit-learn**, featuring multiple ML algorithms, a stunning dark-mode UI, file upload support, user authentication, and a complete admin panel.

---

## ✨ Features

### 👤 User Features
- **Signup / Login** with bcrypt-secured passwords
- **Manual email input** (subject + body)
- **File upload** — scan `.txt` and `.pdf` files
- **Spam / Not Spam** prediction with confidence gauge
- **Dark mode UI** with glassmorphism design
- **Personal dashboard** with charts
- **Scan history** with filters and CSV export

### 🛡️ Admin Features
- View **all scan records** across all users
- **Delete** individual records or clear all history
- **User management** — create/delete users, assign roles
- Platform-wide **statistics dashboard**

### 🤖 ML Models
| Model | Notes |
|---|---|
| Naive Bayes | Fast, great baseline |
| Logistic Regression | Excellent F1, interpretable |
| Random Forest | Robust ensemble method |
| SVM (LinearSVC) | High accuracy on text |

---

## 📁 Project Structure

```
spam-email-detector/
│
├── app.py                   # Main Streamlit entry point
├── requirements.txt
├── README.md
│
├── .streamlit/
│   └── config.toml          # Dark theme config
│
├── model/
│   ├── ml_engine.py         # Training + prediction engine
│   └── *.pkl                # Saved trained models
│
├── dataset/
│   └── spam.csv             # Your dataset (upload via UI)
│
├── auth/
│   ├── auth_manager.py      # Signup/login/bcrypt
│   └── users.json           # User store
│
├── utils/
│   ├── preprocessor.py      # NLTK text preprocessing
│   ├── file_handler.py      # PDF/TXT extraction
│   ├── history_manager.py   # Scan history CRUD
│   ├── charts.py            # Plotly visualisations
│   ├── dashboard_page.py    # Dashboard UI
│   ├── scan_page.py         # Scan email UI
│   ├── history_page.py      # History UI
│   ├── training_page.py     # Model training UI
│   └── admin_page.py        # Admin panel UI
│
├── history/
│   └── scan_history.json
│
└── uploads/                 # Uploaded files cache
```

---

## 🚀 Quick Start

### 1. Clone / open the project
```bash
cd spam-email-detector
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Get a dataset
Download the **SMS Spam Collection** or **Email Spam dataset** from Kaggle:
- [Spam Email Dataset](https://www.kaggle.com/datasets/balaka18/email-spam-classification-dataset-csv)
- [SMS Spam Collection](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)

Place the CSV file in the `dataset/` folder, or upload it via the **Train Models** page.

### 4. Run the app
```bash
streamlit run app.py
```

### 5. Login
Default admin credentials:
- **Username:** `admin`
- **Password:** `admin123`

---

## 📊 Dataset Format

The app auto-detects common column names:

| Label Column | Text Column |
|---|---|
| `label`, `v1`, `class`, `category`, `spam` | `text`, `v2`, `message`, `email`, `body`, `content` |

Label values accepted: `spam`/`ham`, `1`/`0`, `yes`/`no`

---

## ☁️ Deploy to Streamlit Community Cloud

1. Push this folder to a **GitHub repository**
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repo → set `app.py` as the entry point
4. Deploy!

> **Note:** The `history/` and `auth/` data won't persist across redeploys on the free tier. Consider using a database (SQLite, Firebase) for production.

---

## 🔒 Security Notes

- Passwords are hashed with **bcrypt** (not stored in plaintext)
- Admin role required for admin panel access
- Session state cleared on logout

---

## 📦 Dependencies

```
streamlit, pandas, numpy, scikit-learn,
matplotlib, seaborn, nltk, PyPDF2,
joblib, plotly, bcrypt, Pillow, wordcloud
```

---

## 📄 License
MIT License — free for personal and commercial use.
