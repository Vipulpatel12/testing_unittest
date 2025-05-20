import datetime
from typing import List, Dict
import random


class Product:
    def __init__(self, product_id: str, category: str, price: float):
        self.product_id = product_id
        self.category = category
        self.price = price



class User:
    def __init__(self, user_id: str, purchase_history: List[Dict], viewed_products: List[str]):
        self.user_id = user_id
        self.purchase_history = purchase_history  # List of dicts with product_id, date
        self.viewed_products = viewed_products

class RecommendationEngine:
    def __init__(self, products):
        if not isinstance(products, list):
            raise TypeError("Products must be a list")
        self.products = {p.product_id: p for p in products if hasattr(p, 'product_id')}

    def recommend(self, user, top_n=5):
        if not hasattr(user, 'purchase_history') or not hasattr(user, 'viewed_products'):
            raise AttributeError("User must have 'purchase_history' and 'viewed_products'")
        if not isinstance(top_n, int):
            raise TypeError("top_n must be an integer")

        scores = {pid: 0 for pid in self.products}
        today = datetime.date.today()

        for purchase in user.purchase_history:
            if 'product_id' not in purchase or 'date' not in purchase:
                raise KeyError("Each purchase must have 'product_id' and 'date'")
            pid = purchase['product_id']
            days_ago = (today - purchase['date']).days
            recency_score = max(0, 30 - days_ago)
            scores[pid] += recency_score * 1.5
            scores[pid] += 10  # frequency boost

        for pid in user.viewed_products:
            if pid in scores:
                scores[pid] += 5

        category_affinity = self._infer_affinity(user)
        for pid, product in self.products.items():
            if product.category in category_affinity:
                scores[pid] += category_affinity[product.category] * 2

            if self._is_within_price_range(user, product):
                scores[pid] += 3

        sorted_products = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        return [pid for pid, score in sorted_products[:top_n] if score > 0]



    def _infer_affinity(self, user: User) -> Dict[str, int]:
        affinity = {}
        for purchase in user.purchase_history:
            pid = purchase['product_id']
            if pid in self.products:
                cat = self.products[pid].category
                affinity[cat] = affinity.get(cat, 0) + 1
        return affinity

    def _is_within_price_range(self, user: User, product: Product) -> bool:
        if not user.purchase_history:
            return True  # assume no bias
        prices = [self.products[p['product_id']].price for p in user.purchase_history if p['product_id'] in self.products]
        avg_price = sum(prices) / len(prices)
        return abs(product.price - avg_price) < avg_price * 0.5


# Sample Usage
if __name__ == "__main__":
    products = [
        Product("p1", "electronics", 199.99),
        Product("p2", "fashion", 29.99),
        Product("p3", "books", 9.99),
        Product("p4", "electronics", 149.99),
        Product("p5", "fashion", 39.99),
        Product("p6", "books", 15.99),
        Product("p7", "fitness", 89.99),
        Product("p8", "electronics", 299.99),
    ]

    user = User(
        user_id="u1",
        purchase_history=[
            {"product_id": "p1", "date": datetime.date.today() - datetime.timedelta(days=3)},
            {"product_id": "p2", "date": datetime.date.today() - datetime.timedelta(days=15)},
        ],
        viewed_products=["p3", "p4", "p7"]
    )

    engine = RecommendationEngine(products)
    recommendations = engine.recommend(user, top_n=5)
    print("Top Recommendations:", recommendations)
