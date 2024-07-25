def fetch_all_employee_data(employee_ids):
    results = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(fetch_employee_data, emp_id): emp_id for emp_id in employee_ids}
        for future in as_completed(futures):
            emp_id = futures[future]
            try:
                data = future.result()
                if data:
                    results.append({'employee_id': emp_id, 'age': data['age'], 'gender': data['gender']})
            except Exception as e:
                print(f"Error fetching data for employee ID {emp_id}: {e}")
    return results
