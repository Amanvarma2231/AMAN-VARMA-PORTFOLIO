import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT

def build_pdf():
    output_dir = os.path.join(os.path.dirname(__file__), "frontend", "assets")
    os.makedirs(output_dir, exist_ok=True)
    pdf_path = os.path.join(output_dir, "Aman_Varma_Resume.pdf")

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
    
    contact_style = ParagraphStyle(
        'ContactInfo',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        alignment=TA_RIGHT,
        textColor=colors.HexColor("#111827")
    )

    section_heading = ParagraphStyle(
        'SectionHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=colors.HexColor("#002868"),
        spaceAfter=3
    )

    body_bold = ParagraphStyle(
        'BodyBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor("#000000")
    )

    body_text = ParagraphStyle(
        'BodyTextCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12.5,
        textColor=colors.HexColor("#1f2937")
    )

    story = []

    # Header Table
    name_html = "Aman Varma<br/><font size=8.5 color='#2563eb'><a href='http://127.0.0.1:8000'>Portfolio</a> | <a href='https://www.linkedin.com/in/aman-v-697771345'>LinkedIn</a> | <a href='https://github.com/Amanvarma2231'>GitHub</a></font>"
    name_p = Paragraph(name_html, title_style)
    
    contact_text = (
        "<b>Ghaziabad, India</b><br/>"
        "Mobile: +91-6306572504<br/>"
        "Email: <a href='mailto:amangurauli@gmail.com' color='#1f2937'>amangurauli@gmail.com</a>"
    )
    contact_p = Paragraph(contact_text, contact_style)

    header_table = Table([[name_p, contact_p]], colWidths=[320, 220])
    header_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('ALIGN', (1,0), (1,0), 'RIGHT'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0)
    ]))
    story.append(header_table)
    story.append(Spacer(1, 6))

    # Professional Summary
    story.append(Paragraph("PROFESSIONAL SUMMARY", section_heading))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#002868"), spaceBefore=1, spaceAfter=5))
    summary_txt = (
        "B.Tech Computer Science Engineering graduate with 7+ months of hands-on internship experience in Python Backend "
        "Development, RESTful APIs, FastAPI, Flask, database-driven applications, API integration, testing, and debugging. Experience "
        "in developing backend services and automated workflows using SQL/NoSQL databases, Git, and Docker, with additional "
        "experience in NLP, Generative AI, LLM concepts, and Prompt Engineering for AI-powered applications."
    )
    story.append(Paragraph(summary_txt, body_text))
    story.append(Spacer(1, 8))

    # Technical Skills
    story.append(Paragraph("TECHNICAL SKILLS", section_heading))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#002868"), spaceBefore=1, spaceAfter=5))
    skills_data = [
        [Paragraph("<b>Languages</b>", body_text), Paragraph(":", body_text), Paragraph("Python, Java, JavaScript, C++, SQL, HTML5", body_text)],
        [Paragraph("<b>AI ML</b>", body_text), Paragraph(":", body_text), Paragraph("Artificial Intelligence, Machine Learning, NLP, Generative AI, Prompt Engineering, LLMs", body_text)],
        [Paragraph("<b>DSA</b>", body_text), Paragraph(":", body_text), Paragraph("Data Structures Algorithms, Problem Solving, Algorithm Design", body_text)],
        [Paragraph("<b>Backend</b>", body_text), Paragraph(":", body_text), Paragraph("FastAPI, Flask, Django, RESTful APIs, Web Services", body_text)],
        [Paragraph("<b>API & Integration</b>", body_text), Paragraph(":", body_text), Paragraph("REST API Design, API Specifications, OpenAPI, API Integration, JWT, HTTP", body_text)],
        [Paragraph("<b>Databases</b>", body_text), Paragraph(":", body_text), Paragraph("MySQL, MongoDB, CRUD Operations", body_text)],
        [Paragraph("<b>DevOps & Tools</b>", body_text), Paragraph(":", body_text), Paragraph("Manual Testing, Data Validation, Debugging, Git, GitHub, Docker, CI/CD", body_text)]
    ]
    t_skills = Table(skills_data, colWidths=[110, 15, 415])
    t_skills.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
        ('TOPPADDING', (0,0), (-1,-1), 1.5)
    ]))
    story.append(t_skills)
    story.append(Spacer(1, 8))

    # Education
    story.append(Paragraph("EDUCATION", section_heading))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#002868"), spaceBefore=1, spaceAfter=5))
    edu_table = Table([[
        Paragraph("<b>NITRA Technical Campus, AKTU</b><br/><i>B.Tech, Computer Science & Engineering</i> <b>CGPA: 7.12/10</b>", body_bold),
        Paragraph("Ghaziabad UP, India<br/>May 2022 – June 2026", ParagraphStyle('RAlignEdu', parent=body_text, alignment=TA_RIGHT))
    ]], colWidths=[380, 160])
    edu_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0)
    ]))
    story.append(edu_table)
    story.append(Spacer(1, 8))

    # Experience
    story.append(Paragraph("EXPERIENCE", section_heading))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#002868"), spaceBefore=1, spaceAfter=5))
    exp_header = Table([[
        Paragraph("<b>Python Developer Intern</b><br/><i>Druidot Consulting (OPC) Pvt. Ltd.</i>", body_bold),
        Paragraph("Feb 2026 – Present<br/><i>Remote</i>", ParagraphStyle('RAlignExp', parent=body_text, alignment=TA_RIGHT))
    ]], colWidths=[380, 160])
    exp_header.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0)
    ]))
    story.append(exp_header)
    story.append(Spacer(1, 2))

    exp_bullets = [
        "Developed Python-based AI and backend applications using Flask and FastAPI, integrating RESTful APIs and data-processing workflows.",
        "Worked on NLP-based text processing and analysis for AI-oriented application workflows.",
        "Integrated Generative AI and LLM-based capabilities through AI API integrations and prompt-driven workflows.",
        "Built and optimized REST APIs, backend services, automation, testing, and debugging.",
        "Performed data validation and processing with MySQL and MongoDB, supporting reliable AI and backend workflows."
    ]
    for b in exp_bullets:
        story.append(Paragraph(f"• {b}", body_text))
        story.append(Spacer(1, 1.5))
    story.append(Spacer(1, 6))

    # Projects
    story.append(Paragraph("PROJECTS", section_heading))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#002868"), spaceBefore=1, spaceAfter=5))

    # NLPCRM
    proj1_table = Table([[
        Paragraph("<b>NLPCRM – AI-Powered CRM Platform</b> &nbsp;&nbsp;<font size=8 color='#4b5563'><i>Python, FastAPI, Flask, MySQL, SQLite, REST APIs</i></font>", body_bold),
        Paragraph("<a href='https://github.com/Amanvarma2231/NLPCRM' color='#002868'><u>GitHub</u></a>", ParagraphStyle('RAlign2', parent=body_text, alignment=TA_RIGHT))
    ]], colWidths=[440, 100])
    proj1_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0)
    ]))
    story.append(proj1_table)
    story.append(Paragraph("• Designed and developed <b>25+ RESTful API endpoints</b> across contacts, NLP, email, and webhook modules, implementing API specifications, CRUD operations, input validation, and modular backend workflows.", body_text))
    story.append(Paragraph("• Integrated <b>MySQL and SQLite</b> for structured data persistence and database-driven workflows, supporting reliable customer and application data management.", body_text))
    story.append(Paragraph("• Implemented <b>JWT-based access control, rate limiting, and input validation.</b>", body_text))
    story.append(Spacer(1, 5))

    # ContentDesk
    proj2_table = Table([[
        Paragraph("<b>ContentDesk – AI Content & Data Processing Platform</b> &nbsp;&nbsp;<font size=8 color='#4b5563'><i>Python, Flask, SQLite, REST APIs, GitHub Actions</i></font>", body_bold),
        Paragraph("<a href='https://github.com/Amanvarma2231/Content-_Desk' color='#002868'><u>GitHub</u></a>", ParagraphStyle('RAlign3', parent=body_text, alignment=TA_RIGHT))
    ]], colWidths=[440, 100])
    proj2_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0)
    ]))
    story.append(proj2_table)
    story.append(Paragraph("• Engineered a shared <b>Python/Flask backend</b> serving web and desktop application channels, centralizing business logic and database-access workflows for consistent application behavior.", body_text))
    story.append(Paragraph("• Developed an SEO-scoring crawler and <b>TF-IDF near-duplicate detection workflow</b> to automate content analysis and generate data-driven recommendations.", body_text))
    story.append(Paragraph("• Implemented <b>26 automated unit tests</b> in GitHub Actions CI, enabling automated testing on pull requests.", body_text))
    story.append(Spacer(1, 6))

    # Certifications & Activities
    story.append(Paragraph("CERTIFICATIONS & ACTIVITIES", section_heading))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#002868"), spaceBefore=1, spaceAfter=5))
    story.append(Paragraph("• <b>Python Programming Certification</b> – Infosys Springboard &nbsp;&nbsp;&nbsp;&nbsp; <b>Quantitative Research Job Simulation</b> – JPMorgan", body_text))
    story.append(Paragraph("• Presented <i>'Adaptive Residual-Energy Threshold LEACH for Performance & Energy Efficiency'</i> at NGAISL-2026, HRIT University (Apr 2026).", body_text))

    doc.build(story)
    print(f"PDF successfully generated at: {pdf_path}")

if __name__ == "__main__":
    build_pdf()
