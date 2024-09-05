import plotly.express as px
import pandas as pd

df = pd.DataFrame([
    dict(Task="Coating", Start='2024-09-04', Finish='2024-09-05', Completion_pct=0),
    dict(Task="Seeding", Start='2024-09-05', Finish='2024-09-06', Completion_pct=10),
    dict(Task="Proliferation", Start='2024-09-06', Finish='2024-09-08', Completion_pct=50),
    dict(Task="Differentiation", Start='2024-09-08', Finish='2024-09-15', Completion_pct=60),
    dict(Task="Change media _ differentiation", Start='2024-09-08', Finish='2024-09-10', Completion_pct=60),
    dict(Task="Change media _ differentiation", Start='2024-09-10', Finish='2024-09-12', Completion_pct=65),
    dict(Task="Change media _ differentiation", Start='2024-09-12', Finish='2024-09-14', Completion_pct=70),
    dict(Task="Change media _ differentiation", Start='2024-09-14', Finish='2024-09-15', Completion_pct=75),
    dict(Task="PC12 seeding", Start='2024-09-12', Finish='2024-09-15', Completion_pct=65),
    dict(Task="Coculture", Start='2024-09-15', Finish='2024-09-20', Completion_pct=80),
    dict(Task="Change media _ co-culture", Start='2024-09-15', Finish='2024-09-17', Completion_pct=80),
    dict(Task="Change media _ co-culture", Start='2024-09-17', Finish='2024-09-19', Completion_pct=90),
    dict(Task="Change media _ co-culture", Start='2024-09-19', Finish='2024-09-20', Completion_pct=100),
])

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task",color="Completion_pct")
fig.update_yaxes(autorange="reversed") # otherwise tasks are listed from the bottom up
fig.show()