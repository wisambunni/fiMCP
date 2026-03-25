from typing import Any


def truncate_indicator_first_n(payload: Any, n: int = 10) -> Any:
    """For Technical Indicator responses, keep only the first n date entries.

    - Applies only to keys containing "Technical Analysis".
    - Assumes the API already orders dates newest→oldest.
    - Leaves non-indicator sections (e.g., "Meta Data", time series) untouched.
    - This is helpful to avoid exceeding context window with each request
      as most of these indicators return a massive JSON response Claude has to consume
    """
    try:
        if not isinstance(payload, dict):
            return payload
        new_payload: dict[str, Any] = {}
        for k, v in payload.items():
            if isinstance(k, str) and "Technical Analysis" in k and isinstance(v, dict):
                # Take first n items as-is (preserve existing order)
                first_n_items = list(v.items())[:n]
                new_payload[k] = {dk: dv for dk, dv in first_n_items}
            else:
                new_payload[k] = v
        return new_payload
    except Exception:
        return payload