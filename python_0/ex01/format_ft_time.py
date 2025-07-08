import time
from datetime import datetime

def format_ft_time():
    current_timestamp_ms = time.time()

    formatted_timestamp_standard = f"{current_timestamp_ms:,.4f}"

    formatted_timestamp_scientific = f"{current_timestamp_ms:.2e}"

    dt_object = datetime.fromtimestamp(current_timestamp_ms)

    formatted_date_string = dt_object.strftime("%b %d %Y")

    output = (
        f"Seconds since January 1, 1970: {formatted_timestamp_standard} "
        f"or {formatted_timestamp_scientific} in scientific notation\n"
        f"{formatted_date_string}"
    )
    print(output)

if __name__ == "__main__":
    format_ft_time()
