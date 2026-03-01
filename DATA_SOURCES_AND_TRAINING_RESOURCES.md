# Data Sources and Training Resources

## Complete Guide to Satellite Imagery Datasets, Pre-trained Models, and Training Materials

---

## 1. FREE & OPEN-SOURCE SATELLITE IMAGERY DATASETS

### Landsat Mission
- **USGS Landsat Data** - https://www.usgs.gov/faqs/what-are-band-designations-landsat-satellites
  - Free global imagery at 30m resolution
  - Landsat 8-9: 11 spectral bands
  - Access: https://earthexplorer.usgs.gov/
  - API: https://landsat.usgs.gov/landsat-data-access
  - 40+ years of historical data
  - Format: GeoTIFF, Cloud Optimized GeoTIFF (COG)

### Sentinel Mission (Copernicus)
- **Sentinel-2 Multispectral** - https://sentinel.esa.int/web/sentinel/missions/sentinel-2
  - Free 10m-60m resolution imagery
  - 13 spectral bands (visible, NIR, SWIR)
  - Access: https://scihub.copernicus.eu/
  - Archive: https://dataspace.copernicus.eu/
  - Global coverage every 5 days
  - 7+ years of data available

- **Sentinel-1 SAR** - https://sentinel.esa.int/web/sentinel/missions/sentinel-1
  - Radar imagery (weather-independent)
  - VV and VH polarization bands
  - 10m-40m resolution
  - Excellent for change detection

### PlanetScope (Commercial with Free Trial)
- **Planet Labs Data** - https://www.planet.com/products/basemaps/
  - 3m daily global imagery
  - 4-band multispectral data
  - Free 30-day trial: https://developers.planet.com/
  - API access available
  - Ideal for time-series analysis

### NOAA & GOES (Weather/Environmental)
- **NOAA Earth Observation Group** - https://www.noaa.gov/noaa-everywhere/all-noaa-offices
  - Free hyperspectral data
  - Real-time satellite feeds
  - 40+ year archive
  - Access: https://www.ncei.noaa.gov/

---

## 2. COMPUTER VISION & SEGMENTATION DATASETS

### COCO Dataset (Object Detection)
- **MS COCO** - https://cocodataset.org/
  - 330K images, 2.5M instances
  - 80 object categories
  - Download: https://github.com/cocodataset/cocodataset.github.io
  - Split: train (118K), val (5K), test (20K)
  - JSON annotation format

### ImageNet (Pre-training)
- **ImageNet Large Scale Visual Recognition** - https://www.image-net.org/
  - 1.2M labeled training images
  - 1000 object categories
  - Download: http://www.image-net.org/download
  - Foundation for transfer learning

### ADE20K (Scene Parsing)
- **ADE20K Dataset** - https://groups.csail.mit.edu/vision/datasets/ADE20K/
  - 20K scene images with dense annotations
  - 3,169 object/stuff categories
  - Semantic segmentation labels
  - Download: https://github.com/CSAILVision/ADE20K-dataset

### ISPRS Vaihingen & Potsdam (Aerial)
- **ISPRS Datasets** - http://www2.isprs.org/commissions/comm3/wg4/datasets.html
  - High-resolution aerial imagery
  - 0.05m-0.1m pixel size
  - Segmentation labels
  - Download: http://www2.isprs.org/commissions/comm3/wg4/2d-sem-label-contest.html

---

## 3. GEOSPATIAL & REMOTE SENSING SPECIFIC DATASETS

### UC Merced Land Use Classification
- **UCMERCED_LULC Dataset** - http://weegee.vision.ucmerced.edu/datasets/landuse.html
  - 2.5 GB, 2100 images (256x256 pixels)
  - 0.3048m ground sample distance
  - 17 land use classes
  - Perfect for classification training

### BigEarthNet (Sentinel-based)
- **BigEarthNet** - https://www.bigearth.net/
  - 590K Sentinel-1/2 image pairs
  - 19 classification labels
  - Covariate shift assessment
  - Download: https://www.bigearth.net/downloads/BE_Sentinel1_B04_10m_2020_uint8.zip

### SEN12MS (Sentinel-1/2)
- **SEN12MS Dataset** - https://github.com/zhu-xiao/SEN12MS
  - 180K matching Sentinel-1 and Sentinel-2 image pairs
  - Cloud and shadow masks
  - 10GB compressed dataset
  - Ideal for multi-modal learning

### EuroSAT (Land Cover)
- **EuroSAT Dataset** - https://github.com/phelber/EuroSAT
  - 27K Sentinel-2 images
  - 10 land cover classes
  - 10m resolution
  - Download: https://madm.web.unc.edu/sentinel2/

---

## 4. PRE-TRAINED MODELS & CHECKPOINTS

### Meta's Segment Anything (SAM)
- **Official SAM** - https://github.com/facebookresearch/segment-anything
  - Checkpoints: https://github.com/facebookresearch/segment-anything#model-checkpoints
  - ViT-B (375M params): https://dl.fbaipublicfiles.com/segment_anything/sam_vit_b_01ec64.pth
  - ViT-L (308M params): https://dl.fbaipublicfiles.com/segment_anything/sam_vit_l_0b3195.pth
  - ViT-H (632M params): https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth
  - License: Apache 2.0
  - Paper: https://arxiv.org/abs/2304.02643

### YOLOv8 (Object Detection)
- **Ultralytics YOLOv8** - https://github.com/ultralytics/ultralytics
  - Pre-trained models: https://docs.ultralytics.com/models/yolov8/#supported-tasks-and-modes
  - Models on/off/huggingface
  - YOLOv8n, s, m, l, x sizes available
  - License: AGPL-3.0

