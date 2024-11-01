import unicodedata


def get_unicode_info(unicode_input):
    if len(unicode_input) == 1:
        print(ord(unicode_input))
    # Convert the Unicode escape input (e.g., "\u0061") to the actual character
    unicode_char = unicode_input.encode().decode("unicode_escape")

    # Get the character name (description)
    description = unicodedata.name(unicode_char, "Unknown character")

    # Get the Unicode category (e.g., Ll, Lu)
    category = unicodedata.category(unicode_char)

    # Define sub_category based on the Unicode category
    sub_category = "Lowercase" if category == "Ll" else "Uppercase" if category == "Lu" else "Other"

    # Determine the script and language
    script = unicodedata.name(unicode_char).split()[0]  # Extracting the script from the name

    # Get Unicode properties
    # Note: Unicode version is not directly available via unicodedata
    unicode_version = "15.0"  # Use the latest version for reference
    block = unicodedata.category(unicode_char)  # Simplified block extraction from category

    # Construct the result dictionary
    result = {
        "description": description,
        "family": {"script": script, "category": category, "sub_category": sub_category},
        "properties": {"unicode_version": unicode_version, "block": block},
    }

    return result
