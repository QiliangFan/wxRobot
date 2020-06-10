from EpidemicPrevention.EpidemicPrevention import EpidemicPrevention
import sys


if __name__ == "__main__":
    epidemic_prevention = EpidemicPrevention(bool(sys.argv[1] if len(sys.argv) > 1 else ""))