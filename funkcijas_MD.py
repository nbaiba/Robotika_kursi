def get_city_year(p0, perc, delta, p):
    years = 0
    
    while p0 < p:
        p0 += p0 * perc / 100 + delta
        years += 1
        
        if p0 >= p:
            return years
    
    return -1

assert get_city_year(1000, 2, 50, 1200) == 3
assert get_city_year(1000, 2, -50, 5000) == -1
assert get_city_year(1500, 5, 100, 5000) == 15
assert get_city_year(1500000, 2.5, 10000, 2000000) == 10


