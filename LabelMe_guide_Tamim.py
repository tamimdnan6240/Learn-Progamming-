## Use LabelMe via PyQt5 in a Clean Virtual Environment 
conda create -n labelme_env python=3.9 -y
conda activate labelme_env

pip install pyqt5==5.15.9
pip install labelme==5.2.1
labelme


## Code for label, Task: Inclusion-Exclusion
import glob
from PIL import Image
import matplotlib.pyplot as plt
import os

# 🔁 Your folders
image_folder = "cnn_images"
json_folder = "Inclusion-exclusion-labels"

# ✅ Load all image types
image_paths = []
for ext in ['*.jpg', '*.jpeg', '*.png', '*.JPG', '*.PNG']:
    image_paths.extend(glob.glob(os.path.join(image_folder, ext)))
image_paths = sorted(image_paths)

for img_path in image_paths:
    img_name = os.path.basename(img_path)
    img_stem = os.path.splitext(img_name)[0]  # Name without extension
    json_path = os.path.join(json_folder, img_stem + ".json")

    # 🔍 Show image
    img = Image.open(img_path)
    plt.imshow(img)
    plt.axis('off')
    plt.title(f"Annotate in LabelMe: {img_name}")
    plt.show()

    print(f"📝 Use LabelMe to annotate:\n- Image: {img_path}")
    print(f"💾 Save annotation as: {json_path}")

    # Wait until .json file is saved
    while not os.path.exists(json_path):
        input("🔁 Press ENTER when you've saved the .json annotation...")

    print(f"✅ Found annotation: {json_path}\n{'-'*60}")
