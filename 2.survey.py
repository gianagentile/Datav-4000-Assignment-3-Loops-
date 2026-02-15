# count how much each choice appears
def count_preferences(data):
    counts = {}
#loop through the data and count each item
    for item in data:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts

# print market share %
def print_summary(counts,total):
    print("\nMarket Share Results:")
#loop through dictonary 
    for item in counts:
        percent = (counts[item] / total) * 100
        print(item + ": " + str(percent) + "%")

def main():
    responses = ["coffee", "tea","coffee", "soda" ]
    total_responses = len(responses)
    results = count_preferences(responses)
    print_summary(results, total_responses)
main()