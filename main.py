import pandas as pd
import plotly.express as px

savings = float(input("Enter starting savings amount: "))
saving_years = int(input("Enter how many years you would like to save for: "))
interest_rate = float(input("Enter projected earnings %: ").replace('%', ''))
add_per_year = float(input("Enter how much money you would like to add per year: "))
principle = savings


def calc_savings(savings, saving_years, interest_rate, add_per_year):
    projections = []

    for year in range(1, int(saving_years + 1)):
        interest = savings / 100 * interest_rate
        savings = savings + interest + add_per_year

        figures = {'Year': year, 'Savings': round(savings - interest, 2), 'Returns': round(interest, 2),
                   'EOY value': round(savings, 2)}
        print(figures)
        projections.append(figures)

    return projections


data = calc_savings(savings, saving_years, interest_rate, add_per_year)
df = pd.DataFrame(data)
fig = px.bar(df, x="Year", y="EOY value", title=f"Savings projections. {principle} Principle amount. "
                                                f"{interest_rate}% Interest per year."
                                                f"Savings added per year {add_per_year}")

fig.show()
