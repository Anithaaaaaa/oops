from Student import Anitha, Sindhu, Roja, Priya, Saniya

def main():
    anitha = Anitha("ECE", 3, 95)
    sindhu = Sindhu("ECE", 14, 96)
    roja = Roja("AIML", 5, 97)
    priya = priya("CSE", 2, 98)
    saniya = Saniya("EEE", 4, 99)
    
    anitha.display_details()
    print("\n")
    sindhu.display_details()
    print("\n")
    roja.display_details()
    print("\n")
    priya.display_details()
    print("\n")
    Saniya.display_details()
    print("\n")
    
if __name__ == "__main__":
    main()