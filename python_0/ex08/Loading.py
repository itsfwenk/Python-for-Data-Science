import time
import shutil

def format_time(seconds):
    """
    Format seconds into MM:SS

    Args:
        arg1 (int): Seconds to format.

    Returns:
        str: Time formatted as MM:SS
    """
    minutes, seconds = divmod(int(seconds), 60)
    return f"{minutes:02d}:{seconds:02d}"

def ft_tqdm(lst: range) -> None:
    """
    Show a progress bar for loops and iterables

    Args:
        lst (range): The range object to iterate over.

    Yields:
        Any: The current element from the range.

     """
    total = len(lst)
    start_time = time.time()

    progress_bar_width = shutil.get_terminal_size().columns - 40

    for i, item in enumerate(lst, start=1):
        progress = int(i / total * progress_bar_width)
        elapsed_time = time.time() - start_time
        speed = i / elapsed_time
        eta = (total - i) / speed

        elapsed_formatted = format_time(elapsed_time)
        eta_formatted = format_time(eta)

        progress_bar = f"|{'█' * progress:<{progress_bar_width}}|"
        progress_percentage = progress * 100 // progress_bar_width
        progress_info = f"{progress_percentage}%{progress_bar} {i}/{total}"
        time_info = f"[{elapsed_formatted}<{eta_formatted}, {speed:.2f}it/s]"

        print(f"\r{progress_info} {time_info}", end="", flush=True)
        yield item

def main():
    for _ in ft_tqdm(range(0, 333)):
        pass


if __name__ == "__main__":
    main()