# project revenue over # of years
def project_growth(initial_revenue, growth_rate):
    years = 10
    revenue = initial_revenue

    print("Year-by-Year Revenue Projection:")
    print("-----------------------------")
    for year in range(1, years + 1):
        print("Year", year, ":", round(revenue, 2))
        revenue += revenue * (growth_rate / 100)

    print ("------------------------------")
    print("Final Revenue after", years, "years:", round(revenue, 2))

def main():
    initial_revenue = float(input("Enter the initial revenue: "))
    growth_rate = float(input("Enter the annual growth rate (in %): "))
    project_growth(initial_revenue, growth_rate)

main()