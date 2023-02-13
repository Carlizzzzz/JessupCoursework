flight_length = 14
movies = [2, 3, 10, 3, 5, 7]


def jessflix(length, movies):
    for i in range(0, len(movies)):
        for j in range(0, len(movies)):
            if i == j:
                break
            if length - movies[i] == movies[j]:
                return True
    return False


print(jessflix(flight_length, movies))