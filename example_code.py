def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Parameters:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.
    
    Returns:
    float: The area of the rectangle.
    """
    return length * width

# Example usage
if __name__ == "__main__":
    length = 5.0
    width = 3.0
    area = calculate_area(length, width)
    print(f"The area of the rectangle is: {area}")
