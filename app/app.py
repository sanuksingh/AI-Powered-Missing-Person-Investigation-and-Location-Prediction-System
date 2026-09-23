from flask import Flask, render_template, request
import joblib
import pandas as pd
import os
import math

app = Flask(__name__)


# MODEL PATH


MODEL_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "data",
    "final_model",
    "gps_location_prediction_deployment_model.pkl"
)

print("Loading trained model...")
print("Model path:", MODEL_PATH)

model = joblib.load(MODEL_PATH)

print("Model loaded successfully!")



# DISTANCE FUNCTION
# Haversine distance

def calculate_distance_km(lat1, lon1, lat2, lon2):

    R = 6371.0

    lat1_rad = math.radians(lat1)
    lat2_rad = math.radians(lat2)

    delta_lat = math.radians(lat2 - lat1)
    delta_lon = math.radians(lon2 - lon1)

    a = (
        math.sin(delta_lat / 2) ** 2
        + math.cos(lat1_rad)
        * math.cos(lat2_rad)
        * math.sin(delta_lon / 2) ** 2
    )

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c



# HOME PAGE


@app.route("/")
def home():

    return render_template("index.html")


# ABOUT PAGE



@app.route("/about")
def about():
    return render_template("about.html")




# PREDICTION


@app.route("/predict", methods=["POST"])
def predict():

    try:

        
        # Get values from form
        

        latitude = float(request.form["latitude"])
        longitude = float(request.form["longitude"])

        previous_latitude = float(
            request.form["previous_latitude"]
        )

        previous_longitude = float(
            request.form["previous_longitude"]
        )

        altitude = float(
            request.form["altitude"]
        )

        clean_speed_kmh = float(
            request.form["clean_speed_kmh"]
        )

        distance_m = float(
            request.form["distance_m"]
        )

        time_diff_sec = float(
            request.form["time_diff_sec"]
        )

        hour = int(
            request.form["hour"]
        )

        is_weekend = int(
            request.form["is_weekend"]
        )


        
        # Create input dataframe
        

        input_data = pd.DataFrame([{

            "latitude": latitude,

            "longitude": longitude,

            "previous_latitude":
                previous_latitude,

            "previous_longitude":
                previous_longitude,

            "altitude":
                altitude,

            "clean_speed_kmh":
                clean_speed_kmh,

            "distance_m":
                distance_m,

            "time_diff_sec":
                time_diff_sec,

            "hour":
                hour,

            "is_weekend":
                is_weekend

        }])


        
        # Predict
        

        prediction = model.predict(input_data)[0]

        predicted_latitude = float(
            prediction[0]
        )

        predicted_longitude = float(
            prediction[1]
        )


        
        # Calculate distance
        

        prediction_distance_km = calculate_distance_km(
            latitude,
            longitude,
            predicted_latitude,
            predicted_longitude
        )


        prediction_distance_m = prediction_distance_km * 1000


        
        # Display result
        

        return render_template(

            "index.html",

            prediction=True,

            # Current location
            current_latitude=round(latitude, 6),
            current_longitude=round(longitude, 6),

            # Previous location
            previous_latitude=round(
                previous_latitude, 6
            ),
            previous_longitude=round(
                previous_longitude, 6
            ),

            # Other form values
            altitude=altitude,
            clean_speed_kmh=clean_speed_kmh,
            distance_m=distance_m,
            time_diff_sec=time_diff_sec,
            hour=hour,
            is_weekend=is_weekend,

            # Prediction
            predicted_latitude=round(
                predicted_latitude, 6
            ),

            predicted_longitude=round(
                predicted_longitude, 6
            ),

            # Distance
            prediction_distance_km=round(
                prediction_distance_km, 3
            ),

            prediction_distance_m=round(
                prediction_distance_m, 2
            )
        )


    except Exception as e:

        return render_template(
            "index.html",
            error=str(e)
        )



# RUN APPLICATION

if __name__ == "__main__":

    print("=" * 60)
    print("GPS NEXT-LOCATION PREDICTION SYSTEM")
    print("=" * 60)

    print("Starting Flask server....")

    app.run(
    host="127.0.0.1",
    port=5000,
    debug=False,
    use_reloader=False
)


    