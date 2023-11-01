with concurrent.futures.ThreadPoolExecutor(max_workers=CONNECTIONS) as executor:
    future_to_url = (executor.submit(sokolov_parse, url) for url in all_links)
    for future in tqdm(concurrent.futures.as_completed(future_to_url), total=len(all_links)):
        try:
            data = future.result() 
        except Exception as exc:      
            data = str(type(exc))
        finally:
            out.append(data)
