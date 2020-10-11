from collections import namedtuple


class Origin(object):
    def __init__(self):
        self.line_number = 0.0
        self.point_number = 0.0
        self.line_interval = 0.0
        self.point_interval = 0.0
        self.line_distance = 0.0
        self.point_distance = 0.0
        self.easting = 0.0
        self.northing = 0.0
        self.line_azimuth = 0.0

    def get_coordinates(self, line, point):
        e = self.easting + (point - self.point_number) * (self.point_distance * self.point_interval)
        n = self.northing + (line - self.line_number) * (self.line_distance * self.line_interval)

        return [e, n]

    def serialize(self):
        return self.__dict__

    def deserialize(self, data):
        return namedtuple('Origin', data.keys())(*data.values())
