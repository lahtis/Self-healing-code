import json
from pathlib import Path
from jsonschema import validate, ValidationError


def validate_ucr(ucr_path: str | Path, schema_path: str | Path):
    """
    Validates a UCR JSON file against the UCR schema.
    Raises ValidationError if invalid.
    """

    ucr_path = Path(ucr_path)
    schema_path = Path(schema_path)

    with open(ucr_path, "r", encoding="utf-8") as f:
        ucr_data = json.load(f)

    with open(schema_path, "r", encoding="utf-8") as f:
        schema = json.load(f)

    try:
        validate(instance=ucr_data, schema=schema)
        return True

    except ValidationError as e:
        raise ValidationError(
            f"UCR validation failed at {list(e.path)}: {e.message}"
        )
