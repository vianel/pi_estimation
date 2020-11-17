import random
import math
import statistics

def throw_needle(needle_numbers):
    inside_circle = 0

    for _ in range(needle_numbers):
        x = random.random() * random.choice([-1, 1])
        y = random.random() * random.choice([-1, 1])

        distance_from_the_center = math.sqrt(x**2 + y**2)

        if distance_from_the_center <= 1:
            inside_circle += 1

    return (4 * inside_circle) / needle_numbers

def estimate(needle_numbers, attemps):
    pi_estimations = []

    for _ in range(attemps):
       pi = throw_needle(needle_numbers)
       pi_estimations.append(pi)

    pi_avg = statistics.mean(pi_estimations)
    sigma = statistics.pstdev(pi_estimations)
    print(f'Pi estimation is {round(pi_avg, 5)} with standard deviation of {round(sigma, 5)} using in total {needle_numbers} needles')

    return (pi_avg, sigma)

def main(precission, attemps):
    needle_numbers = 1000
    sigma = precission

    while sigma >= precission / 1.96:
        avg, sigma = estimate(needle_numbers, attemps)

        needle_numbers *= 2

    return avg

if __name__ == '__main__':
    main(0.01, 1000)
