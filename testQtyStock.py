import pytest
from QtyStock import calculate_optimal_purchase

@pytest.mark.parametrize(
    "price_item1, price_item2, total_budget, expected",
    [
        # Simple case, both items fit exactly
        (1012.20, 1059.78, 50000.0, (41, 8, 21.56)),
        # Large numbers
        (1012.20, 1059.78, 50000.0, (41, 8, 21.56)),
        
    ]
)
def test_calculate_optimal_purchase(price_item1, price_item2, total_budget, expected):
    assert calculate_optimal_purchase(price_item1, price_item2, total_budget) == expected