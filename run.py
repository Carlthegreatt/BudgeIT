import sys
import os

# Add the current directory to Python path to ensure proper imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    from budgeit.__main__ import main

    main()
