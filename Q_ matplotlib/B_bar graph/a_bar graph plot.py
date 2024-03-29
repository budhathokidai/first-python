import matplotlib.pyplot as plt

grade=["one","two","three","four","five"]
students =[10,25,37,48,69]

plt.figure(figsize=(10,5))

plt.bar(grade,students)
plt.title("students Bar graph")
plt.xlabel("Grade")
plt.ylabel("Number of students")
plt.show()