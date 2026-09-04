
'''Task is the second GIT workflows revision addressing the feedback from the
    first GIT workflow revision.
    The code has been refactored to use a dictionary for storing advice
    based on season and plant type,
    and includes input validation to handle invalid inputs gracefully.'''


# Store advice in a dictionary for multiple plants and seasons.
advice_dict = {
    ("summer", "flower"): (
        "Water your plants regularly and provide some shade. "
        "Use fertiliser to encourage blooms."
    ),
    ("summer", "vegetable"): (
        "Water your plants regularly and provide some shade. "
        "Keep an eye out for pests!"
    ),
    ("winter", "flower"): (
        "Protect your plants from frost with covers. "
        "Use fertiliser to encourage blooms."
    ),
    ("winter", "vegetable"): (
        "Protect your plants from frost with covers. "
        "Keep an eye out for pests!"
    )
}


# Function to get advice based on season and plant type.
def get_advice(season, plant_type):
    """Return advice for a season and plant type."""
    if not isinstance(season, str) or not isinstance(plant_type, str):
        return (
            "No advice available for this season and plant type combination."
        )

    key = (season.strip().lower(), plant_type.strip().lower())
    return advice_dict.get(
        key, "No advice available for this season and plant type combination."
    )


# Main function to collect user input and display advice.
def main():
    """Collect the user's choices and display the matching advice."""
    season = input("Enter the season (summer/winter): ")
    plant_type = input("Enter the plant type (flower/vegetable): ")
    print(get_advice(season, plant_type))


# Run the main function if this script is executed directly.
if __name__ == "__main__":
    main()
