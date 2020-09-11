"""
------------------------------------------------------------------------
Lab 3  Question 13
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-09-25"
------------------------------------------------------------------------
"""
MID_TERM_WORTH=0.35
EXAM_WORTH=0.65

midmark=float(input('Midterm mark (%): '))

exammark=float(input('Exam mark (%): '))

final_grade=(MID_TERM_WORTH*midmark)+ (EXAM_WORTH*exammark)  

print('Final Grade (%): {:.1f}'.format(final_grade))

