# Installation Guide

## Prerequisites

- Python 3.9 or higher
- CUDA 11.8+ (for GPU support, recommended)
- Git
- 8GB+ RAM (16GB+ recommended for model inference)
- 50GB+ disk space for models and datasets

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/Rishav-raj-github/Advanced-Satellite-Imagery-Analysis-with-SAM-and-Segment-Anything.git
cd Advanced-Satellite-Imagery-Analysis-with-SAM-and-Segment-Anything
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

### 4. Install SAM Models

```bash
python -c "from segment_anything import sam_model_registry; sam_model_registry('vit_h')"
```

## Development Installation

For development with additional testing tools:

```bash
pip install -e .[dev]
```

## Installation with Cloud Support

### AWS S3 Support

```bash
pip install -e .[aws]
```

### Google Cloud Support

```bash
pip install -e .[gcp]
```

## Configuration

1. Create a `.env` file in the project root:

```bash
cp .env.example .env
```

2. Update configuration values for your environment.

## Verification

Verify installation:

```bash
python -c "import segment_anything; import torch; print(f'SAM installed. Torch version: {torch.__version__}')"
```

## Troubleshooting

### CUDA Issues

If you encounter CUDA compatibility issues:

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### Geospatial Library Issues

For Rasterio/GDAL issues on macOS:

```bash
conda install -c conda-forge gdal rasterio
```
