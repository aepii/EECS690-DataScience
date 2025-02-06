import pandas as pd
import altair as alt 

def main():
    hp_report = pd.read_csv("../files/happiness_report.csv")
    hp_report_semi_colon = pd.read_csv("../files/happiness_report_semicolon.csv", sep=";")
    hp_report_meta_data = pd.read_csv("../files/happiness_report_metadata.csv", skiprows=2)
    hp_report_xlsx = pd.read_excel("../files/happiness_report.xlsx")

    print(hp_report_xlsx)

if __name__ == "__main__":
    main()