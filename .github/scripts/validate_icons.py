"""
.github/scripts/validate_icons.py

This script validates the icons in the /icons folder and checks
if they have right dimensions and are in the right format.
"""

import os
from PIL import Image


def validate_image(path):
    try:
        with Image.open(path) as img:
            if img.size != (32, 32):
                return False, f"Invalid size: expected (32, 32) but got {img.size}"
            if img.format != "PNG":
                return False, f"Invalid format: expected PNG but got {img.format}"
            if os.path.splitext(path)[1] != ".png":
                return False, f"Incorrect file extension: expected .png but got {os.path.splitext(path)[1]}"
            
            return True, "Icon is valid"
    except Exception as e:
        return False, f"Error: {e}"


if __name__ == "__main__":
    all_checks_passed = True
    
    for icon in os.listdir("icons"):
        success, message = validate_image(f"icons/{icon}")
        if not success:
            print("❌", f"[{icon}]", message)
            all_checks_passed = False
            
    if all_checks_passed:
        print("All checks passed successfully!")
        exit(0) # Exit with success
    else:
        print("Some checks failed. See errors for details.")
        exit(1) # Exit with failure
