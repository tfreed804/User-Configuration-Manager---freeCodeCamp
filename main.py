test_settings = {
    'theme': 'dark',
    'notifications': 'enabled',
    'volume': 'high'
}

def add_setting(settings, key_val_tup):
    key, value = key_val_tup
    lower_key = key.lower()
    lower_value = value.lower()

    if lower_key in settings:
        return f"Setting '{lower_key}' already exists! Cannot add a new setting with this name."
    else:
        settings[lower_key] = lower_value
        return f"Setting '{lower_key}' added with value '{lower_value}' successfully!"

def update_setting(settings, key_val_tup):
    key, value = key_val_tup
    lower_key = key.lower()
    lower_value = value.lower()

    if lower_key in settings:
        settings[lower_key] = lower_value
        return f"Setting '{lower_key}' updated to '{lower_value}' successfully!"
    else:
        return f"Setting '{lower_key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, key):
    lower_key = key.lower()

    if lower_key in settings:
        del settings[lower_key]
        return f"Setting '{lower_key}' deleted successfully!"
    else:
        return 'Setting not found!'

def view_settings(settings):
    if not settings:
        return "No settings available."
    
    lines = ["Current User Settings:"]
    
    for key, value in settings.items():
        lines.append(f"{key.capitalize()}: {value}")
    
    return "\n".join(lines) + "\n"
