
# 🌿 **How to Run ViSAGE 1.0**  
*A complete step‑by‑step guide for Natural England and project collaborators*

---

## **1. Install the environment**

ViSAGE requires Python 3.10+ and a small set of geospatial libraries.

Create and activate a virtual environment:

```
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

```

---

## **2. Prepare your input data**

Place your datasets inside:

```
data/
```

Expected inputs:

- **Origins** — population-weighted centroids or LSOA centroids  
- **Destinations** — greenspace polygons or centroids  
- **Network** — walking network (optional for v1.0)  
- **Quality attributes** — any greenspace quality metrics you want to include  

**Note:**  
No raw data is included in the repository. Users must supply their own.

---

## **3. Adjust model parameters**

Open:

```
scripts/00_setup/parameters.py
```

You can modify:

- `BETA` — distance decay parameter  
- `QUALITY_WEIGHT` — weight applied to greenspace quality  
- `MAX_DISTANCE` — maximum walking distance (metres)  

These are the only parameters most users will need to change.

---

## **4. Run the baseline model**

From the repository root:

```
python scripts/02_scenarios/run_baseline.py
```

This will:

- load and prepare data  
- apply the gravity model  
- apply the quality attractor  
- build the OD matrix  
- export baseline outputs  

---

## **5. Run the Oxford North scenario**

```
python scripts/02_scenarios/run_oxford_north.py
```

This will:

- apply the development changes  
- rerun the model  
- export scenario outputs  

---

## **6. Generate the triptych**

The triptych shows:

- baseline  
- scenario  
- difference  

Run:

```
python scripts/03_outputs/plot_triptych.py
```

Outputs will appear in:

```
figures/
```

---

## **7. Export tables and summaries**

```
python scripts/03_outputs/export_results.py
python scripts/03_outputs/summarise_outputs.py
```

These produce:

- OD matrices  
- summary tables  
- difference statistics  

---

## **8. Output locations**

- `figures/` → maps, triptychs  
- `data/processed/` → OD matrices, cleaned layers  
- `paper/` → manuscript and technical chapter  
- `scripts/` → the full ViSAGE engine  

---

## **9. Extending ViSAGE**

To add a new scenario, create a new script inside:

```
scripts/02_scenarios/
```

Then call it via:

```python
from scenario_runner import run_scenario
```

This enables Natural England (or any user) to extend the model without modifying the core engine.

---

