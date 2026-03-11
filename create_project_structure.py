import os

structure = {
    "data": {
        "raw": [],
        "processed": []
    },

    "notebooks": {
        "EDA": [
            "01_data_overview.ipynb",
            "02_survival_target_analysis.ipynb",
            "03_spatial_analysis.ipynb",
        ],

        "preprocessing": [
            "01_data_cleaning.ipynb",
            "02_feature_engineering.ipynb",
            "03_feature_selection.ipynb",
        ],

        "modeling": [
            "01_baseline_survival_model.ipynb",
            "02_cox_model.ipynb",
            "03_random_forest_survival.ipynb",
            "04_lightgbm_survival.ipynb",
        ],

        "inference": [
            "01_generate_submission.ipynb"
        ]
    },

    "models": [],

    "artifacts": [],

    "submissions": [],

    "experiments": {
        "dvclive": []
    },

    "configs": [
        "model_config.yaml"
    ],

    "": ["README.md"]
}


def create_structure(base, struct):

    for name, content in struct.items():

        path = os.path.join(base, name)

        if isinstance(content, dict):

            os.makedirs(path, exist_ok=True)
            create_structure(path, content)

        elif isinstance(content, list):

            os.makedirs(path, exist_ok=True)

            for file in content:

                file_path = os.path.join(path, file)

                if not os.path.exists(file_path):
                    open(file_path, "a").close()


create_structure(".", structure)

print("Project structure created successfully.")