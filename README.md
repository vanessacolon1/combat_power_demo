# Combat Power Dashboard

The **Combat Power Dashboard** is an interactive Streamlit application designed for military commanders and analysts to explore, update, and analyze unit combat power data. The dashboard provides tools to view unit readiness, adjust FMC/NMC totals, and perform hierarchy-based analysis.

---

## Features

1. **Home Page**
   - Overview of all units and their combat power.
   - Quick snapshot of key metrics (`oh_gcss`, `total_fmc_gcss`, `total_nmc_supply`, `total_nmc_maintenance`).

2. **Search UIC**
   - Allows commanders to enter a **Unit Identification Code (UIC)** and view its current combat power status.

3. **Update Combat Power**
   - Adjust `Total FMC GCSS`, `Total NMC Supply`, and `Total NMC Maintenance` for a specific unit.
   - Changes are **saved to the dataset** to reflect real-time readiness.

4. **Analysis**
   - Aggregate combat power by **UIC hierarchy** (e.g., brigade, battalion).
   - Bar charts and tables for FMC, NMC totals.
   - Overall summary statistics for quick assessment.

---

## Dataset

The app expects a **combat power CSV file** with the following columns:

| Column | Description |
|--------|-------------|
| uic | Unit Identification Code |
| uic_hierarchy | Higher-level organizational hierarchy |
| uic_name | Unit name |
| oh_gcss | On-hand equipment count |
| total_fmc_gcss | Fully Mission Capable equipment |
| total_nmc_supply | Non-Mission Capable due to supply |
| total_nmc_maintenance | Non-Mission Capable due to maintenance |
| equipment_description | Description of the equipment |
| model | Equipment model |

> The default dataset is `combat_power.csv`. The app also supports uploading custom datasets.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/combat_power_demo.git
cd combat_power_demo
```

2. Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## Usage

Run the Streamlit app:

```bash
streamlit run combat_power_app.py
```

- Navigate between pages using the sidebar.
- Search or update UICs.
- Perform hierarchy-based analysis.

---

## Dependencies

- Python >= 3.9  
- pandas  
- streamlit  

You can install them via `pip install -r requirements.txt`.

---

## Notes

- Changes to combat power values are **saved persistently** in `combat_power.csv`.  
- Use the **Analysis** page to get an overview of readiness across multiple units.  
- Ensure that the `uic` values are unique for proper searching and updating.

---

## License

This project is licensed under the MIT License.
