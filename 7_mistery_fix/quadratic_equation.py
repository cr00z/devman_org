import argparse
from math import sqrt


def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None, None
    root1 = (-b - sqrt(discriminant)) / (2 * a)
    root2 = (-b + sqrt(discriminant)) / (2 * a)
    if discriminant > 0:
        return root1, root2
    else:
        return root1, None


def get_cmdline_args():
    parser = argparse.ArgumentParser(
        description='universal Quadratic ("square") equation solver')
    parser.add_argument('coef_a', metavar='coef_A', type=float,
                        help='coefficient A of the equation')
    parser.add_argument('coef_b', metavar='coef_B', type=float,
                        help='coefficient B of the equation')
    parser.add_argument('coef_c', metavar='coef_C', type=float,
                        help='coefficient C of the equation')
    return parser.parse_args()


if __name__ == '__main__':
    args = get_cmdline_args()
    solutions = get_roots(args.coef_a, args.coef_b, args.coef_c)
    if solutions[0] is None:
        answer = 'No real solution'
    elif solutions[1] is None:
        answer = 'double root is {}'.format(solutions[0])
    else:
        answer = 'root1 is {0[0]}, root2 is {0[1]}'.format(solutions)
    print(answer)
