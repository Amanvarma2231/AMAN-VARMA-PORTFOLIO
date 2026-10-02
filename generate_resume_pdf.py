import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_RIGHT

def build_pdf():
    output_dir = os.path.join(os.path.dirname(__file__), "frontend", "assets")
    os.makedirs(output_dir, exist_ok=True)
    pdf_path = os.path.join(output_dir, "Aman_Varma_Resume.pdf")

    # Margins: 0.5 inch (36 points) for clean single page fit
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=32,
        bottomMargin=32
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'NameTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=26,
        textColor=colors.HexColor("#000000")
    )

    links_style = ParagraphStyle(
        'HeaderLinks',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor("#1d4ed8")
    )

    contact_style = ParagraphStyle(
        'ContactInfo',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        alignment=TA_RIGHT,
        textColor=colors.HexColor("#000000")
    )

    section_heading = ParagraphStyle(
        'SectionHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=colors.HexColor("#1d4ed8"),
        spaceBefore=8,
        spaceAfter=3
    )

    body_bold = ParagraphStyle(
        'BodyBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor("#000000")
    )

    body_text = ParagraphStyle(
        'BodyTextCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12.5,
        textColor=colors.HexColor("#1e293b")
    )

    story = []

    # 1. HEADER
    header_left = (
        "<b><font size=24 color='#000000'>Aman Varma</font></b><br/>"
        "<font color='#1d4ed8'><u><a href='http://127.0.0.1:8000' color='#1d4ed8'>Portfolio</a></u> | "
        "<u><a href='https://www.linkedin.com/in/aman-v-697771345' color='#1d4ed8'>LinkedIn</a></u> | "
        "<u><a href='https://github.com/Amanvarma2231' color='#1d4ed8'>GitHub</a></u></font>"
    )
    header_right = (
        "Ghaziabad, India<br/>"
        "Mobile: +91-6306572504<br/>"
        "Email: <a href='mailto:amangurauli@gmail.com' color='#1d4ed8'><u>amangurauli@gmail.com</u></a>"
    )

    header_table = Table([[Paragraph(header_left, styles['Normal']), Paragraph(header_right, contact_style)]], colWidths=[320, 220])
    header_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('ALIGN', (1,0), (1,0), 'RIGHT')
    ]))
    story.append(header_table)
    story.append(Spacer(1, 6))

    def add_section_header(title_text):
        story.append(Paragraph(title_text, section_heading))
        story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#1d4ed8"), spaceBefore=1, spaceAfter=5))

    # 2. PROFESSIONAL SUMMARY
    add_section_header("PROFESSIONAL SUMMARY")
    summary_txt = (
        "B.Tech Computer Science Engineering graduate with 7+ months of hands-on internship experience in Python Backend "
        "Development, RESTful APIs, FastAPI, Flask, database-driven applications, API integration, testing, and debugging. Experience "
        "in developing backend services and automated workflows using SQL/NoSQL databases, Git, and Docker, with additional "
        "experience in NLP, Generative AI, LLM concepts, and Prompt Engineering for AI-powered applications."
    )
    story.append(Paragraph(summary_txt, body_text))

    # 3. TECHNICAL SKILLS
    add_section_header("TECHNICAL SKILLS")
    skills_data = [
        [Paragraph("<b>Languages</b>", body_text), Paragraph(":", body_text), Paragraph("Python, Java, JavaScript, C++, SQL, HTML5", body_text)],
        [Paragraph("<b>AI ML</b>", body_text), Paragraph(":", body_text), Paragraph("Artificial Intelligence, Machine Learning, NLP, Generative AI, Prompt Engineering, LLMs", body_text)],
        [Paragraph("<b>DSA</b>", body_text), Paragraph(":", body_text), Paragraph("Data Structures Algorithms, Problem Solving, Algorithm Design", body_text)],
        [Paragraph("<b>Backend</b>", body_text), Paragraph(":", body_text), Paragraph("FastAPI, Flask, Django, RESTful APIs, Web Services", body_text)],
        [Paragraph("<b>API & Integration</b>", body_text), Paragraph(":", body_text), Paragraph("REST API Design, API Specifications, OpenAPI, API Integration, JWT, HTTP", body_text)],
        [Paragraph("<b>Databases</b>", body_text), Paragraph(":", body_text), Paragraph("MySQL, MongoDB, CRUD Operations", body_text)],
        [Paragraph("<b>DevOps & Tools</b>", body_text), Paragraph(":", body_text), Paragraph("Manual Testing, Data Validation, Debugging, Git, GitHub, Docker, CI/CD", body_text)]
    ]
    t_skills = Table(skills_data, colWidths=[125, 12, 403])
    t_skills.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0)
    ]))
    story.append(t_skills)

    # 4. EDUCATION
    add_section_header("EDUCATION")
    edu_table = Table([[
        Paragraph("<b>NITRA Technical Campus, AKTU</b><br/><i>B.Tech, Computer Science & Engineering</i> <b>CGPA: 7.12/10</b>", body_text),
        Paragraph("Ghaziabad UP, India<br/>May 2022 – June 2026", ParagraphStyle('R1', parent=body_text, alignment=TA_RIGHT))
    ]], colWidths=[360, 180])
    edu_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0)
    ]))
    story.append(edu_table)

    # 5. EXPERIENCE
    add_section_header("EXPERIENCE")
    exp_table = Table([[
        Paragraph("<b>Python Developer Intern</b><br/><i>Druidot Consulting (OPC) Pvt. Ltd.</i>", body_text),
        Paragraph("Feb 2026 – Present<br/><i>Remote</i>", ParagraphStyle('R2', parent=body_text, alignment=TA_RIGHT))
    ]], colWidths=[360, 180])
    exp_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0)
    ]))
    story.append(exp_table)
    story.append(Spacer(1, 2))

    exp_bullets = [
        "Developed Python-based AI and backend applications using Flask and FastAPI, integrating RESTful APIs and data-processing workflows..",
        "Worked on NLP-based text processing and analysis for AI-oriented application workflows.",
        "Integrated Generative AI and LLM-based capabilities through AI API integrations and prompt-driven workflows.",
        "Built and optimized REST APIs, backend services, automation, testing, and debugging using .",
        "Performed data validation and processing with MySQL and MongoDB, supporting reliable AI and backend workflows."
    ]
    for b in exp_bullets:
        story.append(Paragraph(f"• {b}", body_text))
        story.append(Spacer(1, 1.5))

    # 6. PROJECTS
    add_section_header("PROJECTS")

    # Project 1: NLPCRM
    p1_left = "<b>NLPCRM – AI-Powered CRM Platform</b> &nbsp;&nbsp; <i>Python, FastAPI, Flask, MySQL, SQLite, REST APIs</i>"
    p1_right = "<u><a href='https://github.com/Amanvarma2231/NLPCRM' color='#000000'>GitHub</a></u>"
    p1_table = Table([[Paragraph(p1_left, body_text), Paragraph(p1_right, ParagraphStyle('R3', parent=body_text, alignment=TA_RIGHT))]], colWidths=[460, 80])
    p1_table.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
    story.append(p1_table)
    story.append(Paragraph("• Designed and developed <b>25+ RESTful API endpoints</b> across contacts, NLP, email, and webhook modules, implementing API specifications, CRUD operations, input validation, and modular backend workflows.", body_text))
    story.append(Paragraph("• Integrated <b>MySQL and SQLite</b> for structured data persistence and database-driven workflows, supporting reliable customer and application data management.", body_text))
    story.append(Paragraph("• Implemented <b>JWT-based access control, rate limiting, and input validation.</b>", body_text))
    story.append(Spacer(1, 4))

    # Project 2: ContentDesk
    p2_left = "<b>ContentDesk – AI Content & Data Processing Platform</b> &nbsp;&nbsp; <i>Python, Flask, SQLite, REST APIs, GitHub Actions</i>"
    p2_right = "<u><a href='https://github.com/Amanvarma2231/Content-_Desk' color='#000000'>GitHub</a></u>"
    p2_table = Table([[Paragraph(p2_left, body_text), Paragraph(p2_right, ParagraphStyle('R4', parent=body_text, alignment=TA_RIGHT))]], colWidths=[460, 80])
    p2_table.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
    story.append(p2_table)
    story.append(Paragraph("• Engineered a shared <b>Python/Flask backend</b> serving web and desktop application channels, centralizing business logic and database-access workflows for consistent application behavior.", body_text))
    story.append(Paragraph("• Developed an SEO-scoring crawler and <b>TF-IDF near-duplicate detection workflow</b> to automate content analysis and generate <b>data-driven recommendations.</b>", body_text))
    story.append(Paragraph("• Implemented <b>26 automated unit tests</b> in GitHub Actions CI, enabling automated testing on pull requests.", body_text))
    story.append(Spacer(1, 4))

    # 7. CERTIFICATIONS & ACTIVITIES
    add_section_header("CERTIFICATIONS & ACTIVITIES")
    story.append(Paragraph("• <b>Python Programming Certification</b> – Infosys Springboard &nbsp;&nbsp;&nbsp;&nbsp; <b>Quantitative Research Job Simulation</b> – JPMorgan", body_text))
    story.append(Paragraph("• Presented “Adaptive Residual-Energy Threshold LEACH for Performance & Energy Efficiency” at NGAISL-2026, HRIT University (Apr 2026).", body_text))

    doc.build(story)
    print(f"PDF successfully compiled at: {pdf_path}")

if __name__ == "__main__":
    build_pdf()
