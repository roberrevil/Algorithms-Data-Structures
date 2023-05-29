def fibonacci_series(n):
    series = [0, 1]  # Initialize the first two numbers
    
    while len(series) < n:  # Generate subsequent numbers until desired length
        next_number = series[-1] + series[-2]
        series.append(next_number)
    
    return series