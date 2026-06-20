from random import choice

class Randomwalk:
    def __init__(self, x_values = 0, y_values = 0,num_points = 50000):
        self.num_points = num_points

        self.x_values = [x_values]
        self.y_values = [y_values]

    def get_step(self):
            direction = choice([1,-1])
            distance = choice([0,1,2,3,4,5])
            step = direction*distance
            return step

    def fill_walk(self):
        while len(self.x_values)< self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()
            if y_step == 0 or x_step ==0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)



       