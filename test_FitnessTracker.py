from FitnessTracker import GetWorkout
import pytest

a = GetWorkout('Jong', 70, 175, 20, 'M', 'aengida@gmail.com')

def test_user_info():
    b = a.user_info('Jong', 70, 175, 20, 'M', 'aengida@gmail.com')
    c = {}
    g = {}
    g['age'] = 20
    g['email'] = 'aengida@gmail.com'
    g['gender'] = 'M'
    g['height'] = 70
    g['weight'] = 175
    c['Jong'] = g
    assert b == c

def test_bmi_calculator():

    assert a.bmi_calculator(70, 175) == 25.107142857142858
    assert a.bmi_calculator(68, 143) == 21.74070069204152
    assert a.bmi_calculator(60, 125) == 24.40972222222222
    assert a.bmi_calculator(74, 225) == 28.885135135135137
    assert a.bmi_calculator(72, 180) == 24.40972222222222
    
def test_calories_calculator():
    
    assert a.calories_calculator(70,175,20,'M') == f'You are overweight. In order to lose 1 to 2 lbs per week, you need to reduce your daily calorie intake by 20%, from 1935 calories to 1548 calories.'
    assert a.calories_calculator(68,143,18,'M') == 'Congrats! You are healthy. In order to maintain this weightyou need to consume 1721 calories daily.'
    assert a.calories_calculator(60,125,29,'M') == 'Congrats! You are healthy. In order to maintain this weightyou need to consume 1430 calories daily.'
    assert a.calories_calculator(74,225,45,'F') == 'You are overweight. In order to lose 1 to 2 lbs per week, you need to reduce your daily calorie intake by 20%, from 1758 calories to 1407 calories.'
    assert a.calories_calculator(72,180,59,'F') == 'Congrats! You are healthy. In order to maintain this weightyou need to consume 1490 calories daily.'
    
def test_workoutplan():
    assert a.workoutplan('workoutplan.csv') == ('\n'.join(a.workoutplan_list))
    