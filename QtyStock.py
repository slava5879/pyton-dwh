def calculate_optimal_purchase(price_item1, price_item2, total_budget, add_amount=10):
    """
    Calculate the optimal quantities of two items to purchase within a given budget, minimizing the remaining budget.
    Args:
        price_item1 (float): The price of the first item.
        price_item2 (float): The price of the second item.
        total_budget (float): The total available budget.
    Returns:
        tuple: A tuple containing:
            - best_qty_item1 (int): The optimal quantity of the first item to purchase.
            - best_qty_item2 (int): The optimal quantity of the second item to purchase.
            - min_remainder (float): The minimal remaining budget after the purchase, rounded to two decimal places.
    The function iterates through all possible integer quantities of the first item that can be bought within the budget,
    then calculates the maximum possible quantity of the second item with the remaining budget. It selects the combination
    that leaves the smallest remainder, preferring combinations that spend more of the budget if multiple combinations
    leave the same remainder.
    """

    min_remainder = float('inf')  # Initialize the minimum remainder with infinity
    best_qty_item1 = 0
    best_qty_item2 = 0
    #add_amount = 10
    total_budget = total_budget + add_amount

    # Determine the maximum possible quantity of each item
    # Assume we can buy whole units of the item
    max_qty_item1 = int(total_budget // price_item1)
    max_qty_item2 = int(total_budget // price_item2)

    # Iterate through all possible quantities of item 1
    for qty_item1 in range(max_qty_item1 + 1):
        cost_item1 = qty_item1 * price_item1
        remaining_budget_for_item2 = total_budget - cost_item1

        # If the budget allows to buy at least some of item 2
        if remaining_budget_for_item2 >= 0:
            # Determine the maximum quantity of item 2 that can be bought
            qty_item2 = int(remaining_budget_for_item2 // price_item2)
            cost_item2 = qty_item2 * price_item2
            
            current_total_cost = cost_item1 + cost_item2
            current_remainder = total_budget - current_total_cost

            # Update if a better combination (with a smaller remainder) is found
            if current_remainder < min_remainder:
                min_remainder = current_remainder
                best_qty_item1 = qty_item1
                best_qty_item2 = qty_item2
            # If the remainder is the same, but more money was spent (closer to the budget)
            elif current_remainder == min_remainder and current_total_cost > (best_qty_item1 * price_item1 + best_qty_item2 * price_item2):
                best_qty_item1 = qty_item1
                best_qty_item2 = qty_item2
    
    add_investment = add_amount - min_remainder
    return best_qty_item1, best_qty_item2, add_investment # Round the remainder

if __name__ == "__main__":
    # Example usage
    price_item1 = 1012.6  # Price of item 1
    price_item2 = 1022.82  # Price of item 2
    total_budget = 50000.0  # Total budget

    qty_item1, qty_item2, add_investment = calculate_optimal_purchase(price_item1, price_item2, total_budget)
    
    print(f"Optimal quantity of item 1: {qty_item1}")
    print(f"Optimal quantity of item 2: {qty_item2}")
    print(f"Additional investment     : {add_investment:.2f}")