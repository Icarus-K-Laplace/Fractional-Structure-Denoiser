import numpy as np
import cv2
from typing import Optional

class FractionalSpectralResponse:
    """
    Implements fractional differentiation in the frequency domain to preserve 
    high-frequency textures better than integer-order derivatives.
    
    Theory: D^alpha f(x) <-> (iw)^alpha F(w)
    """
    
    def __init__(self, default_alpha: float = 1.3):
        self.default_alpha = default_alpha
        self._cache = {}

    def apply(self, img: np.ndarray, alpha: Optional[float] = None) -> np.ndarray:
        """
        Apply fractional filter via FFT.
        
        Args:
            img: Input 2D image (float32).
            alpha: Fractional order (usually 1.0 < alpha < 2.0).
        """
        if alpha is None:
            alpha = self.default_alpha
            
        h, w = img.shape
        key = (h, w, alpha)
        
        # Caching the filter kernel for performance
        if key not in self._cache:
            fx = np.fft.fftfreq(h).reshape(-1, 1)
            fy = np.fft.fftfreq(w).reshape(1, -1)
            # Spectral magnitude response
            mag = np.sqrt(fx**2 + fy**2)
            # Fractional power law
            self._cache[key] = np.power(np.maximum(mag, 1e-8), alpha)
            
        filter_kernel = self._cache[key]
        
        # Frequency domain operation
        fft_img = np.fft.fft2(img.astype(np.float32))
        response = np.fft.ifft2(fft_img * filter_kernel).real
        
        # Normalize response for feature usage
        response = np.nan_to_num(response)
        return (response - response.min()) / (response.max() - response.min() + 1e-8)
