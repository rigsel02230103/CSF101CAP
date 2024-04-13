################################
 #Rigsel Pem
 #B.E,ECE
 #02230103
 ################################
 #REFERENCES
 #https://youtu.be/_uQrJ0TkZlc?si=1YyTxZd8pYt_qPl9
 #https://youtu.be/5yAEngAvL2E?si=2lEGPkxaRA3sJRqs
 #https://www.javatpoint.com/how-to-develop-a-game-in-python
 ################################
 #SOLUTION
 #YourSolutionScore: 49483
 #input_3_cap1.txt
 ################################

def read_input(file_path):
    """
    Reads the input file and returns a list of tuples containing shape and outcome.
    """
    with open(file_path, 'r') as file:
        rounds = [(line.strip().split()) for line in file]
    return rounds

def calculate_score(rounds):
    """
    Calculates the total score based on the rounds played.
    """
    # Using dictionary comprehension to define the score mapping
    score_mapping = {
        "A": {"X": 3, "Y": 4, "Z": 8},
        "B": {"X": 1, "Y": 5, "Z": 9},
        "C": {"X": 2, "Y": 6, "Z": 7}
    }
    
    # Calculating total score using a single line with dictionary comprehension
    total_score = sum(score_mapping[shape][outcome] for shape, outcome in rounds)
    
    return total_score

# Main program
file_path = "input_3_cap1.txt" # Replace with the path to your input file
rounds = read_input(file_path)
total_score = calculate_score(rounds)
print("Total Score:", total_score)
