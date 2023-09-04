import threading

def krasna_funkce():
    print(f"Zravi te krasna funkce: {threading.current_thread()}")


krasne_vlakno = threading.Thread(target=krasna_funkce)
krasne_vlakno.start()

total_threads = threading.active_count()
thread_name = threading.current_thread().name

print(f"Aktualne mi bezi {total_threads} vlakno")
print(f"Toto vlakno se jmenuje {thread_name}")

krasne_vlakno.join()

# race condition
