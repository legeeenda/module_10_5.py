import time
import multiprocessing
import os

def read_info(name):
  all_data = []
  try:
    with open(name, 'r') as f:
      line = f.readline()
      while line:
        all_data.append(line.strip())
        line = f.readline()
  except FileNotFoundError:
    print(f"Error: File '{name}' not found.")
  return len(all_data)

if __name__ == '__main__':
  num_files = 4
  for i in range(1, num_files + 1):
    filename = f'./file_{i}.txt'
    with open(filename, 'w') as f:
      for j in range(100000):
        f.write(f"Line {j+1} in file {i}\n")

  filenames = [f'./file_{number}.txt' for number in range(1, num_files + 1)]

  # Линейный вызов
  start_time = time.time()
  for filename in filenames:
    read_info(filename)
  end_time = time.time()
  elapsed_time = end_time - start_time
  print(f"{elapsed_time:.4f} линейный")


  # Многопроцессный вызов
  start_time = time.time()
  with multiprocessing.Pool() as pool:
    results = pool.map(read_info, filenames)
  end_time = time.time()
  elapsed_time = end_time - start_time
  print(f"{elapsed_time:.4f} многопроцессный")


