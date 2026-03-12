# 🌿 ViSAGE 1.0 |

*A transparent, gravity‑based modelling framework for analysing greenspace visitation and development impacts.*

ViSAGE (Visitation Simulation and Greenspace Evaluation) is a reproducible spatial modelling framework designed to help planners, researchers and environmental agencies understand how people interact with greenspace networks — and how new developments reshape demand.

This repository contains the core ViSAGE 1.0 model used for the Oxford North case study and for the associated Landscape & Urban Planning manuscript.

---

## 🔍 What ViSAGE does |

- Models greenspace visitation using a gravity‑based approach  
- Integrates a **quality‑based attractiveness** extension
- Generates **origin–destination flows** between population centres and greenspaces  
- Supports **scenario testing**, including new developments and network changes  
- Produces clear, reproducible outputs including the signature **baseline–scenario–difference triptych**

---

## 📁 Repository structure |

visage-1.0/
│
├── data/                # Placeholder for input data (not included)
│
├── scripts/             # Core modelling code
│   ├── 00_setup/        # Data loading, cleaning, parameters
│   │   ├── load_data.py
│   │   ├── prepare_layers.py
│   │   └── parameters.py
│   │
│   ├── 01_model/        # Gravity model + quality attractor + OD builder
│   │   ├── gravity_model.py
│   │   ├── quality_attractor.py
│   │   ├── od_matrix_builder.py
│   │   └── utils.py
│   │
│   ├── 02_scenarios/    # Baseline + Oxford North + scenario runner
│   │   ├── run_baseline.py
│   │   ├── run_oxford_north.py
│   │   └── scenario_runner.py
│   │
│   └── 03_outputs/      # Triptych plotting + exports + summaries
│       ├── plot_triptych.py
│       ├── export_results.py
│       └── summarise_outputs.py
│
├── notebooks/           # Exploratory analysis (optional)
│
├── figures/             # Baseline, scenario and difference maps
│
└── paper/               # Manuscript and technical chapter scaffolding

---

## ⚙️ How the model works (conceptually) |

1. **Load and prepare data**  
   Origins, destinations and networks are aligned, cleaned and normalised.

2. **Apply gravity model**  
   Distance decay and attractiveness weights generate visitation probabilities.

3. **Integrate quality attractor**  
   Greenspace quality modifies destination attractiveness (ViSAGE 1.0 feature).

4. **Build OD matrix**  
   Flows are computed between each origin–destination pair.

5. **Run scenarios**  
   Baseline and development scenarios (e.g., Oxford North) are executed.

6. **Generate outputs**  
   Maps, triptychs and summary tables are exported for analysis.

---

## 🚀 Running ViSAGE 1.0 |

A full “How to run ViSAGE 1.0” guide is provided in  
`paper/how_to_run_visage.md` (or will be added shortly).

In brief:

1. Place your input data in `data/`  
2. Adjust parameters in `scripts/00_setup/parameters.py`  
3. Run a scenario script, e.g.:

```bash
python scripts/02_scenarios/run_baseline.py
python scripts/02_scenarios/run_oxford_north.py

```

---

## 📊 Outputs will appear in:

- figures/
- data/processed/

---

## 📦 Versioning |

This repository corresponds to ViSAGE v1.0.0, the version used for:

- Natural England’s greenspace accessibility work
- A submission to the Landscape & Urban Planning journal

* Future versions (1.1, 2.0) will extend the framework with:
- multi‑modal networks,
- behavioural heterogeneity,
- dynamic accessibility metrics.

---

## 📄 License |

This project is released under the MIT License, enabling reuse and adaptation with attribution.

---

## 🤝 Acknowledgements |

ViSAGE 1.0 was developed by T.E O’Shea, H.T.P Williams, T. Collins, N. Nugroho with support and guidance from T. Chugh, F. Botta, P. Challinor, A. Heppenstall, Y. Gamalaldin, T. Mitomi as part of ongoing research into environmental intelligence, socio‑spatial modelling and greenspace accessibility.
The Oxford North scenario was produced through collaboration between the universities of Exeter and Glasgow, with guidamce and support from Natural England.

---




