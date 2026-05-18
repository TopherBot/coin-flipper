#!/usr/bin/env python3
"""coin-flipper: flip a coin from the command line.

Run without arguments to flip once.
Provide a positive integer to flip that many times.
"""
import argparse, random, sys

def flip_one():
    return random.choice(['H', 'T'])

def main():
    parser = argparse.ArgumentParser(description='Flip a coin.')
    parser.add_argument('count', nargs='?', type=int, default=1,
                        help='Number of flips (default: 1)')
    args = parser.parse_args()
    if args.count < 1:
        sys.exit('error: count must be >= 1')
    results = [flip_one() for _ in range(args.count)]
    for i, r in enumerate(results, 1):
        print(f'Flip {i}: {r}')
    heads = results.count('H')
    tails = results.count('T')
    print('\nSummary:')
    print(f'  Heads: {heads} ({heads/args.count*100:.1f}%)')
    print(f'  Tails: {tails} ({tails/args.count*100:.1f}%)')

if __name__ == '__main__':
    main()
