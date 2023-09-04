from concurrent.futures import ThreadPoolExecutor, as_completed


def _generate_in_batches(self, all_item_ids: Iterable[str]) -> Iterable[Tuple[str, List[str]]]:
   valid_ids = filter(_is_valid_item_id, all_item_ids)

   with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
       futures = []
       for batch in _batches(valid_ids, size=BATCH_SIZE):
           f = executor.submit(self._precompute_for_batch, batch)
           futures.append(f)

           # 5x max_workers to ensure worker threads have enough work while
           # items are uploaded to storage
           if len(futures) == 5 * self.max_workers:
               for f in as_completed(futures):
                   yield from f.result()
               futures = []

       if len(futures) > 0:
           for f in as_completed(futures):
               yield from f.result()
