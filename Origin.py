class Origin:
    def __init__(self):
        self.line_number = None
        self.point_number = None
        self.line_interval = None
        self.point_interval = None
        self.line_distance = None
        self.point_distance = None
        self.easting = None
        self.northing = None
        self.line_azimuth = None

    def get_coordinates(self, line, point):
        e = self.easting + (point - self.point_number) * (self.point_distance * self.point_interval)
        n = self.northing + (line - self.line_number) * (self.line_distance * self.line_interval)

        return [e, n]
