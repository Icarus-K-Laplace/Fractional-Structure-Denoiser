import cv2
import numpy as np
from concurrent.futures import ThreadPoolExecutor
from .priors import FractionalSpectralResponse

class StructureEncoder:
    """
    Extracts multi-scale structural features including:
    1. Local Gradient Energy
    2. Fractional Spectral Response
    3. Local Conductivity (Diffusion Coefficient)
    """
    
    def __init__(self):
        self.frac_op = FractionalSpectralResponse()

    def extract(self, img: np.ndarray) -> dict:
        img_f = img.astype(np.float32)
        
        # Parallel extraction for speed
        with ThreadPoolExecutor(max_workers=2) as executor:
            future_frac = executor.submit(self.frac_op.apply, img_f)
            future_local = executor.submit(self._compute_local, img_f)
            
            frac_resp = future_frac.result()
            local_feats = future_local.result()
            
        return {**local_feats, "fractional": frac_resp}

    @staticmethod
    def _compute_local(img: np.ndarray) -> dict:
        # Structure Tensor eigenvalues approximation
        gx = cv2.Sobel(img, cv2.CV_32F, 1, 0)
        gy = cv2.Sobel(img, cv2.CV_32F, 0, 1)
        gradient = np.sqrt(gx**2 + gy**2)
        
        # Local Variance (Texture energy)
        mean = cv2.GaussianBlur(img, (5,5), 1.0)
        sq_mean = cv2.GaussianBlur(img**2, (5,5), 1.0)
        variance = np.maximum(sq_mean - mean**2, 0)
        
        # Perona-Malik Conductivity
        k = np.percentile(gradient, 90)
        conductivity = np.exp(-(gradient / (k + 1e-6))**2)
        
        return {
            "gradient": gradient, 
            "variance": variance,
            "conductivity": conductivity
        }
