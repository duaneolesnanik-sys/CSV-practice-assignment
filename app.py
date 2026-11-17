import csv

def main():
    with open("student_test_scores.csv", "r", newline = "") as file:
        content = list(csv.DictReader(file))
    passing = [list(student.values()) for student in content if int(student["Test Score"]) >= 70]
    failing = [list(student.values()) for student in content if int(student["Test Score"]) < 70]
    with open("passed.csv", "w", newline = "") as file:
        writer = csv.writer(file)
        writer.writerows(passing)
    with open("failed.csv", "w", newline = "") as file:
        writer = csv.writer(file)
        writer.writerows(failing)
    content.sort(key = lambda x: int(x["Test Score"]))
    scores = [int(student["Test Score"])  for student in content]
    print(f"Highest Score: {content[-1]["Student"]} \nLowest Score: {content[0]["Student"]} \nAverage: {sum(scores)/len(scores)}")
    

if __name__ == "__main__":
    main()

