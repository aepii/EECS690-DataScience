import pandas as pd

def main():
  marathon_data = pd.read_csv("marathon_small.csv")

  marathon_data_top_25 = marathon_data.head(25)

  num_rows, num_cols = marathon_data.shape[0], marathon_data.shape[1]

  print(f"Top 25 Results:\n{marathon_data_top_25}")
  print(f"Number of Rows: {num_rows}\nNumber of Columns: {num_cols}")

  marathon_data_males = marathon_data[marathon_data["sex"] == "male"]

  print(f"Male Runners:\n{marathon_data_males}")

if __name__ == "__main__":
  main()