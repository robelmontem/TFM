from pathlib import Path
import random
import shutil

INPUT_DIR = Path("../../MEDIDAS")
OUTPUT_DIR = Path("../../IMAGENES_PARA_ANOTAR")
IMAGES_PER_SUBJECT = 250
IMAGE_EXTENSIONS = {".jpeg", ".png"}

random.seed(1234)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

for subject_dir in INPUT_DIR.iterdir():
    if not subject_dir.is_dir():
        continue

    images = [
        path for path in subject_dir.rglob("*")
        if path.suffix.lower() in IMAGE_EXTENSIONS
    ]

    selected_images = random.sample(images, min(IMAGES_PER_SUBJECT, len(images)))

    subject_output_dir = OUTPUT_DIR / subject_dir.name
    subject_output_dir.mkdir(parents=True, exist_ok=True)

    for image_path in selected_images:
        safe_name = "__".join(image_path.relative_to(subject_dir).parts)
        shutil.copy2(image_path, subject_output_dir / safe_name)

    print(f"{subject_dir.name}: {len(selected_images)} images copied")