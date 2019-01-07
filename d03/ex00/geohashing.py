import sys
import antigravity


if __name__ == "__main__":
    try:
        if len(sys.argv) == 4:
            latitude = float(sys.argv[1])
            longitude = float(sys.argv[2])
            datedow = sys.argv[3].encode('utf-8')
            antigravity.geohash(latitude, longitude, datedow)
        else:
            raise IOError
    except (IOError, ValueError):
        print("Usage: python3 geohashing.py longitude latitude datedow\n"
              "longitude et latitude are floats and datedow must follow the below format\n"
              "Example: python3 geohashing.py 37.421542 -122.085589 2005-05-26-10458.68")
