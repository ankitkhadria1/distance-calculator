import json
import logging
from math import radians, sin, cos, acos

logger = logging.getLogger(__name__)

class CalculateDistance(object):
    """
        Class to get distance between two lat, long position between point using great circle distance.
    """
    def __init__(self, lat, long):
        self.home_location_lat = lat
        self.home_location_long = long

    def great_circle(self, lon1, lat1, lon2, lat2):
        lon1, lat1, lon2, lat2 = float(lon1), float(lat1), float(lon2), float(lat2)
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        return 6371 * (
            acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon1 - lon2))
        )

    def caluate_distance(self, destination_long: str, destination_lat: str) -> float:
        return self.great_circle(self.home_location_long, self.home_location_lat, destination_long, destination_lat)


if __name__ == "__main__":

    home_pos_lat = "53.339428"
    home_pos_long = "-6.257664"
    user_data_obj = CalculateDistance(home_pos_lat, home_pos_lat)
    res = user_data_obj.caluate_distance("52.986375", "-6.043701")
    logger.warn(res)
