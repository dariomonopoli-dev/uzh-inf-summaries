import csv
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

countries_to_visualize = ["USA", "CHN", "IND", "BRA", "ZAF", "WLD"]
non_countries = [
    "ARB",
    "CEB",
    "CSS",
    "EAP",
    "EAR",
    "EAS",
    "ECA",
    "ECS",
    "EMU",
    "EUU",
    "FCS",
    "HIC",
    "HPC",
    "IBD",
    "IBT",
    "IDA",
    "IDB",
    "IDX",
    "LAC",
    "LCN",
    "LDC",
    "LIC",
    "LMC",
    "LMY",
    "LTE",
    "MEA",
    "MIC",
    "MNA",
    "NAC",
    "OED",
    "OSS",
    "PRE",
    "PSS",
    "PST",
    "SAS",
    "SSA",
    "SSF",
    "SST",
    "TEA",
    "TEC",
    "TLA",
    "TMN",
    "TSA",
    "TSS",
    "UMC",
    "WLD",
]

file_path = "WB_indicator.csv"

data_melted = []

country_code_idx = 1
year_start_index = 4

with open(file_path, mode="r", encoding="utf-8-sig") as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)

    for row in reader:
        country_code = row[country_code_idx] if country_code_idx < len(row) else None
        if country_code in countries_to_visualize or country_code == "WLD":
            print(f"Country in: {country_code}")
            print(len(headers))
            for i in range(year_start_index, len(headers)):
                year = headers[i]
                value = row[i] if i < len(row) else None  # Check for existence
                if value:  # Ensure there's a value
                    data_melted.append(
                        {
                            "Country Code": country_code,
                            "Year": int(year),
                            "Expense (% of GDP)": float(value),
                        }
                    )

assert len(data_melted) > 0, "Data is empty"
print(len(data_melted))
print(len(data_melted[0]))
# Sorting for plotting
data_melted.sort(key=lambda x: (x["Country Code"], x["Year"]))

plt.figure(figsize=(14, 8))
colors = list(mcolors.TABLEAU_COLORS.values())

for index, country in enumerate(countries_to_visualize):
    print(index, country)
    country_data = [item for item in data_melted if item["Country Code"] == country]
    years = [item["Year"] for item in country_data]
    expenses = [item["Expense (% of GDP)"] for item in country_data]

    plt.plot(
        years,
        expenses,
        marker="o",
        linestyle="-",
        color=colors[index % len(colors)],
        label=country,
    )

plt.title("Government Expense as % of GDP Over Time")
plt.xlabel("Year")
plt.ylabel("Expense (% of GDP)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
