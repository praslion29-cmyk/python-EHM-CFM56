# ==============================
# Aircraft Engine Health Monitoring Dashboard Generator
# ==============================

# Engine limits CFM56-7B (typical)
EGT_LIMIT = 920          # °C
N1_LIMIT = 102            # %
N2_LIMIT = 101            # %
OIL_PRESS_LOW = 30        # psi
OIL_PRESS_HIGH = 60       # psi
OIL_TEMP_LIMIT = 165      # °C
VIB_LIMIT = 3.5           # unit
FUEL_FLOW_LIMIT = 6000    # kg/h (max per engine)

# Sample input data (bisa diubah langsung di sini)
aircraft = "B737-800"
egt = 650
n1 = 97
n2 = 98
oil_pressure = 45
oil_temp = 140
vibration = 1.5
fuel_flow = 4500

# ==============================
# Function to determine status
# ==============================
def status(value, low_limit, high_limit=None):
    """Return status text with color class and emoji"""
    if high_limit is None:
        # Only upper limit
        if value > low_limit*0.9 and value <= low_limit:
            return "Approaching Limit 🟡", "approaching"
        elif value > low_limit:
            return "Warning 🔴", "warning"
        else:
            return "Normal 🟢", "normal"
    else:
        # Both lower & upper limit
        if value < low_limit or value > high_limit:
            return "Warning 🔴", "warning"
        elif (low_limit <= value <= low_limit*1.1) or (value >= high_limit*0.9):
            return "Approaching Limit 🟡", "approaching"
        else:
            return "Normal 🟢", "normal"

# ==============================
# Generate HTML content
# ==============================
html_content = f"""
<html>
<head>
<title>Aircraft Engine Monitoring</title>
<style>
body {{
    font-family: Arial, sans-serif;
    margin: 30px;
    background-color: #f4f4f4;
}}
h1 {{
    color: #003366;
}}
p {{
    font-size: 18px;
}}
.status-normal {{ color: green; }}
.status-approaching {{ color: orange; }}
.status-warning {{ color: red; }}
.box {{
    background-color: white;
    padding: 20px;
    border-radius: 10px;
    margin-bottom: 10px;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
}}
</style>
</head>
<body>
<h1>Aircraft Engine Health Monitoring</h1>

<div class="box">
<p>Aircraft : {aircraft}</p>

<p>EGT : {egt} °C - <span class="status-{status(egt, EGT_LIMIT)[1]}">{status(egt, EGT_LIMIT)[0]}</span></p>
<p>N1 : {n1} % - <span class="status-{status(n1, N1_LIMIT)[1]}">{status(n1, N1_LIMIT)[0]}</span></p>
<p>N2 : {n2} % - <span class="status-{status(n2, N2_LIMIT)[1]}">{status(n2, N2_LIMIT)[0]}</span></p>
<p>Oil Pressure : {oil_pressure} PSI - <span class="status-{status(oil_pressure, OIL_PRESS_LOW, OIL_PRESS_HIGH)[1]}">{status(oil_pressure, OIL_PRESS_LOW, OIL_PRESS_HIGH)[0]}</span></p>
<p>Oil Temperature : {oil_temp} °C - <span class="status-{status(oil_temp, OIL_TEMP_LIMIT)[1]}">{status(oil_temp, OIL_TEMP_LIMIT)[0]}</span></p>
<p>Vibration : {vibration} - <span class="status-{status(vibration, VIB_LIMIT)[1]}">{status(vibration, VIB_LIMIT)[0]}</span></p>
<p>Fuel Flow : {fuel_flow} kg/h - <span class="status-{status(fuel_flow, FUEL_FLOW_LIMIT)[1]}">{status(fuel_flow, FUEL_FLOW_LIMIT)[0]}</span></p>
</div>

</body>
</html>
"""

# ==============================
# Save file with UTF-8
# ==============================
with open("dashboard.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("HTML dashboard berhasil dibuat! Buka file 'dashboard.html' di browser.")