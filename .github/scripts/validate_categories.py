"""
.github/scripts/validate_categories.py

This script validates the categories in the
categories.json file and in the /ingredients folder.
"""

import os
import json


def validate_category(category):
    try:
        if not os.path.exists(f"ingredients/{category}"):
            return False, "Category folder does not exist"
        
        return True, "Category is valid"
    except Exception as e:
        return False, f"Error: {e}"


if __name__ == "__main__":
    all_checks_passed = True
    
    try:
        categories = json.load(open("ingredients/categories.json"))
    except Exception as e:
        print("❌", f"Error loading categories.json: {e}")
        exit(1)
    
    for category in categories:
        success, message = validate_category(category)
        if not success:
            print("❌", f"[{category}]", message)
            all_checks_passed = False
    
    for folder in os.listdir("ingredients"):
        if folder not in categories and folder != "categories.json":
            print("❌", f"[{folder}]", "Category is not listed in categories.json")
            all_checks_passed = False
            
    if all_checks_passed:
        print("All checks passed successfully!")
        exit(0) # Exit with success
    else:
        print("Some checks failed. See errors for details.")
        exit(1) # Exit with failure
