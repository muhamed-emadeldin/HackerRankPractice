import math

def gradingStudents(grades):
  #-->defense function
  assert(isinstance(grades, list)), "Grades should be list"

  for i in range(len(grades)):

    #-->basic variables
    score     = grades[i]
    get_multi = math.ceil(score / 5) * 5
    get_diff  = get_multi - score

    
    #-->basic condation
    if score >= 38:
      if get_diff < 3:
        score += get_diff
        
      grades[i] = score

  return grades

print(gradingStudents([73, 67, 38, 33]))
