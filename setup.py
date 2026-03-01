from setuptools import setup, find_packages
import os

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='satellite-imagery-analysis',
    version='1.0.0',
    author='Rishav Raj',
    author_email='contact@example.com',
    description='Enterprise-grade satellite imagery analysis with SAM and Segment Anything',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Rishav-raj-github/Advanced-Satellite-Imagery-Analysis-with-SAM-and-Segment-Anything',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Image Recognition',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.9',
    install_requires=[
        'torch>=2.0.0',
        'torchvision>=0.15.0',
        'segment-anything==1.0',
        'rasterio>=1.3.0',
        'geopandas>=0.14.0',
        'opencv-python>=4.8.0',
        'numpy>=1.24.0',
        'scikit-learn>=1.3.0',
        'matplotlib>=3.8.0',
        'tqdm>=4.66.0',
    ],
    extras_require={
        'dev': [
            'pytest>=7.4.0',
            'pytest-cov>=4.1.0',
            'black>=23.12.0',
            'flake8>=6.1.0',
            'mypy>=1.7.0',
        ],
        'aws': ['boto3>=1.34.0', 's3fs>=2023.12.0'],
        'gcp': ['google-cloud-storage>=2.10.0'],
    },
    entry_points={
        'console_scripts': [
            'satellite-analyze=src.cli:main',
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
