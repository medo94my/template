from quickchart import QuickChart

qc = QuickChart()
qc.width = 500
qc.height = 300
qc.version = '2'

# Config can be set as a string or as a nested dict
qc.config = """{
  type: 'bar',
  data: {
    labels: ['Q1', 'Q2', 'Q3', 'Q4'],
    datasets: [{
      label: 'Users',
      data: [50, 60, 70, 180],
      backgroundColor:"yellow"
      width:30
    }, {
      label: 'Revenue',
      data: [100, 200, 300, 400]
    }]
  }
}"""

# You can get the chart URL...
print(qc.get_url())

# Get the image as a variable...
image = qc.get_short_url()
print(image)
# Or write the chart to a file
qc.to_file('mychart.png')