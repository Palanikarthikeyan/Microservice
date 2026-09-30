from flask import Flask, request, jsonify
from prometheus_client import (
    Counter,
    Histogram,
    generate_latest,
    CONTENT_TYPE_LATEST
)
import time


app = Flask(__name__)


# ---------------------------------------------------
# Prometheus Metrics
# ---------------------------------------------------

# Total number of HTTP requests
http_requests_total = Counter(
    "order_service_http_requests_total",
    "Total number of HTTP requests",
    ["method", "endpoint", "status"]
)


# Request processing time
http_request_duration_seconds = Histogram(
    "order_service_http_request_duration_seconds",
    "HTTP request processing time",
    ["method", "endpoint"]
)


# Total orders created
orders_created_total = Counter(
    "orders_created_total",
    "Total number of orders created"
)


# Total application errors
application_errors_total = Counter(
    "order_service_errors_total",
    "Total number of application errors"
)


# ---------------------------------------------------
# Simple in-memory database
# ---------------------------------------------------

orders = {}

order_id_counter = 1


# ---------------------------------------------------
# Create Order
# ---------------------------------------------------

@app.route("/orders", methods=["POST"])
def create_order():

    global order_id_counter

    start_time = time.time()

    try:

        data = request.get_json()

        if not data:
            application_errors_total.inc()

            response = jsonify({
                "error": "Request body is required"
            })

            status = 400

            return response, status

        customer = data.get("customer")
        amount = data.get("amount")

        if not customer or amount is None:

            application_errors_total.inc()

            response = jsonify({
                "error": "customer and amount are required"
            })

            status = 400

            return response, status

        order = {
            "order_id": order_id_counter,
            "customer": customer,
            "amount": amount
        }

        orders[order_id_counter] = order

        order_id_counter += 1

        orders_created_total.inc()

        response = jsonify(order)

        status = 201

        return response, status

    finally:

        duration = time.time() - start_time

        http_request_duration_seconds.labels(
            method="POST",
            endpoint="/orders"
        ).observe(duration)

        http_requests_total.labels(
            method="POST",
            endpoint="/orders",
            status=status if "status" in locals() else 500
        ).inc()


# ---------------------------------------------------
# Get Order
# ---------------------------------------------------

@app.route("/orders/<int:order_id>", methods=["GET"])
def get_order(order_id):

    start_time = time.time()

    try:

        if order_id not in orders:

            application_errors_total.inc()

            response = jsonify({
                "error": "Order not found"
            })

            status = 404

            return response, status

        response = jsonify(orders[order_id])

        status = 200

        return response, status

    finally:

        duration = time.time() - start_time

        http_request_duration_seconds.labels(
            method="GET",
            endpoint="/orders/<id>"
        ).observe(duration)

        http_requests_total.labels(
            method="GET",
            endpoint="/orders/<id>",
            status=status if "status" in locals() else 500
        ).inc()


# ---------------------------------------------------
# Health Check
# ---------------------------------------------------

@app.route("/health", methods=["GET"])
def health():

    return jsonify({
        "status": "UP",
        "service": "order-service"
    })


# ---------------------------------------------------
# Prometheus Metrics Endpoint
# ---------------------------------------------------

@app.route("/metrics")
def metrics():

    return generate_latest(), 200, {
        "Content-Type": CONTENT_TYPE_LATEST
    }


# ---------------------------------------------------
# Start application
# ---------------------------------------------------

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5001,
        debug=True
    )

