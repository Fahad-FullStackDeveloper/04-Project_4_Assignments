SENTENCE_START : str = "Panaversity is fun. I learned to program and used Python to solve problems. I am excited to learn more about programming and computer science."
def main():
    
    adjective : str = str(input("Please type an adjective and press enter. "))
    noun : str = str(input("Please type a noun and press enter. "))
    verb : str = str(input("Please type a verb and press enter. "))
    
    print(SENTENCE_START + adjective + " " + noun + " " + verb + "!")
    
if __name__ == "__main__":
    main()