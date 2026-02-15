# caculate 10% commission 
def calculate_commission(sales_amount):
   return sales_amount * 0.10

# commission dictionary
def get_commission(sales):
    commisions = {}
#loop through employee
    for name in sales: 
        commisions[name] = calculate_commission(sales[name])
    return commisions

#print leaderboard
def print_leaderboard(commisions):
    print("Commission Leaderboard:")
    sorted_list = sorted(commisions.items(), key=lambda x: x[1], reverse=True)
    rank = 1
    for person, amount in sorted_list:
        print(str(rank) + ". " + person + "-", amount)
        rank += 1
    
def main():
    sales = {"Alice": 5000, "Bob": 7000, "Carol": 3000}
    comissions = get_commission(sales)
    print_leaderboard(comissions)

main()