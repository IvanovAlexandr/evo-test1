import numpy as np

if __name__ == "__main__":
    array = np.random.random_integers(0, 9, (10, 10, 10))

    print(array)
    max_sum_x = 0
    index_max_sum_x = [0, 0]
    max_sum_y = 0
    index_max_sum_y = [0, 0]
    max_sum_z = 0
    index_max_sum_z = [0, 0]
    for j in range(10):
        for k in range(10):
            sum_x = 0
            sum_y = 0
            sum_z = 0
            for i in range(10):
                sum_z += array[i, j, k]
                sum_y += array[j, i, k]
                sum_x += array[j, k, i]

            if max_sum_z <= sum_z:
                max_sum_z = sum_z
                index_max_sum_z = [j, k]
            if max_sum_y <= sum_y:
                max_sum_y = sum_y
                index_max_sum_y = [j, k]
            if max_sum_x <= sum_x:
                max_sum_x = sum_x
                index_max_sum_x = [j, k]

    print("max_x -> [", index_max_sum_x[0], ",", index_max_sum_x[1], ", x ] = ", max_sum_x)
    print("max_y -> [", index_max_sum_y[0], ", y ,", index_max_sum_y[1], "] = ", max_sum_y)
    print("max z -> [ z ,", index_max_sum_z[0], ",", index_max_sum_z[1], "] = ", max_sum_z)
