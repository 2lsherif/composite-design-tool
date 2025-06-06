# Custom Composite Design Tool

A web-based tool to recommend natural fiber composites based on mechanical properties and cost criteria.

## 🔧 Features

- Material database (fibers & resins)
- Flask web interface
- PostgreSQL data storage
- Recommendation engine
- Data visualization with charts
- Dockerized deployment

## 🚀 Technologies Used

- Python
- Flask
- PostgreSQL
- SQLAlchemy
- Pandas
- Matplotlib
- Docker
- HTML/CSS + Bootstrap
- Git & GitHub

## 📁 Project Structure

composite-tool/
├── app.py
├── config.py
├── data
│   ├── clean_fibers.csv
│   ├── clean_resins.csv
│   ├── raw_fibers.csv
│   └── raw_resins.csv
├── docs
│   └── data_process.md
├── __pycache__
│   └── config.cpython-312.pyc
├── README.md
├── requirements.txt
├── scripts
│   └── preprocess_data.py
├── static
│   └── style.css
├── templates
│   └── index.html
├── tests
│   └── __init__.py
└── venv
    ├── bin
    ├── include
    ├── lib
    ├── lib64 -> lib
    └── pyvenv.cfg


## 📌 Setup Instructions

```bash
git clone https://github.com/2lsherif/composite-design-tool.git
cd composite-design-tool
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

📬 Contact

Created by [Elsherif Emad](https://www.linkedin.com/in/elsherif-abdelrahman-2a03651ba/) — feel free to reach out!
