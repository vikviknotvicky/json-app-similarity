import argparse


parser = argparse.ArgumentParser(description='Find the best match for a given new JSON app object.')
parser.add_argument('--input', '-i', help='This is the path to the new JSON app object.',
                    required=True)
parser.add_argument('--apps_json', '-a', help='This is the path to the existing application JSONs')
