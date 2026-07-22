
## Features

- Hand detection in images and videos
- Trained on over 13,000 diverse images
- Optimized accuracy with YOLOv8
- Easy to use and deploy
- Ready for real-time applications

## Dataset

### Oxford Hand Dataset

The Oxford Hand Dataset is a benchmark dataset in the field of hand detection. It includes:

- 13,050 annotated images
- Diverse web-sourced scenes
- Hands in various poses, sizes, and backgrounds
- Precise bounding box annotations

> "A hand detection dataset is proposed. A total of 13,050 hand instances are annotated from images collected from the web."
> -- Oxford Visual Geometry Group

## Credits

### Original Dataset

**Oxford Hand Dataset**
*Visual Geometry Group (VGG), University of Oxford*

- Official Site: http://www.robots.ox.ac.uk/~vgg/data/hands/
- Academic Publication: "Hand detection using multiple proposals" (BMVC 2011)

### YOLO Conversion Script

**PINTO0309**
*Developer of the conversion script to YOLO format*

- GitHub Repository: https://github.com/PINTO0309/oxford-hands-to-yolo
- Automatic conversion from .mat annotations to .txt (YOLO format)
- Folder structure ready for training

### Training Framework

**Ultralytics YOLOv8**
*Training and deployment framework*

- Official Site: https://ultralytics.com/
- Documentation: https://docs.ultralytics.com/

## Trained Models

The trained model weights are available on Google Drive:

| Model | Description | Link |
|-------|-------------|------|
| best.pt | Best model during training | https://drive.google.com/file/d/1dkwCudqm0G9Bx_959DvrC9h-nV5V3bfZ/view?usp=sharing |
| last.pt | Final model at the end of training | https://drive.google.com/file/d/1QauwCvWTGRmbVZCRXkcEQVbsnvrQs2Ha/view?usp=sharing |