### Vision Transformer (ViT)
- **Google Vision Transformer** - https://github.com/google-research/vision_transformer
  - Pre-trained on ImageNet-21k
  - Models: ViT-B/16, ViT-L/16, ViT-H/14
  - Weights: https://storage.googleapis.com/vit_models/
  - Paper: https://arxiv.org/abs/2010.11929

### DINO (Self-Supervised Vision)
- **DINO Transformers** - https://github.com/facebookresearch/dino
  - Tokenless image transformers
  - Excellent feature representations
  - Weights: https://github.com/facebookresearch/dino#pre-trained-models
  - License: Apache 2.0
  - Paper: https://arxiv.org/abs/2104.14294

---

## 5. TRAINING & ANNOTATION TOOLS

### Annotation Platforms
- **LabelImg** - https://github.com/heartexlabs/labelImg (Free)
- **CVAT** - https://github.com/opencv/cvat (Free, self-hosted)
- **Labelbox** - https://labelbox.com/ (Freemium)
- **Roboflow** - https://roboflow.com/ (Freemium, auto-augmentation)
- **Segment Anything Labeling Tool** - https://github.com/facebookresearch/segment-anything#onnx-model-export

### Data Augmentation Libraries
- **Albumentations** - https://github.com/albumentations-team/albumentations
- **Torchvision Transforms** - https://pytorch.org/vision/stable/transforms.html
- **Imgaug** - https://github.com/aleju/imgaug
- **GDAL/Rasterio** - For geospatial augmentation

---

## 6. MACHINE LEARNING FRAMEWORKS & LIBRARIES

### Deep Learning Frameworks
- **PyTorch** - https://pytorch.org/ (Recommended)
  - `pip install torch torchvision torchaudio`
  - CUDA support
  - TorchScript for deployment

- **TensorFlow/Keras** - https://www.tensorflow.org/
  - `pip install tensorflow`
  - TFLite for mobile/edge
  - TF Serving for production

### Computer Vision Libraries
- **OpenCV** - https://opencv.org/ (`pip install opencv-python`)
- **scikit-image** - https://scikit-image.org/ (`pip install scikit-image`)
- **PIL/Pillow** - https://pillow.readthedocs.io/ (`pip install Pillow`)

### Geospatial Libraries
- **GDAL** - https://gdal.org/ (Raster/vector processing)
- **Rasterio** - https://rasterio.readthedocs.io/ (`pip install rasterio`)
- **GeoPandas** - https://geopandas.org/ (`pip install geopandas`)
- **Shapely** - https://shapely.readthedocs.io/ (Geometry operations)
- **Fiona** - https://fiona.readthedocs.io/ (Vector I/O)
- **Pyproj** - https://pyproj4.github.io/pyproj/ (Projection/datum transformations)

---

## 7. BENCHMARK DATASETS FOR EVALUATION

### Satellite Change Detection
- **LEVIR-CD** - https://github.com/S2Looking/Dataset
- **DSIFN-Dataset** - https://github.com/GaoXvlong/DSIFN-Dataset
- **WHU-CD** - https://github.com/daifeng2016/Change-Detection-Dataset

### Building Extraction
- **SpaceNet** - https://www.spacenet.ai/datasets/
- **Inria Aerial Image Labeling** - https://project.inria.fr/aerialimagelabeling/
- **Massachusetts Buildings Dataset** - https://www.cs.toronto.edu/~vmnih/

---

## 8. ONLINE LEARNING RESOURCES

### Courses
- **Deep Learning (Fast.ai)** - https://course.fast.ai/
- **Computer Vision (Stanford CS231n)** - https://cs231n.github.io/
- **Remote Sensing (ESA)** - https://www.esa.int/Education
- **Geospatial Analysis (Coursera)** - https://www.coursera.org/learn/gis-data-formats-design-creation

### Papers & Research
- **arXiv** - https://arxiv.org/ (Computer Vision & Remote Sensing)
- **IEEE Xplore** - https://ieeexplore.ieee.org/
- **Google Scholar** - https://scholar.google.com/
- **Papers with Code** - https://paperswithcode.com/ (Code + Papers)

---

## 9. API & CLOUD PLATFORMS

### Data Access APIs
- **USGS EROS** - https://ers.cr.usgs.gov/swagger/
- **Sentinel Hub** - https://www.sentinel-hub.com/ (API + APIs)
- **Planet API** - https://developers.planet.com/apis/orders/
- **Google Earth Engine** - https://earthengine.google.com/ (JS API + Python)

### Cloud ML Platforms
- **Google Cloud Vertex AI** - https://cloud.google.com/vertex-ai/
- **AWS SageMaker** - https://aws.amazon.com/sagemaker/
- **Azure ML** - https://azure.microsoft.com/en-us/services/machine-learning/
- **Kaggle Notebooks** - https://www.kaggle.com/notebooks (Free GPU/TPU)

---

## 10. QUICK START DOWNLOAD COMMANDS

```bash
# Landsat via AWS S3
aws s3 ls s3://usgs-landsat/

# Sentinel via Copernicus
curl -O https://dataspace.copernicus.eu/

# SAM Checkpoints
wget https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth

# YOLOv8
pip install ultralytics
from ultralytics import YOLO

# EuroSAT Dataset
wget https://madm.web.unc.edu/sentinel2/Eurosat.zip

# BigEarthNet
wget http://www.bigearth.net/downloads/BigEarthNet.tar
```

---

**Last Updated:** March 1, 2026
**Maintained By:** Rishav Raj | Advanced AI Research Division
