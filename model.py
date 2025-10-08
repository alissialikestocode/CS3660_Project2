"""
model.py 
"""
import json

def get_professionals():
    """
    Returns Professionals data
    """
    with open ("data/professionals.dat", "r", encoding="UTF-8") as f:
        return json.load(f)

def get_services():
    """
    Returns Services data
    """
    with open ("data/services.dat", "r", encoding="UTF-8") as f:
        return json.load(f)
