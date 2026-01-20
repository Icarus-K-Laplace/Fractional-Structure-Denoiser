# Fractional-Structure-Denoiser
A research-grade denoising framework utilizing Fractional Calculus and Structure Tensors to preserve fine textures in medical and scientific imaging. Features frequency-domain fractional filtering, multi-scale structural analysis, and Python/Numba implementation. GPL-3.0 licensed; ideal for MRI, CT, and microscopy restoration.
# Fractional-Structure-Denoiser: Physics-Aware Texture Preservation

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Research%20Prototype-orange.svg)]()

> **"Denoising without Smoothing."**

**Fractional-Structure-Denoiser (FSD)** is a research-grade image restoration framework designed for **medical imaging (MRI/CT)** and **scientific microscopy**. Unlike traditional filters that blur fine details, FSD utilizes **Fractional Calculus** and **Structure Tensors** to distinguish between noise and delicate textures.

---

## 🧠 Theory: Why Fractional?

Standard derivatives (Gradient $\nabla I$) are integers ($1^{st}, 2^{nd}$ order). They are too aggressive for texture analysis.
**Fractional derivatives** ($D^\alpha I$, where $1 < \alpha < 2$) provide a continuous spectrum of frequency responses, allowing us to:

1.  **Preserve Weak Textures**: Amplify mid-frequency details (tissue, cells) without over-enhancing high-frequency noise.
2.  **Frequency Domain Implementation**:
    $$ \mathcal{F}\{D^\alpha f(x)\} = (i\omega)^\alpha \mathcal{F}\{f(x)\} $$
    We implement this efficiently using FFT.

---

## 👁️ Visual Results

| Noisy Input (Simulated Low-Dose CT) | Standard Median Filter | **FSD (Ours)** |
| :---: | :---: | :---: |
| ![Noisy](image.png) | ![Median](assets/medical_median.png) | ![FSD](assets/medical_restored.png) |
| *High noise destroys tissue details* | *Blurry, "plastic" look* | **Texture preserved, noise removed** |

> *Note: FSD maintains the stochastic nature of the tissue texture, crucial for diagnostic confidence.*

---

## 🚀 Key Features

*   **Fractional Spectral Priors**: Frequency-domain filtering for texture enhancement.
*   **Structure Tensor Analysis**: Local anisotropy detection to guide restoration direction.
*   **Physics-Guided**: Designed for images governed by physical transport phenomena (diffusion, heat).
*   **Modular Design**: Clean separation of mathematical priors (`fsd.priors`) and core logic (`fsd.core`).

---

## 🛠️ Installation

```bash
git clone https://github.com/[YourUsername]/Fractional-Structure-Denoiser.git
cd Fractional-Structure-Denoiser
pip install .
