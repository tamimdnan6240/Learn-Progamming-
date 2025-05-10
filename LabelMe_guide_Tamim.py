## Code for label, Task: Inclusion-Exclusion
import glob
from PIL import Image
import matplotlib.pyplot as plt
import os
import shutil

# 🔁 Input folders
image_folder = "cnn_images"
json_folder = "Inclusion-exclusion-labels"
output_folder = "cnn_dataset_ready"

# ✅ Label shortcuts
class_key_map = {
    'v': 'vehicle',
    'p': 'pedestrian',
    't': 'train',
    'e': 'empty'
}

# ✅ Create output folders
for cls in class_key_map.values():
    os.makedirs(os.path.join(output_folder, cls), exist_ok=True)

# ✅ Load all image formats
image_paths = []
for ext in ['*.jpg', '*.jpeg', '*.png', '*.JPG', '*.PNG']:
    image_paths.extend(glob.glob(os.path.join(image_folder, ext)))
image_paths = sorted(image_paths)

# 🔁 Loop through each image
for img_path in image_paths:
    img_name = os.path.basename(img_path)
    img_stem = os.path.splitext(img_name)[0]
    json_path = os.path.join(json_folder, img_stem + ".json")

    # 🔍 Show image
    img = Image.open(img_path)
    plt.imshow(img)
    plt.axis('off')
    plt.title(f"Now annotate and then label:\n{img_name}")
    plt.show()

    print(f"📝 Use LabelMe GUI to annotate.")
    print(f"💾 Save .json as: {json_path}")

    # ⏳ Wait for JSON annotation to be saved
    while not os.path.exists(json_path):
        input("🔁 Press ENTER after saving .json file...")

    # ⌨️ Prompt for label class using key
    label_key = input("▶️ Enter label key [v=vehicle, p=pedestrian, t=train, e=empty]: ").lower().strip()

    if label_key in class_key_map:
        label = class_key_map[label_key]
        dst_path = os.path.join(output_folder, label, img_name)
        shutil.copy(img_path, dst_path)
        print(f"✅ Copied to: {dst_path}\n{'-'*60}")
    else:
        print(f"❌ Invalid key. Skipped {img_name}\n{'-'*60}")
