#!/usr/bin/env python3
"""
Test Repository - Main Module

A simple Python script for demonstration purposes.
"""

def hello_world():
    """Print a hello world message."""
    print("Hello, World!")
    print("This is a test repository!")

def add_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b

def main():
    """Main function."""
    hello_world()
    
    # Test the add function
    result = add_numbers(5, 3)
    print(f"5 + 3 = {result}")
    
    print("Test repository is working correctly!")

if __name__ == "__main__":
    main()
