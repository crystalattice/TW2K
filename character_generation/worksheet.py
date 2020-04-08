from dataclasses import dataclass, field
from typing import Dict, List


@dataclass()
class Character:
    """Basic information for character generation"""

    char_name: str
    char_initiative: int
    char_rad_exposure: int
    char_age: int
    char_weight: int
    char_load_capacity: int
    char_throw_range: int
    char_unarmed_damage: int
    char_equipment_allowance: int
    char_to_hit_numbers: List[Dict[Dict[str, int]]] = field(
        default=[
            {
                "Small Arms (Pistol)": {
                    "Close": 0,
                    "Medium": 0,
                    "Long": 0,
                    "Extreme": 0
                },
                "Small Arms (Rifle)": {
                    "Close": 0,
                    "Medium": 0,
                    "Long": 0,
                    "Extreme": 0
                },
                "Hunting Bow": {
                    "Close": 0,
                    "Medium": 0,
                    "Long": 0,
                    "Extreme": 0
                },
                "Heavy Weapons": {
                    "Close": 0,
                    "Medium": 0,
                    "Long": 0,
                    "Extreme": 0
                }
            }
        ]
    )
    char_hit_capacity: Dict[str, int] = field(
        default={
            "Head": 0,
            "Chest": 0,
            "Abdomen": 0,
            "Right Arm": 0,
            "Left Arm": 0,
            "Right Leg": 0,
            "Left Leg": 0
        }
    )
    char_gender: str = "Male"  # Male gender assumed due to the number of men in the military
    char_nationality: str = "USA"
    char_languages: List[str] = field(default="English")  # Default field must be set
    char_attributes: Dict[str, int] = field(default_factory=dict)  # If no default field, then use default factory
    char_background_skills: Dict[str, int] = field(default_factory=dict)
    char_careers: List[Dict[str, str]] = field(default=[{"Term 1": "", "Secondary Act": "", "Contact": ""}])
    char_skills: List[Dict[str, int]] = field(default_factory=list)


