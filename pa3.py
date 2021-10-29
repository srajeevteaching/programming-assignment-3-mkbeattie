# Katie Beattie
# CS151 Dr. Rajeev
# October 28, 2021
# Programming Assignment 3

choice = input("Choose a target sport: football, quiddich, or gymnastics? ")
choice.strip().lower()
if choice == "football":
    def statistic_f (completions, attempts, passing_yards, touchdown_passes, interceptions):
        stat_f = [100 * (5 * (completions / attempts – 0.30) + 0.25 * (passing_yards / attempts - 3) + 20 * (touchdown_passes / attempts) + 2.375 – (25 * interceptions / attempts)] / 6
        print("The quarterback's rating is: ", stat_f)
    def main():
        completions = input("Enter the quarterback's completions. ")
        attempts = input("Enter the team's touchdown attempts. ")
        passing_yards = input("Enter the quarterback's total passing yards. ")
        touchdown_passes = input("Enter the quarterback's touchdown passes. ")
        interceptions = input("Enter the team's interceptions. ")
        if completions.isdigit() and completions != 0:
            if attempts.isDigit() and attempts != 0:
                if passing_yards.isDigit() and passing_yards != 0:
                    if touchdown_passes.isDigit() and touchdown_passes != 0:
                        statistic_f(completions, attempts, passing_yards, touchdown_passes, interceptions)
                    else:
                        print("Error! Result of calculation: 0")
                else:
                    print("Error! Result of calculation: 0")
            else:
                print("Error! Result of calculation: 0")
        else:
            print("Error! Result of calculation: 0")
    print("The quarterback's rating is : ", statistic_f(completions, attempts, passing_yards, touchdown_passes, interceptions))
elif choice == "quiddich":
    def statistic_qy (goals, snitch):
        stat_qy = (10 * goals) + diff
        print("The team's total score is: ", stat_qy)

    def statistic_qn(goals, snitch):
        stat_qn = 10 * goals
        print("The team's total score is: ", stat_qn)
    def main():
        goals = input("How many times did the team score? ")
        snitch = input("Did the team catch the snitch? ")
        snitch.strip().lower()
        if goals.isDigit() and goals != 0:
            if snitch == "yes":
                statistic_qy(goals, snitch)
            elif snitch == "no":
                statistic_qy(goals, snitch)
        else:
            print("Error! Result of calculation: 0")
elif choice == "gymnastics":
    def statistic_g (ex1, ex2, ex3, ex4, ex5, diff):
        stat_g = ((ex1 + ex2 + ex3 + ex4 + ex5) / 5) + diff
        print("Gymnast's total score is :", stat_g)
    def main():
        ex1 = input("Enter the 1st 0-to-10 execution score: ")
        ex2 = input("Enter the 2nd 0-to-10 execution score: ")
        ex3 = input("Enter the 3rd 0-to-10 execution score: ")
        ex4 = input("Enter the 4th 0-to-10 execution score: ")
        ex5 = input("Enter the 5th 0-to-10 execution score: ")
        diff = input("Enter the 0-to-10 difficulty score: ")
        if ex1.isDigit():
            if ex2.isDigit():
                if ex3.isDigit():
                    if ex4.isDigit():
                        if ex5.isDigit():
                            if diff.isDigit():
                                statistic_g(ex1, ex2, ex3, ex4, ex5, diff)
                            else:
                                print("Error! Result of calculation: 0")
                        else:
                            print("Error! Result of calculation: 0")
                    else:
                        print("Error! Result of calculation: 0")
                else:
                    print("Error! Result of calculation: 0")
            else:
                print("Error! Result of calculation: 0")
        else:
            print("Error! Result of calculation: 0")
else:
    print"Invalid choice!")
