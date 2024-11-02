from flask import Flask, request, jsonify
import matplotlib.pyplot as plt
import pandas as pd

app = Flask(__name__)

@app.route('/visualize', methods=['GET'])
def visualize_data():
    # Your data processing and visualization code here
    df = pd.read_csv("global_terrorism_data.csv")
    region_counts = df['region'].value_counts()

    # Generate and save the visualization
    plt.figure(figsize=(10, 6))
    region_counts.plot(kind='bar')
    plt.title('Incidents by Region')
    plt.xlabel('Region')
    plt.ylabel('Number of Incidents')
    plt.savefig("incidents_by_region.png")

    # Return the path to the saved image
    return jsonify({"image_url": "/path/to/incidents_by_region.png"})

if __name__ == '__main__':
    app.run(debug=True)
