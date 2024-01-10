import csv
import threading
import subprocess

def process_account(row, result_list):
    username, password = row[0], row[1]

    try:
        output_bytes = subprocess.check_output(["python", "one_account.py", username, password])
        output = output_bytes.decode('utf-8')  # Use utf-8 encoding to decode the bytes
    except subprocess.CalledProcessError as e:
        output = f"Error: {e.output.decode('utf-8')}"  # Use utf-8 encoding to decode the error output

    result_list.append((username, output))  # 将结果存入结果列表

if __name__ == '__main__':
    success = 0
    count = 0
    all_results = []  # 用于存储每个线程的结果列表

    with open('account.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        threads = []

        for row in reader:
            count += 1
            print(f'用户{count}: {row[2]}({row[0]})')

            # 创建一个线程并启动，为每个线程创建独立的结果列表
            results = []
            thread = threading.Thread(target=process_account, args=(row, results))
            threads.append(thread)
            thread.start()

            # 将每个线程的结果列表存入总的结果列表
            all_results.append(results)

        # 等待所有线程执行完毕
        for thread in threads:
            thread.join()
    print('\n所有用户运行完毕\n')
    # 统计成功和失败的用户
    for results in all_results:
        for username, output in results:
            if "Error" not in output:
                success += 1
            print(f'用户{username}运行结果：\n{output}')

    print(f'共{count}个用户，成功{success}个，失败{count - success}个')
