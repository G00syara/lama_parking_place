try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    "description": "Parking Lot Space Detector",
    "author": "Lama Team",
    "url": "https://github.com/G00syara/lama_parking_place",
    "version": "0.1",
    "install_requires": ["cv2", "numpy", "yml"],
    "packages": ["lama_parking_lot"],
    "scripts": [],
    "name": "LamaParkingPlace"
}

setup(**config)
