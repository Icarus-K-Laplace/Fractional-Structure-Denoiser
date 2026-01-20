import sys
import os
import cv2
import numpy as np

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fsd.core import FractionalStructureDenoiser
from fsd.utils import load_image, save_image, add_gaussian_noise

def main():
    print("="*60)
    print("FSD: Medical Image Restoration Demo")
    print("="*60)
    
    # 1. Setup Data
    # Use a dummy image if file not found (for easy testing)
    img_path = "data/brain_mri.png" 
    if not os.path.exists(img_path):
        print(f"Warning: {img_path} not found. Creating synthetic pattern.")
        img = np.zeros((512, 512), dtype=np.float32)
        cv2.circle(img, (256, 256), 100, 150, -1) # Tumor-like
        # Add texture
        noise_texture = np.random.normal(0, 10, (512, 512))
        img += noise_texture
        img = np.clip(img, 0, 255)
    else:
        img = load_image(img_path)

    # 2. Add Noise (Simulate Low-Dose CT)
    print("Simulating noise...")
    noisy = add_gaussian_noise(img, sigma=30.0)
    
    # Create a dummy mask (process whole image for this demo)
    mask = np.ones_like(noisy, dtype=np.uint8)

    # 3. Process
    print("Running Fractional Structure Denoiser...")
    denoiser = FractionalStructureDenoiser(iterations=3, relaxation=0.8)
    
    # Note: In a real scenario, this would call the optimized core.
    # Here we simulate the output to verify pipeline connectivity.
    # The actual 'process' logic in core.py needs to be fully implemented 
    # with the polynomial fit logic from your previous MAPD work.
    # For this demo, we assume core.py is fully functional.
    result = denoiser.process(noisy, mask)
    
    # 4. Save Results
    os.makedirs("results", exist_ok=True)
    save_image("results/medical_noisy.png", noisy)
    save_image("results/medical_restored.png", result)
    
    print("✅ Done! Results saved to 'results/' folder.")

if __name__ == "__main__":
    main()
