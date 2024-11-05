"""
.github/scripts/validate_ingredients.py

This script validates the ingredients in the /ingredients
folder and checks if they have the right structure.
"""

import os
import json


def validate_ingredient(data):
    # Check required top-level keys
    required_keys = ["name", "description", "icon", "checks"]
    for key in required_keys:
        if key not in data:
            return False, f"Missing required key: '{key}'"

    # Check "checks" for "tags" or "headers"
    checks = data["checks"]
    if not isinstance(checks, dict):
        return False, "'checks' should be a dictionary"

    tags = checks.get("tags", [])
    headers = checks.get("headers", [])

    # Ensure that at least one of "tags" or "headers" is non-empty
    if not tags and not headers:
        return False, "At least one check ('tags' or 'headers') should be non-empty"

    # Validate the "tags" structure if present
    if tags:
        if not isinstance(tags, list):
            return False, "'tags' should be a list"
        for tag_entry in tags:
            if not isinstance(tag_entry, dict):
                return False, "Each 'tags' check should be a dictionary"
            if "tag" not in tag_entry or "value" not in tag_entry:
                return False, "Each 'tags' check must contain 'tag' and 'value' keys"
            if "attribute" in tag_entry and not (isinstance(tag_entry["attribute"], str) or tag_entry["attribute"] is None):
                return False, "'attribute' in 'tags' check must be a string or null"

    # Validate the "headers" structure if present
    if headers:
        if not isinstance(headers, list):
            return False, "'headers' should be a list"
        for header_entry in headers:
            if not isinstance(header_entry, dict):
                return False, "Each 'headers' check should be a dictionary"
            if "header" not in header_entry or "value" not in header_entry:
                return False, "Each 'headers' check must contain 'header' and 'value' keys"
            if not (isinstance(header_entry["header"], str) or header_entry["header"] is None):
                return False, "'header' in 'headers' check must be a string"

    # Validate the "icon" path
    if not data["icon"].startswith("/icon/"):
        return False, "Icon should start with '/icon/'"
   
    # Validate if the icon exists
    if not os.path.exists(f"icons/{data['icon'].split('/icon/')[1]}"):
        return False, f"Icon '{data['icon'].split('/icon/')[1]}' does not exist"

    # Validate description
    if not data["description"][-1] == ".":
        return False, "Description should end with a period"

    # All checks passed
    return True, "Ingredient is valid"


if __name__ == "__main__":
    all_checks_passed = True
    categories = json.load(open("ingredients/categories.json"))
    
    for category in categories:
        for ingredient in os.listdir(f"ingredients/{category}"):
            success, message = validate_ingredient(json.load(open(f"ingredients/{category}/{ingredient}")))
            if not success:
                print("❌", f"[{category}/{ingredient}]", message)
                all_checks_passed = False
            
    if all_checks_passed:
        print("All checks passed successfully!")
        exit(0) # Exit with success
    else:
        print("Some checks failed. See errors for details.")
        exit(1) # Exit with failure
