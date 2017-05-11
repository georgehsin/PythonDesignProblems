class Task:
	def tasksScheduling(self, workingHours, tasks):
	    tasks.sort(reverse=True)
	    if tasks[0]>workingHours:
	        return -1
	    day = 0
	    while len(tasks)>0:
	        results = taskHelper(tasks, workingHours)
	        taskIndices = results[1]
	        taskIndices.sort(reverse=True)
	        for x in taskIndices:
	            del tasks[x]
	        print tasks
	        day += 1
	    return day


	def taskHelper(self, tasks, hours):
	    minIndices = []
	    minRemainder = hours
	    for x in range(0, len(tasks)):
	        indices = [x]
	        remainder = hours - tasks[x]
	        for i in range(x+1, len(tasks)):
	            if remainder == tasks[i]:
	                indices.append(i)
	                return (0, indices)
	            if remainder > tasks[i]:
	                remainder -= tasks[i]
	                indices.append(i)
	        if remainder < minRemainder:
	            minRemainder = remainder
	            minIndices = indices
	    return (minRemainder, minIndices)

tasks = [15,15,14,13,8,8,7,6,5,4,4,3]
hours = 15

newTask = Task()

newTask.taskManager(hours, tasks)



# As a new engineer at Asana, you're working on a feature that helps users estimate how long it will take them to complete their workload. All a user has to do is specify the number of hours they work every day, provide the time allocated for each task, and the feature automatically calculates the number of days it will take for the user to finish all of their tasks. Since you think it's a bad habit to leave a given task unfinished at the end of a day, tasks should be distributed so that each one will be completed during the working hours of a single day.

# Given the time allocated to a user's tasks and their daily workingHours, return the minimum number of days necessary for them to complete the given tasks. If there's no way to tackle all of them, return -1 instead.

# Example

# For workingHours = 2 and tasks = [1, 2, 1], the output should be
# tasksScheduling(workingHours, tasks) = 2.

# The first and the third tasks can be completed during the first day, and the second task can be completed during the second day.

# For workingHours = 3 and tasks = [2, 2, 2], the output should be
# tasksScheduling(workingHours, tasks) = 3.

# Completing any two tasks in a day requires 4 hours which is more than workingHours, so it is impossible to complete more than one task during a single day, meaning that the total number of days needed to complete all the tasks is 3.

# For workingHours = 2 and tasks = [1, 1, 3], the output should be
# tasksScheduling(workingHours, tasks) = -1.

# It is impossible to complete the third task during a single day.

# Input/Output

# [time limit] 4000ms (py)
# [input] integer workingHours

# A positive integer representing the number of hours a user works in a day.

# Guaranteed constraints:
# 1 ≤ workingHours ≤ 15.

# [input] array.integer tasks

# An array of positive integers. tasks[i] equals the time it will take to finish the ith task.

# Guaranteed constraints:
# 1 ≤ tasks.length ≤ 12,
# 1 ≤ tasks[i] ≤ 15.

# [output] integer

# The minimum number of days required to complete all the tasks, or -1 if it is impossible to finish all of them.

                
