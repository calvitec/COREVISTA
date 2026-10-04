from flask import Flask, render_template, request

app = Flask(__name__)
app.config["SECRET_KEY"] = "corevista-software-secret-2026"

COMPANY_INFO = {
    "legal_name": "COREVISTA SOFTWARE LLC",
    "entity_number": "0451505802",
    "registered": "New Jersey, USA (08/03/2026)",
    "registered_agent": "Michael Lanza",
    "registered_office": "40 Wantage Ave, Branchville, New Jersey 07890",
    "email": "corevistasoftwares@gmail.com",
    "phone": "+1 (850) 228-5378",
    "business_purpose": (
        "To develop, license, market, and support software applications, "
        "digital platforms, and technology solutions for businesses and consumers."
    ),
}

SERVICES = [
    {
        "id": "software-platform-development",
        "name": "Software & Platform Development",
        "icon": "fa-code",
        "description": (
            "Building scalable consumer applications and robust enterprise "
            "digital platforms."
        ),
        "image": (
            "https://images.unsplash.com/photo-1498050108023-c5249f4df085"
            "?auto=format&fit=crop&w=1200&q=85"
        ),
        "features": [
            "Consumer applications",
            "Enterprise platforms",
            "Scalable architecture",
            "Product engineering",
        ],
    },
    {
        "id": "ai-training-engineering",
        "name": "AI Training & Engineering",
        "icon": "fa-brain",
        "description": (
            "Partnering with AI pioneers to deliver specialized software "
            "engineering workflows for machine learning model training."
        ),
        "image": (
            "https://images.unsplash.com/photo-1677442136019-21780ecad995"
            "?auto=format&fit=crop&w=1200&q=85"
        ),
        "features": [
            "Model-training workflows",
            "Data quality engineering",
            "Evaluation pipelines",
            "AI model optimization",
        ],
    },
    {
        "id": "technology-solutions",
        "name": "Technology Solutions",
        "icon": "fa-microchip",
        "description": (
            "Licensing and supporting market-ready products designed for "
            "high performance and seamless integration."
        ),
        "image": (
            "https://images.unsplash.com/photo-1518770660439-4636190af475"
            "?auto=format&fit=crop&w=1200&q=85"
        ),
        "features": [
            "Product licensing",
            "System integration",
            "Technical support",
            "Performance optimization",
        ],
    },
]

PROCESS_STEPS = [
    {
        "number": "01",
        "title": "Discovery & Strategy",
        "description": (
            "We align on your goals, users, technical constraints, and the "
            "outcomes that define success."
        ),
        "icon": "fa-compass",
    },
    {
        "number": "02",
        "title": "Architecture & Design",
        "description": (
            "We shape a secure, scalable technical foundation and an "
            "experience built around real needs."
        ),
        "icon": "fa-diagram-project",
    },
    {
        "number": "03",
        "title": "Development & AI Training",
        "description": (
            "Our engineers build, test, and refine software and AI "
            "engineering workflows with care."
        ),
        "icon": "fa-code-branch",
    },
    {
        "number": "04",
        "title": "Deployment & Support",
        "description": (
            "We support launch, integration, and continuous improvement "
            "as your products grow."
        ),
        "icon": "fa-cloud-arrow-up",
    },
]

WHY_CHOOSE_US = [
    {
        "title": "Enterprise-grade engineering",
        "description": (
            "Thoughtful architecture, disciplined delivery, and dependable "
            "software built to scale."
        ),
        "icon": "fa-shield-halved",
    },
    {
        "title": "AI-first approach",
        "description": (
            "Practical AI engineering expertise that supports model training, "
            "evaluation, and optimization."
        ),
        "icon": "fa-brain",
    },
    {
        "title": "NJ-licensed & compliant",
        "description": (
            "A New Jersey registered limited liability company committed to "
            "clear, accountable business practices."
        ),
        "icon": "fa-circle-check",
    },
    {
        "title": "Strategic partnerships with AI leaders",
        "description": (
            "A specialized engineering partner for organizations advancing "
            "the next generation of AI."
        ),
        "icon": "fa-handshake",
    },
]

ABOUT = (
    "At the intersection of modern innovation and technical precision, "
    "COREVISTA SOFTWARE LLC specializes in developing, licensing, marketing, "
    "and supporting advanced software applications, digital platforms, and "
    "tailored technology solutions for both businesses and consumers.\n\n"
    "Beyond our proprietary product ecosystem, we serve as a specialized "
    "strategic partner for leading artificial intelligence firms. By "
    "subcontracting high-end software engineering work, we power the "
    "foundational training and optimization of next-generation AI models. "
    "We bridge the gap between human engineering excellence and scalable "
    "digital infrastructure to shape the future of technology."
)


@app.route("/")
def index():
    return render_template(
        "corevista.html",
        company=COMPANY_INFO,
        about=ABOUT,
        services=SERVICES,
        process_steps=PROCESS_STEPS,
        reasons=WHY_CHOOSE_US,
    )


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        phone = request.form.get("phone", "").strip()
        message = request.form.get("message", "").strip()

        if not name or not email or not message:
            return render_template(
                "contact.html",
                company=COMPANY_INFO,
                success=False,
                error="Please provide your name, email, and message.",
                form_data={
                    "name": name,
                    "email": email,
                    "phone": phone,
                    "message": message,
                },
            ), 400

        return render_template(
            "contact.html",
            company=COMPANY_INFO,
            success=True,
            name=name,
            message=(
                "Thank you for contacting COREVISTA SOFTWARE LLC. "
                "We will be in touch soon."
            ),
        )

    return render_template(
        "contact.html",
        company=COMPANY_INFO,
        success=False,
        form_data={},
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
