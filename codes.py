# Importing necessary libraries 
import pandas as pd

data = {
    "Imaging Modality": ["CT", "MRI", "X-Ray", "USG", "PET"],
    "Body Part": ["Head", "Neck", "Chest", "Pelvis", "Abdomen"],
    "View": ["Axial", "Sagittal", "Lateral", "Coronal", "Oblique"],
    "Contrast": ["With Contrast", "Without Contrast"]
}

# Adding the new special modifiers

# Special Modifier (SS)

# PD: Pediatric
# OB: Obstetric
# EM: Emergency
# IN: Interventional
# 3D: 3D Reconstruction
# FU: Follow-up
# SC: Screening
special_modifiers = ["PD", "OB", "EM", "IN", "3D", "FU", "SC"]


combinations_with_modifiers = []

for modality in data["Imaging Modality"]:
    for part in data["Body Part"]:
        for view in data["View"]:
            for contrast in data["Contrast"]:
                for modifier in special_modifiers:
                    code = f"{modality[:1]}-{part[:2]}-{view[:2]}-{('C' if 'With' in contrast else 'NC')}-{modifier}"
                    combinations_with_modifiers.append({
                        "Modality": modality,
                        "Body Part": part,
                        "View": view,
                        "Contrast": contrast,
                        "Special Modifier": modifier,
                        "Internal Code": code
                    })

# DataFrame to export as Excel with special modifiers
df_with_modifiers = pd.DataFrame(combinations_with_modifiers)

# Saving the dataframe with special modifiers to an Excel file
file_path_with_modifiers = 'internal_imaging_codes_with_modifiers.xlsx'
df_with_modifiers.to_excel(file_path_with_modifiers, index=False)
