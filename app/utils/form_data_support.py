from collections import OrderedDict

def weight_input_transform(form_data):
    """
    Add description here.
    """
    
    ordered_data = OrderedDict()

    # As long as the data can be converted to type float, add to ordered_data
    try:
        for key, value in form_data.items():
            if key != 'week_10':
                # Allow empty input
                if value == "":
                    ordered_data[key] = 0.0
                else:
                    ordered_data[key] = float(value)
        # Add "week_10" at the end of ordered_data (to ensure that week_10 comes at the end and not between week_1 and week_2)
        if 'week_10' in form_data:
            # Allow empty input
                if value == "":
                    ordered_data['week_10'] = 0.0
                else:
                    ordered_data['week_10'] = float(form_data['week_10'])
    except ValueError as e:
        return "Invalid input"
    else:
        return ordered_data
