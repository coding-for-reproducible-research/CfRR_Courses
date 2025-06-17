import psutil

def get_cpu_info():
    """Retrieves CPU specifications and usage."""

    try:
        # Get CPU count
        cpu_count = psutil.cpu_count(logical=False) # Get physical cores
        cores = psutil.cpu_count(logical=True) # Get logical cores
        
        return f"CPU: {cpu_count} physical cores, {cores} logical cores"

    except Exception as e:
        print(f"Error getting CPU info: {e}")
        return None

def get_ram_info():
    """Retrieves memory information."""

    try:
        memory_info = psutil.virtual_memory() # Get virtual memory usage
        total_memory_gb = memory_info.total / (1024**3) # Convert to GB

        return f"RAM: Total {total_memory_gb:.2f} GB"

    except Exception as e:
        print(f"Error getting RAM info: {e}")
        return None

print(get_cpu_info())
print(get_ram_info())

