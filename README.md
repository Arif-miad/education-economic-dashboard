



````markdown
# 🌍 How Education Drives Economic Growth - Interactive Dashboard

## 🔹 Project Overview

This project is an **interactive, professional Streamlit dashboard** that explores how **education (literacy rate)** and **healthcare (physician density)** influence economic growth across different countries.  
Users can interactively filter data, explore visualizations, and analyze feature importance to understand the key drivers of **GDP growth**.

**✨ Key Features:**

- 🔐 Interactive **Login Page** with background image  
- 🧭 5-page **Navigation Structure**:
  1. **Home:** Dataset overview, summary stats, missing values  
  2. **Basic Plots:** Histogram, Count/Bar, Box, KDE  
  3. **Advanced Plots:** Scatter, Violin, Pairplot, Heatmap, Pie, Line plots  
  4. **Feature Analysis:** Random Forest feature importance + GDP correlation  
  5. **About:** Dataset and project overview  
- 🌎 Interactive filters for **Continent** & **GDP per Capita Category**  
- 🎨 Fully responsive **UI with custom CSS styling**  
- 📊 Plotly-powered **interactive charts**  
- ☁️ Ready for **deployment** on Streamlit Cloud, Heroku, or AWS  

---

## 🔹 Dataset

**File:** `how-education-drives-economic-growth.csv`

| Column | Description |
|--------|--------------|
| Country | Name of the country |
| Literacy Rate | Percentage of literate population |
| Physician Density | Physicians per 1,000 people |
| GDP (Current USD) | Gross Domestic Product |
| GDP Growth (% Annual) | Annual GDP growth rate |
| GDP per Capita (Current USD) | GDP divided by population |
| GDP per Capita Category | Categorized GDP level (Low/Mid/High) |
| Unemployment Rate (%) | National unemployment rate |
| Continent | Continent name |

---

## 🔹 Technologies & Frameworks Used

| Category | Technology / Framework |
|-----------|-----------------------|
| Programming Language | Python 3.10+ |
| Web Framework | Streamlit |
| Data Analysis | Pandas, NumPy |
| Visualization | Plotly, Seaborn, Matplotlib |
| Machine Learning | Scikit-learn (Random Forest), XGBoost (optional) |
| Styling | HTML, CSS |
| Version Control | Git & GitHub |

---

## 🔹 Installation & Running the App

Follow these simple steps to set up the project locally 👇

```bash
# 1️⃣ Clone the repository
git clone https://github.com/Arif-miad/education-economic-dashboard.git
cd education-economic-dashboard

# 2️⃣ Create a virtual environment
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate     # For Windows

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Run the Streamlit app
streamlit run professional_dashboard.py
````

✅ Open your browser at `http://localhost:8501` to explore the dashboard.

---

## 🔹 Screenshots

### 🧭 Navigation Bar

<img src="https://github.com/Arif-miad/education-economic-dashboard/blob/main/assets/navigation.PNG" width="70%" height="70%">

### 🔐 Login Page

<img src="https://github.com/Arif-miad/education-economic-dashboard/blob/main/assets/login.PNG" width="70%" height="70%">

### 🏠 Home Page

<img src="https://github.com/Arif-miad/education-economic-dashboard/blob/main/assets/home.PNG" width="70%" height="70%">

### 📊 Basic Plots

<img src="https://github.com/Arif-miad/education-economic-dashboard/blob/main/assets/basic.PNG" width="70%" height="70%">

### 📈 Advanced Plots

<img src="https://github.com/Arif-miad/education-economic-dashboard/blob/main/assets/advance.PNG" width="70%" height="70%">

### 🧩 Feature Analysis

<img src="https://github.com/Arif-miad/education-economic-dashboard/blob/main/assets/feature.PNG" width="70%" height="70%">

---

## 🔹 Project Folder Structure

```
education_economic_dashboard/
│
├── data/
│   └── how-education-drives-economic-growth.csv
├── assets/
│   ├── login.png
│   ├── home.png
│   ├── basic.png
│   ├── advance.PNG
│   └── feature.png
├── utils/
│   ├── preprocessing.py
│   ├── plotting.py
│   └── feature_analysis.py
├── professional_dashboard.py
├── requirements.txt
└── README.md
```

---

## 🔹 Deployment

You can deploy the project easily on:

* 🌐 **Streamlit Cloud:** [https://share.streamlit.io](https://share.streamlit.io)
* ☁️ **Heroku / AWS / Render**
* 💻 Or run locally via `streamlit run professional_dashboard.py`

---

## 🔹 Contributing

Contributions are welcome!
If you’d like to improve the dashboard or add features:

1. Fork the repository
2. Create your feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m "Add feature name"`
4. Push to the branch: `git push origin feature-name`
5. Open a Pull Request 🎉

---

## 🔹 Contact & Links

| Platform    | Link                                                                                         |
| ----------- | -------------------------------------------------------------------------------------------- |
| 🌍 GitHub   | [https://github.com/Arif-miad](https://github.com/Arif-miad)                                 |
| 💼 LinkedIn | [https://www.linkedin.com/in/Arif-miad](www.linkedin.com/in/arif-miah-8751bb217)               |
| 📊 Kaggle   | [https://www.kaggle.com/Arif-miad](https://www.kaggle.com/miadul)                         |
| 🎥 YouTube  | [https://www.youtube.com/channel/your-channel](https://www.youtube.com/@intelliaiworld) |
| ✉️ Email    | [your.email@example.com](arifmiahcse@gmail.com)                                      |

---

## 🔹 License

📝 This project is licensed under the **MIT License** – see the [`LICENSE`](LICENSE) file for details.

---

## ⭐ Acknowledgment

Special thanks to the open data community and contributors who made this project possible.
If you like this project, don’t forget to **⭐ Star the repo** on GitHub!

---

```

---


```
