def calculate_optimal_purchase(price_item1, price_item2, fee, total_budget, add_amount, priority=False, item='item1'):

   min_remainder = float('inf')  # Initialize the minimum remainder with infinity
   best_qty_item1 = 0
   best_qty_item2 = 0
   total_budget = total_budget + add_amount

   if price_item1 <= 0:
        price_item1 = 1000000
   if price_item2 <= 0:
        price_item2 = 1000000  # Set to a very high value to avoid division by zero

   # add fee to the prices
   price_item1_with_fee = price_item1 * (1 + fee / 100)
   price_item2_with_fee = price_item2 * (1 + fee / 100)

   # Determine the maximum possible quantity of each item
   # Assume we can buy whole units of the item
   max_qty_item1 = int(total_budget // price_item1_with_fee)
   #max_qty_item2 = int(total_budget // price_item2_with_fee)

   # Iterate through all possible quantities of item 1
   for qty_item1 in range(max_qty_item1 + 1):
       cost_item1 = qty_item1 * price_item1_with_fee
       remaining_budget_for_item2 = total_budget - cost_item1

       # If the budget allows to buy at least some of item 2
       if remaining_budget_for_item2 >= 0:
           # Determine the maximum quantity of item 2 that can be bought
           qty_item2 = int(remaining_budget_for_item2 // price_item2_with_fee)

           # Apply priority constraint if enabled
           if priority:
               if item == 'item1':
                   # item1 must have strictly more than item2
                   if qty_item1 <= qty_item2:
                       continue  # Skip: item1 qty not greater
               elif item == 'item2':
                   # item2 must have strictly more than item1
                   if qty_item2 <= qty_item1:
                       continue  # Skip: item2 qty not greater

           cost_item2 = qty_item2 * price_item2_with_fee
           current_total_cost = cost_item1 + cost_item2
           current_remainder = total_budget - current_total_cost

           # Update if a better combination (with a smaller remainder) is found
           if current_remainder < min_remainder:
               min_remainder = current_remainder
               best_qty_item1 = qty_item1
               best_qty_item2 = qty_item2

           # If the remainder is the same, but more money was spent (closer to the budget)
           elif current_remainder == min_remainder and current_total_cost > (best_qty_item1 * price_item1_with_fee + best_qty_item2 * price_item2_with_fee):
               best_qty_item1 = qty_item1
               best_qty_item2 = qty_item2

   add_investment = add_amount - min_remainder

   # Validate priority constraint was met
   if priority and (best_qty_item1 > 0 or best_qty_item2 > 0):
       if item == 'item1' and best_qty_item1 <= best_qty_item2:
           print(f"WARNING: Priority constraint violated! item1 ({best_qty_item1}) should be > item2 ({best_qty_item2})")
       elif item == 'item2' and best_qty_item2 <= best_qty_item1:
           print(f"WARNING: Priority constraint violated! item2 ({best_qty_item2}) should be > item1 ({best_qty_item1})")

   return best_qty_item1, best_qty_item2, add_investment

if __name__ == "__main__":

   fee = 0.2                   # 0.2% fee
   price_item1 = 1023.08       # Price of item 1
   price_item2 = 1047.49       # Price of item 2
   total_budget = 100000        # Total budget

   # Test 1: No priority (original behavior)
   print("=" * 60)
   print("Test 1: No priority constraint")
   print("=" * 60)
   qty_item1, qty_item2, add_investment = calculate_optimal_purchase(price_item1,
                                                                     price_item2,
                                                                     fee,
                                                                     total_budget,
                                                                     add_amount=0,
                                                                     priority=False,
                                                                     item='item1')

   print(f"Optimal quantity of item 1: {qty_item1}")
   print(f"Optimal quantity of item 2: {qty_item2}")
   print(f"Price1 with fee           : {price_item1 * (1 + fee / 100):.3f}")
   print(f"Price2 with fee           : {price_item2 * (1 + fee / 100):.2f}")
   print(f"Total budget              : {total_budget:.2f}")
   print(f"Additional investment     : {add_investment:.2f}")

   # Test 2: Priority on item1 (item1 qty must be > item2 qty)
   print("\n" + "=" * 60)
   print("Test 2: Priority on item1 (item1 qty > item2 qty)")
   print("=" * 60)
   qty_item1, qty_item2, add_investment = calculate_optimal_purchase(price_item1,
                                                                     price_item2,
                                                                     fee,
                                                                     total_budget,
                                                                     add_amount=0,
                                                                     priority=True,
                                                                     item='item1')

   print(f"Optimal quantity of item 1: {qty_item1}")
   print(f"Optimal quantity of item 2: {qty_item2}")
   #print(f"Constraint check (item1 > item2): {qty_item1} > {qty_item2} = {qty_item1 > qty_item2}")
   print(f"Additional investment     : {add_investment:.2f}")

   # Test 3: Priority on item2 (item2 qty must be > item1 qty)
   print("\n" + "=" * 60)
   print("Test 3: Priority on item2 (item2 qty > item1 qty)")
   print("=" * 60)
   qty_item1, qty_item2, add_investment = calculate_optimal_purchase(price_item1,
                                                                     price_item2,
                                                                     fee,
                                                                     total_budget,
                                                                     add_amount=0,
                                                                     priority=True,
                                                                     item='item2')

   print(f"Optimal quantity of item 1: {qty_item1}")
   print(f"Optimal quantity of item 2: {qty_item2}")
   #print(f"Constraint check (item2 > item1): {qty_item2} > {qty_item1} = {qty_item2 > qty_item1}")
   print(f"Additional investment     : {add_investment:.2f}")
