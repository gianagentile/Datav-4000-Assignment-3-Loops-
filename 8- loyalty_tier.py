#assign loyality tier based on purchase amount 
def assign_tier(amount):
    if amount < 1000: 
        return "Bronze"
    elif amount < 5000:
        return "Silver"
    else:
        return "Gold"   
# count customers in each tier
def count_tiers(customers):
    tier_counts = {"Bronze": 0, "Silver": 0, "Gold": 0}
#loop 
    for customer, amount in customers.items():
        tier = assign_tier(amount)
        tier_counts[tier] += 1
    return tier_counts

#display tier summary 
def print_summary(tier_counts):
    print("Customer Loyalty Tier Summary:")
    for tier in tier_counts:
        print(tier + ": " + str(tier_counts[tier]))
#main function
def main():
    customers = {
        "Alice": 500,
        "Bob": 2500,
        "Carol": 6000,
        "David": 800,
        "Eve": 4500
    }
#count each customer in teir and print 
    tier_counts = count_tiers(customers)
    print_summary(tier_counts)

main()
