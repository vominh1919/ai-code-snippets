#!/usr/bin/env python3
"""AI Code Snippet 48"""

import numpy as np
from typing import List, Dict, Any

def process_data(data: List[float]) -> Dict[str, Any]:
    """Process numerical data."""
    return {
        "mean": np.mean(data),
        "std": np.std(data),
        "min": np.min(data),
        "max": np.max(data),
        "count": len(data)
    }

def normalize_data(data: List[float]) -> List[float]:
    """Normalize data to 0-1 range."""
    min_val = min(data)
    max_val = max(data)
    if max_val == min_val:
        return [0.5] * len(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

# Example usage
if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = process_data(data)
    print(f"Statistics: {result}")
    
    normalized = normalize_data(data)
    print(f"Normalized: {normalized}")
