#CREATE DATASET FOR 10 STUDENTS
import numpy as np 
np.random.seed(42)
students=np.array([
    "PRABHU", "RAJESH", "CHARAN", "DENNIS", "EVELYN",
    "MANJULA", "NILA", "BHAGYA", "PRIYA", "AISHWARYA"
])
study_hours=np.random.randint(1, 10,10)
attendance=np.random.randint(50, 101,10)
assignment=np.random.randint(3, 11,10)
marks=np.random.randint(30, 101,10)
#LETS SEE THE DATA
print("STUDENTS:",students)
print("STUDY HOURS:",study_hours)
print("ATTENDANCE:",attendance)
print("ASSIGNMENT:",assignment)
print("MARKS:",marks)
#LETS SEE THE SHAPE OF THE DATA
print("STUDENTS SHAPE:",students.shape)
print("STUDY HOURS SHAPE:",study_hours.shape)
print("ATTENDANCE SHAPE:",attendance.shape)
print("ASSIGNMENT SHAPE:",assignment.shape)
print("MARKS SHAPE:",marks.shape)
#COMBINE THE NUMERICAL DATA INTO A SINGLE ARRAY
data=np.column_stack((study_hours, attendance, assignment, marks))
print("COMBINED DATA:",data)
print(data.shape)
#WE WANT FEATURES AND TARGET SEPARATELY
x=data[:,:-1] #FEATURES
y=data[:,-1] #TARGET
#LETS SEE THE FEATURES AND TARGET
print("FEATURES:",x)    
print("TARGET:",y)
#STUDENT WHO SCORED ABOVE 70
high_scorers=students[marks>70]
print("STUDENTS WHO SCORED ABOVE 70:",high_scorers)
print("MARKS:", marks[marks>70]) #to get their names
#LETS FIND THE STUDENTS WHO NEED IMPROVEMENT (SCORED BELOW 50)
needs_improvement=students[marks<50]
print("STUDENTS WHO NEED IMPROVEMENT:",needs_improvement)
print("MARKS:", marks[marks<50]) #to get their names
#FIND STRONGEST STUDENTS BASED ON STUDY HOURS AND MARKS
condition=(study_hours>5) & (marks>70)
print("STRONGEST STUDENTS:",students[condition])
#CALCULATE STATISTICS
print("AVERAGE: ",np.mean(marks))
print("HIGHEST: ",np.max(marks))
print("LOWEST: ",np.min(marks))
print("STANDARD DEVIATION: ",np.std(marks))
#FIND THE TOP STUDENTS AND THIER NAME AND MARKS
best_index=np.argmax(marks)
print("TOP STUDENT:", students[best_index])
print("MARKS:", marks[best_index])
#RANK STUDENTS
ranking=np.argsort(marks)[::-1] #descending order
print(students[ranking])
print(marks[ranking])
#PASS OR FAIL CLASSIFICATION
results=np.where(marks>50,"PASS", "FAIL")
print("RESULTS:",results)
#ANALYZE THE ATTENDANCE
low_attendance=students[attendance<75]
print("STUDENTS WITH LOW ATTENDANCE:", low_attendance)
print("ATTENDANCE:", attendance[attendance<75])
#FINDING STUDENTS MEETING ALL CRITERIA (STUDY HOURS>5, ATTENDANCE>75, ASSIGNMENT>5, MARKS>70)
criteria=(study_hours>5) & (attendance>75) & (assignment>5) & (marks>70)
print("STUDENTS MEETING ALL CRITERIA:", students[criteria])
print("MARKS:", marks[criteria])
#COLUMN STATISTICS
print("STUDY HOURS - AVERAGE:", np.mean(study_hours))
print("ATTENDANCE - AVERAGE:", np.mean(attendance))
print("ASSIGNMENT - AVERAGE:", np.mean(assignment)) 
print("MARKS - AVERAGE:", np.mean(marks))
print(np.max(data, axis=0)) #max of each column
print(np.min(data, axis=0)) #min of each column
print(np.std(data, axis=0)) #standard deviation of each column
