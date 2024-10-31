import copy
import random


class Hat():
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for _ in range(value):
                self.contents.append(key)

    def draw(self, number_of_balls):
        result_list = []
        if len(self.contents) <= number_of_balls:
            result_list = self.contents
            self.contents = []
            return result_list
        for _ in range(number_of_balls):
            index = random.randint(0, len(self.contents)-1)
            # print(index)
            result_list.append(self.contents.pop(index))

        return result_list


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_match = 0
    for _ in range(num_experiments):
        new_hat = copy.deepcopy(hat)
        balls_drawn = new_hat.draw(num_balls_drawn)
        ball_count = {x: balls_drawn.count(x) for x in set(balls_drawn)}
        is_expected = True
        # print(ball_count)
        for key, value in expected_balls.items():
            # print(key, value)
            # print(f'{key}' in ball_count)
            if f'{key}' in ball_count:
                if ball_count[key] < value:
                    is_expected = False
            else:
                is_expected = False
                break

        if is_expected:
            expected_match += 1
    # print(expected_match)
    return expected_match/num_experiments


hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)

print(hat2.contents)
print(hat2.draw(9))
print(hat2.contents)
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                         expected_balls={'red': 2, 'green': 1},
                         num_balls_drawn=5,
                         num_experiments=2000)

print(probability)
