# Repository: ANN Data and Design for Servers

## Description
This repository contains a collection of Jupyter notebooks, datasets, and scripts designed to facilitate the analysis, simulation, and modeling of artificial neural networks (ANNs) and server configurations. The files encompass work on ergotropy calculations, data preprocessing, and server design tailored for various data scales.

## Contents

### Notebooks

1. **ANN Data Requirements**
   - `ANN_DATA_REQUIREMENT.ipynb`: Outlines the data requirements for training and evaluating ANNs in specific applications.

2. **Server Design Series**
   - `Design_for_server_1-10k_new.ipynb`
   - `Design_for_server_1.ipynb`
   - `Design_for_server_Final_to_selected_XL.ipynb` (X ranges from 1.5L to 7L, including 10k, 50k, and other scales): Contains designs for server configurations optimized for different dataset sizes.

3. **Ergotropy Analysis**
   - `ergotropy_my_eit-6-atoms-T0_high_set1-main-ARC_try-Final_Pre_thesis.ipynb`
   - `ergotropy_my_eit-common_GS_6_3_3.5-All systems.ipynb`
   - Variations for Rb-87 trials and specific ergotropy curve analyses: Focused on calculating ergotropy in multi-atomic systems and understanding dynamics under various conditions.

4. **Model Prediction**
   - `model_3_lakh_trial_to_predict_REQUIRED_plots_MJS.ipynb`: Training and evaluating models on large datasets.
   - `using_the_model_3_lakh_19_february_2024.ipynb`: Application of the trained models for predictive tasks.

5. **Generic Server Design**
   - `Designing_generic_file_for_server.ipynb`: Blueprint for a general-purpose server design model.

6. **Utility Scripts**
   - `run_notebooks.py`: A script to automate the execution of multiple notebooks.

### Datasets

- `Test_data_1000.csv`: A sample dataset for initial testing and model evaluation.
- `updated_Data_till_T0_2-75_durga_oct17.7z`: Compressed data for extended analyses and simulations.

## Key Features
- Tools for designing servers tailored to datasets of varying scales.
- Detailed analysis and visualization of ergotropy in multi-atomic systems.
- Large-scale ANN training and predictions.
- Scripts for automating repetitive tasks, enhancing efficiency.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/ManashSarmah/ANN_Data_and_Design.git
   cd ANN_Data_and_Design
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Extract compressed datasets (if applicable):
   ```bash
   tar -xvzf updated_Data_till_T0_2-75_durga_oct17.7z
   ```

## Usage

- Explore the notebooks for specific use cases (e.g., server design, ANN training).
- Modify the input data paths in notebooks as required.
- Use `run_notebooks.py` to batch-process multiple notebooks.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request to suggest improvements or add new features.



## Contact
For queries or collaborations, please reach out via the Issues tab or contact the repository owner.

