def class_to_json(obj):
    """Converts an object instance to a dictionary representation for JSON serialization."""
    json_dict = {}

    # Iterate over the object's attributes
    for attr in dir(obj):
        # Exclude private and special attributes
        if not attr.startswith("__"):
            value = getattr(obj, attr)

            # Check if the attribute value is of a serializable type
            if isinstance(value, (list, dict, str, int, bool)):
                json_dict[attr] = value

    return json_dict
