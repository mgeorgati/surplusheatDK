
# Surplus heat analysis in Danish DH systems  

## Overview  
This analysis aims to assess the utilization of surplus heat in Danish district heating (DH) systems. The methodological approach consists of two main steps: analyzing historical data and identifying current potential for surplus heat integration.  

---

## Methodological Approach  

### 1. Historical Data Processing  
**Notebook:** `linegraph_DHproduction_EH.ipynb`  

- **Objective:** Process historical data on surplus heat utilization in Danish DH systems.  
- **Steps:**  
  a. Extract relevant data from the Excel file `6_ept_produktions-_og_forbrugsdata_2021-2023` (Sheet: `EPT2021-2023`):  
     - Select rows where `aar = 2022` and `Brændselsfrit_TJ >0`  AND `VrkTypeID==ER` 
  b. Aggregate data by `vaerk_kommune`, summing `varmeprod_TJ`.   
  c. Join the dataset with a GeoJSON file of municipalities using `vaerk_kommune` and `kode`.  

- **Additional Processing Notebooks:**  
  - `processing_historicalSurplusHeat.ipynb`  
  - `makeMap_EHshares_hist.ipynb`  
  - `bbox.ipynb`  

- **Manual Adjustments:**  
  - Facility names have been manually classified into five sectoral categories (not done in Python).  
  - The same approach is applied to other historical datasets that are not detailed here.  

---

### 2. Current Potential Analysis  
**Objective:** Identify surplus heat potentials that could be integrated into the existing DH systems.  

- **Processing Scripts & Notebooks:**  
  - `reclassVarmeplanDenmark2021.py` – Data classification  
  - `summarize_VarmeplanDenmarkData.ipynb` – Summarizing available data  
  - `summarizePotential_bySector.ipynb` – Sector-wise potential assessment and assessment based on the current utilisation
  - `makeMap_EHshares_varmeplan.ipynb` – Mapping potential surplus heat shares  

---

## Required Data  
The analysis relies on the following datasets:  

1. **DH Areas** – Spatial boundaries and attributes of district heating networks. Available at https://geodata-info.dk/srv/dan/catalog.search#/metadata/f4d297b7-6d6f-489d-9d74-e852d1d00ef6.    
2. **Municipal Boundaries** – GeoJSON or shapefile containing administrative divisions for spatial analysis. Available at https://dataforsyningen.dk/data/3901 
3. **EPT Data** – Energy production and consumption data (`6_ept_produktions-_og_forbrugsdata_2021-2023.xlsx`). Available at https://ens.dk/analyser-og-statistik/data-oversigt-over-energisektoren.   

Ensure these datasets are available and properly formatted before running the analysis.  

---

## Notes  
- The analysis involves both Python-based processing and manual classification steps.  
- The results provide insights into the extent of surplus heat utilization and opportunities for further integration.  

For any questions, feel free to reach out at marinag@plan.aau.dk  





