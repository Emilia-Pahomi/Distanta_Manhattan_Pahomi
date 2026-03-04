from functii import manhattan_scipy, manhattan_manual, citeste

def main():
    try:
        
        vector_a, vector_b = citeste('data.txt')
        print(f"Vector A: {vector_a}")
        print(f"Vector B: {vector_b}")

        
        dist_manual = manhattan_manual(vector_a, vector_b)
        
        
        dist_scipy = manhattan_scipy(vector_a, vector_b)

        print(f"Distanta Manhattan (Manual): {dist_manual}")
        print(f"Distanta Manhattan (SciPy):  {dist_scipy}")

    except FileNotFoundError:
        print("Error: data.txt not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()