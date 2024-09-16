from datetime import datetime, timezone
from typing import Optional
from zoneinfo import ZoneInfo


def datetime_utcnow() -> datetime:
    """
    Get the current UTC time as an aware datetime object.

    Returns:
        datetime: The current time in UTC as an aware datetime object.
    """
    return datetime.now(timezone.utc)


def utc_from_timestamp(timestamp: float) -> datetime:
    """
    Convert a timestamp to an aware UTC datetime object.

    Args:
        timestamp (float): The timestamp to be converted.

    Returns:
        datetime: The corresponding aware UTC datetime object.
    """
    return datetime.fromtimestamp(timestamp, timezone.utc)


def naive_from_timestamp(timestamp: float) -> datetime:
    """
    Convert a timestamp to a naive datetime object (no timezone info).

    Args:
        timestamp (float): The timestamp to be converted.

    Returns:
        datetime: A naive datetime object.
    """
    return utc_from_timestamp(timestamp).replace(tzinfo=None)


def naive_utcnow() -> datetime:
    """
    Get the current UTC time as a naive datetime object (no timezone info).

    Returns:
        datetime: The current time as a naive datetime object.
    """
    return datetime_utcnow().replace(tzinfo=None)


def naive_from_dttz(
    timeobject: Optional[datetime], timezone_str: Optional[str]
) -> datetime:
    """
    Convert a timezone-aware datetime object to a naive
    datetime object after adjusting for the given timezone.

    Args:
        timeobject (datetime): The datetime
        object to be converted. Cannot be None.
        timezone_str (str): The timezone as
        a string (e.g., 'America/New_York'). Cannot be None.

    Raises:
        ValueError: If either the timeobject or timezone_str
        is None, or if an invalid timezone is provided.

    Returns:
        datetime: A naive datetime object after conversion
        to the specified timezone.
    """
    if timeobject is None:
        raise ValueError("timeobject cannot be None")
    if timezone_str is None:
        raise ValueError("timezone cannot be None")

    try:
        tz = ZoneInfo(timezone_str)
    except Exception as e:
        raise ValueError(f"Invalid timezone: {timezone_str}") from e

    # Set the timezone of the given timeobject
    date_new_tz = timeobject.replace(tzinfo=tz)

    # Convert to naive datetime after adjusting for the timezone
    return naive_from_timestamp(date_new_tz.timestamp())
