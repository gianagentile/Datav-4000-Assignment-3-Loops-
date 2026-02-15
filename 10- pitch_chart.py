#  generate ASCII bar chart for projected reveune 
def visualize_revenue(yearly_revenue):
    print("Projected Revenue by Year (ASCII Style):\n")

    #loop 
    for year, revenue in enumerate(yearly_revenue, start=1): 
        bar_length = revenue // 1000 
        bar = '#' * bar_length
        print("Year", year, ":", bar)

def main():
    yearly_revenue = [3000, 5000, 8000, 12000]
    visualize_revenue(yearly_revenue)
main()
