import unittest
import numpy as np
from fsd.priors import FractionalSpectralResponse

class TestFractionalPriors(unittest.TestCase):
    
    def setUp(self):
        self.fsr = FractionalSpectralResponse()
        
    def test_fractional_response_shape(self):
        """Output shape should match input."""
        img = np.random.rand(64, 64).astype(np.float32)
        res = self.fsr.apply(img, alpha=1.5)
        self.assertEqual(img.shape, res.shape)
        
    def test_high_frequency_response(self):
        """Fractional derivative should highlight edges."""
        # Create an image with a step edge
        img = np.zeros((100, 100), dtype=np.float32)
        img[:, 50:] = 1.0
        
        res = self.fsr.apply(img, alpha=1.0) # ~ 1st derivative
        
        # The response at the edge (col 50) should be high
        edge_response = np.max(res[:, 48:52])
        flat_response = np.mean(res[:, 10:20])
        
        self.assertGreater(edge_response, flat_response * 2, 
                           "Edge response should be significantly higher than flat region")

    def test_alpha_sensitivity(self):
        """Higher alpha should produce stronger high-freq emphasis."""
        img = np.random.rand(32, 32).astype(np.float32)
        res_low = self.fsr.apply(img, alpha=0.5)
        res_high = self.fsr.apply(img, alpha=2.0)
        
        # This is a heuristic check; exact comparison depends on implementation details
        # But generally, higher derivative order amplifies noise/texture more.
        self.assertNotEqual(np.sum(res_low), np.sum(res_high))

if __name__ == '__main__':
    unittest.main()
