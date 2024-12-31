import os
import tensorflow as tf

# Check if GPU is available and set the GPU device
if tf.test.is_gpu_available():
    physical_devices = tf.config.experimental.list_physical_devices('GPU')
    tf.config.experimental.set_memory_growth(physical_devices[0], True)
    print("GPU available. Using GPU:", physical_devices[0])
else:
    print("GPU not available. Using CPU.")

# List of notebook files to run
notebooks = [
    
    "Design_for_server_Final_to_selected_10k.ipynb",
    "Design_for_server_Final_to_selected_50k.ipynb",
    "Design_for_server_Final_to_selected_1l.ipynb",
    "Design_for_server_Final_to_selected_1.5l.ipynb",
    "Design_for_server_Final_to_selected_2l.ipynb",
    "Design_for_server_Final_to_selected_2.5l.ipynb",
    "Design_for_server_Final_to_selected_3l.ipynb",
    "Design_for_server_Final_to_selected_3.5l.ipynb",
    "Design_for_server_Final_to_selected_4l.ipynb",
    "Design_for_server_Final_to_selected_4.5l.ipynb",
    "Design_for_server_Final_to_selected_5l.ipynb",
    "Design_for_server_Final_to_selected_5.5l.ipynb",
    "Design_for_server_Final_to_selected_6.0l.ipynb",
    "Design_for_server_Final_to_selected_6.5l.ipynb",
    "Design_for_server_Final_to_selected_7l.ipynb"
]

# Iterate through the list of notebooks and run them
for notebook in notebooks:
    os.system(f"jupyter nbconvert --execute --to notebook --inplace {notebook}")

