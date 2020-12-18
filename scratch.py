import smtplib, ssl
from argparse import ArgumentParser
import requests, re, pandas as pd, time, webbrowser, sys

workoutplan_list = []
with open(filename) as work_out:
    workout_file = csv.reader(work_out, delimiter = ',')
    for row in workout_file:
        Day = row[:]
        workoutplan_list.append(day)
    if exercise not in user_hist_list:
        workoutplan_list.append(exercise)
    return workoutplan_list