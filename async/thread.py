# pid
import os
import threading


print(f"Aktualne bezim pod ideckem {os.getpid()}")

total_threads = threading.active_count()
thread_name = threading.current_thread().name

print(f"Aktualne mi bezi {total_threads} vlakno")
print(f"Toto vlakno se jmenuje {thread_name}")
