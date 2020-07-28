name = input(" Welcome! What is your name? ")
Fitness_Plan = {
    "A": "Muscle Building",
    "B": "Stamina Building",
    "C": "Fat Burning"
}
goal = input(
    name + " What is your Fitness goal? (Type A B or C)" + str(Fitness_Plan))
print("Here are some suggestions. ")
if goal == "B":
    Fitness_Plan_list = [
        " 3x10 Push-ups, 3x10 Chair dips, 3x10 Squats, 1 min set of Side Planks"]
elif goal == "A":
    Fitness_Plan_list = [
        " 3x12 Biceps Curls, 3x12 Military Press, 3x12 Seated Rows,"]
elif goal == "C":
    Fitness_Plan_list = [" 30 mins of Jogging, 5x1 min High knees, 50 Jumping Jacks"]
else:
    print("Please enter the apporiate choice")
print(Fitness_Plan_list)
