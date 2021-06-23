import plotly.figure_factory as pff
import pandas as pd
import plotly.graph_objects as pgo
import statistics

df = pd.read_csv("StudentsPerformance.csv")
scoreData = df["reading score"].tolist()

mean = sum(scoreData) / len(scoreData) # or statistics.mean(scoreData)
median = statistics.median(scoreData)
mode = statistics.mode(scoreData)

standardDeviation = statistics.stdev(scoreData)

first_sds = mean - standardDeviation
first_sdse = mean + standardDeviation

second_sds = mean - (2 * standardDeviation)
second_sdse = mean + (2 * standardDeviation)

third_sds = mean - (3 * standardDeviation)
third_sdse = mean + (3 * standardDeviation)

fig = pff.create_distplot([scoreData], ["reading scores"], show_hist=False)

fig.add_trace(pgo.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))

fig.add_trace(pgo.Scatter(x=[first_sds, first_sds], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(pgo.Scatter(x=[first_sdse, first_sdse], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))

fig.add_trace(pgo.Scatter(x=[second_sds, second_sds], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(pgo.Scatter(x=[second_sdse, second_sdse], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))

fig.add_trace(pgo.Scatter(x=[third_sds, third_sds], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3"))
fig.add_trace(pgo.Scatter(x=[third_sdse, third_sdse], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3"))

fig.show()

dataInFirstStandardDeviationRange = [result for result in scoreData if result > first_sds and result < first_sdse]
dataInSecondStandardDeviationRange = [result for result in scoreData if result > second_sds and result < second_sdse]
dataInThirdStandardDeviationRange = [result for result in scoreData if result > third_sds and result < third_sdse]

print("Mean of the data is {}".format(mean))
print("Median of the data is {}".format(median))
print("Mode of the data is {}".format(mode))
print("\nStandard Deviation of the data is {}".format(standardDeviation))

print("\n{}% of data lies in First Standard Deviation Range".format(len(dataInFirstStandardDeviationRange) * 100.0 / len(scoreData)))
print("{}% of data lies in Second Standard Deviation Range".format(len(dataInSecondStandardDeviationRange) * 100.0 / len(scoreData)))
print("{}% of data lies in Third Standard Deviation Range".format(len(dataInThirdStandardDeviationRange) * 100.0 / len(scoreData)))