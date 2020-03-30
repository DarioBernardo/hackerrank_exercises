"""
Exercise as explained here:
https://vimeo.com/158532188
minute 1:10
The password is FB_IPS

Explanation:
You have a group of people, birth year and death year
find the year with most people alive.
"""

# DATA GENERATION
import numpy as np
import random


# Parameters
POP_SIZE = 100
MEAN_LIFE_SPAN = 80
STD_LIFE_SPAN = 10

population = []
for i in range(0, POP_SIZE):
    birth = random.randint(1800, 2010)
    death = np.random.normal(MEAN_LIFE_SPAN,STD_LIFE_SPAN)
    death = birth + int(death)
    population.append({"birth": birth, "death": death})

    print(f"{birth} {death}")


def find_year_with_most_people_alive(population: list) -> int:

    year_population_counter = {}
    # For each person in population
        # for each year the person is alive, increase counter

    # go through all years and find max

    # complexity:
    # assuming p is pop size, l = max lifespan () and y = min(birth) - max(death)
    # complexity is O(p * l + y)
    # NOT GOOD.

    # INSTEAD:
    # We could have two lists, births and deaths, and then have a global population counter which increases when
    # someone is born and is decreased when someone dies. At this point, every time it is increased I can just keep
    # track of its max value

    births = []
    deaths = []
    for person in population:
        births.append(person["birth"])
        deaths.append(person["death"])

    sorted_births = sorted(births)
    sorted_deaths = sorted(deaths)

    """
    [1950, 1953, 1980, 1988, 2000] 5
    [1970, 1980, 1987, 2005, 2006] 5
    
    birth_index = 0
    death_index = 0
    """

    birth_index = 0
    death_index = 0
    global_population_counter = 0
    max_pop = 0

    while birth_index < len(sorted_births) and death_index < len(sorted_deaths):
        birth_date = sorted_births[birth_index]
        death_date = sorted_deaths[death_index]
        if birth_date < death_date:
            global_population_counter += 1
            max_pop = max(max_pop, global_population_counter)
            birth_index += 1

        if birth_date > death_date:
            global_population_counter -= 1
            death_index += 1

        if birth_date == death_date:
            birth_index += 1
            death_index += 1

        # print(f"current pop {global_population_counter}")

    print(f"{max_pop} {len(sorted_births[birth_index:])} {len(sorted_deaths[death_index:])} ")
    global_population_counter += (len(sorted_births[birth_index:]) - len(sorted_deaths[death_index:]))
    max_pop = max(max_pop, global_population_counter)

    return max_pop


highest_population = find_year_with_most_people_alive(population)
print(f"Highest pop number {highest_population}")
