# Testing commit for fun 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-a","--add",help="test")
args = parser.parse_args()

print("Creating args"+args.add)

