import heapq

def min_cost_to_connect_cables(cables):

  heapq.heapify(cables)  # Перетворюємо список у купу 
  total_cost = 0
  while len(cables) > 1:
    # Витягуємо два найкоротші кабелі
    cable1 = heapq.heappop(cables)
    cable2 = heapq.heappop(cables)
    
    # Обчислюємо вартість їх з'єднання
    cost = cable1 + cable2
    total_cost += cost
    
    # Додаємо новий кабель до купи
    heapq.heappush(cables, cost)
  
  return total_cost

cables = [5, 2, 9, 1, 5, 6]
min_cost = min_cost_to_connect_cables(cables)
print(f"Мінімальна вартість з'єднання кабелів: {min_cost}")