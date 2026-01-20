from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="fsd-denoiser",
    version="0.1.0",
    author="[Your Name]",
    author_email="[Your Email]",
    description="Physics-Aware Texture Preservation Denoising",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/[YourUsername]/Fractional-Structure-Denoiser",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.21.0",
        "opencv-python-headless>=4.5.0",
        "scipy>=1.7.0",
    ],
    extras_require={
        "test": ["pytest"],
    },
)
