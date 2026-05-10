from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder=".")

# Categories available on the platform
CATEGORIES = [
    {"id": "real-estate", "name": "Real Estate & Land", "icon": "🏠", "desc": "Properties, plots & land across Zambia"},
    {"id": "graphics", "name": "Graphics & Design", "icon": "🎨", "desc": "Branding, logos & creative design"},
    {"id": "printing", "name": "Printing Services", "icon": "🖨️", "desc": "Flyers, banners & quality print"},
    {"id": "motors", "name": "Motor Vehicles", "icon": "🚗", "desc": "Cars, trucks & motorcycles"},
    {"id": "courier", "name": "Courier Services", "icon": "📦", "desc": "Deliveries nationwide & cross-border"},
    {"id": "loans", "name": "Loans & Finance", "icon": "💰", "desc": "Personal, business & micro-finance loans"},
]

# Sample listings data
LISTINGS = {
    "real-estate": [
        {"title": "3-Bedroom House – Kabulonga", "price": "K850,000", "location": "Lusaka", "tag": "For Sale", "image": "Commercial_Real_Estate.jpg"},
        {"title": "Prime Plot – Lilayi", "price": "K120,000", "location": "Lusaka", "tag": "Plot", "image": "plot.jpg"},
        {"title": "Commercial Land – Ndola CBD", "price": "K1,000,000", "location": "Ndola", "tag": "Commercial", "image": "Plots.jpg"},
        {"title": "2-Bedroom Flat – Woodlands", "price": "K2,500/mo", "location": "Lusaka", "tag": "For Rent", "image": "Real_Estate_Investing.jpg"},
    ],
    "graphics": [
        {"title": "Logo Design Package", "price": "K500", "location": "Lusaka", "tag": "Branding", "image": "Graphics.jpg"},
        {"title": "Social Media Creatives", "price": "K200/mo", "location": "Online", "tag": "Digital", "image": "Designer.jpg"},
        {"title": "Business Card Design", "price": "K150", "location": "Kitwe", "tag": "Print Ready", "image": "Graphics.jpg"},
        {"title": "Billboard Design", "price": "K1,200", "location": "Lusaka", "tag": "Outdoor", "image": "Designer.jpg"},
    ],
    "printing": [
        {"title": "A3 Flyers – 500 copies", "price": "K350", "location": "Lusaka", "tag": "Flyers"},
        {"title": "Pull-Up Banner 2m", "price": "K280", "location": "Ndola", "tag": "Banners"},
        {"title": "Branded T-Shirts x50", "price": "K1,800", "location": "Lusaka", "tag": "Apparel"},
        {"title": "Wedding Invitation Cards", "price": "K400", "location": "Livingstone", "tag": "Events"},
    ],
    "motors": [
        {"title": "Toyota Hilux 2019 – Double Cab", "price": "K198,000", "location": "Lusaka", "tag": "Pickup"},
        {"title": "Honda Fit 2016 – Hybrid", "price": "K85,000", "location": "Kitwe", "tag": "Sedan"},
        {"title": "Yamaha FZ 150cc", "price": "K18,500", "location": "Lusaka", "tag": "Motorcycle"},
        {"title": "Toyota Land Cruiser V8", "price": "K450,000", "location": "Lusaka", "tag": "SUV"},
    ],
    "courier": [
        {"title": "Same-Day Delivery – Lusaka City", "price": "K80", "location": "Lusaka", "tag": "Express", "image": "courier_services.jpg"},
        {"title": "Lusaka–Livingstone Cargo", "price": "K350/trip", "location": "Nationwide", "tag": "Cargo", "image": "courierServices.jpg"},
        {"title": "Cross-Border – Zambia/Zimbabwe", "price": "K1,200", "location": "Cross-Border", "tag": "International", "image": "courier_services.jpg"},
        {"title": "Parcel Pickup & Drop", "price": "K100", "location": "Lusaka", "tag": "Parcels", "image": "courierServices.jpg"},
    ],
    "loans": [
        {"title": "Personal Loan up to K50,000", "price": "From 5%", "location": "All Branches", "tag": "Personal"},
        {"title": "SME Business Loan", "price": "From 8%", "location": "Lusaka", "tag": "Business"},
        {"title": "Micro-Finance – K500 to K5,000", "price": "Flexible", "location": "Nationwide", "tag": "Micro"},
        {"title": "Home Purchase Loan", "price": "From 12%", "location": "All Provinces", "tag": "Mortgage"},
    ],
}

@app.route("/")
def index():
    return render_template("index.html", categories=CATEGORIES)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/dashboard")
def dashboard():
    active = request.args.get("category", "real-estate")
    listings = LISTINGS.get(active, [])
    return render_template("dashboard.html", categories=CATEGORIES, active=active, listings=listings)

@app.route("/category/<cat_id>")
def category(cat_id):
    return redirect(url_for("dashboard", category=cat_id))

if __name__ == "__main__":
    app.run(debug=True)
