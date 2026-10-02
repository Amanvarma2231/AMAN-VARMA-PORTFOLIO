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
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'NameTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=colors.HexColor("#0f172a")
    )
    
    contact_style = ParagraphStyle(
        'ContactInfo',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13,
        alignment=TA_RIGHT,
        textColor=colors.HexColor("#334155")
    )

    section_heading = ParagraphStyle(
        'SectionHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#0284c7"),
        spaceAfter=4
    )

    body_bold = ParagraphStyle(
        'BodyBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor("#0f172a")
    )

    body_text = ParagraphStyle(
        'BodyTextCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor("#334155")
    )

    story = []

    # Header Table
    name_p = Paragraph("Aman Varma", title_style)
    sub_title = Paragraph("<font color='#0284c7'><b>Python Backend, Generative AI & NLP Engineer</b></font>", body_bold)
    
    contact_text = (
        "Ghaziabad, UP, India<br/>"
        "Mobile: +91-6306572504 | Email: amangurauli@gmail.com<br/>"
        "LinkedIn: linkedin.com/in/aman-v-697771345<br/>"
        "GitHub: github.com/Amanvarma2231"
    )
    contact_p = Paragraph(contact_text, contact_style)

    header_table = Table([[Paragraph("Aman Varma<br/><font size=10 color='#0284c7'>Python Backend, GenAI & NLP Engineer</font>", title_style), contact_p]], colWidths=[300, 240])
    header_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('ALIGN', (1,0), (1,0), 'RIGHT')
    ]))
    story.append(header_table)
    story.append(Spacer(1, 8))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#0284c7"), spaceBefore=2, spaceAfter=8))

    # Professional Summary
    story.append(Paragraph("PROFESSIONAL SUMMARY", section_heading))
    summary_txt = (
        "B.Tech Computer Science Engineering graduate with 7+ months of hands-on internship experience in Python Backend "
        "Development, RESTful APIs, FastAPI, Flask, database-driven applications, API integration, testing, and debugging. Experience "
        "in developing backend services and automated workflows using SQL/NoSQL databases, Git, and Docker, with additional "
        "experience in NLP, Generative AI, LLM concepts, and Prompt Engineering for AI-powered applications."
    )
    story.append(Paragraph(summary_txt, body_text))
    story.append(Spacer(1, 10))

    # Technical Skills
    story.append(Paragraph("TECHNICAL SKILLS", section_heading))
    skills_data = [
        [Paragraph("<b>Languages:</b>", body_text), Paragraph("Python, Java, JavaScript, C++, SQL, HTML5", body_text)],
        [Paragraph("<b>AI / ML / NLP:</b>", body_text), Paragraph("Artificial Intelligence, Machine Learning, NLP, Generative AI, Prompt Engineering, LLMs", body_text)],
        [Paragraph("<b>Backend & APIs:</b>", body_text), Paragraph("FastAPI, Flask, Django, RESTful APIs, OpenAPI, Web Services, JWT, HTTP", body_text)],
        [Paragraph("<b>Databases:</b>", body_text), Paragraph("MySQL, MongoDB, SQLite, CRUD Operations, Data Persistence", body_text)],
        [Paragraph("<b>DevOps & Tools:</b>", body_text), Paragraph("Git, GitHub, Docker, CI/CD, GitHub Actions, Manual Testing, Debugging", body_text)]
    ]
    t_skills = Table(skills_data, colWidths=[110, 430])
    t_skills.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('TOPPADDING', (0,0), (-1,-1), 2)
    ]))
    story.append(t_skills)
    story.append(Spacer(1, 10))

    # Experience
    story.append(Paragraph("WORK EXPERIENCE", section_heading))
    exp_header = Table([[
        Paragraph("<b>Python Developer Intern</b> — <i>Druidot Consulting (OPC) Pvt. Ltd.</i>", body_bold),
        Paragraph("Feb 2026 – Present | Remote", ParagraphStyle('RAlign', parent=body_text, alignment=TA_RIGHT))
    ]], colWidths=[380, 160])
    exp_header.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP')]))
    story.append(exp_header)
    story.append(Spacer(1, 3))

    exp_bullets = [
        "Developed Python-based AI and backend applications using Flask and FastAPI, integrating RESTful APIs and data-processing workflows.",
        "Worked on NLP-based text processing and analysis for AI-oriented application workflows.",
        "Integrated Generative AI and LLM-based capabilities through AI API integrations and prompt-driven workflows.",
        "Built and optimized REST APIs, backend services, automation, testing, and debugging.",
        "Performed data validation and processing with MySQL and MongoDB, supporting reliable AI and backend workflows."
    ]
    for b in exp_bullets:
        story.append(Paragraph(f"• {b}", body_text))
        story.append(Spacer(1, 2))
    story.append(Spacer(1, 8))

    # Projects
    story.append(Paragraph("FEATURED PROJECTS", section_heading))

    # NLPCRM
    proj1_table = Table([[
        Paragraph("<b>NLPCRM – AI-Powered CRM Platform</b> (Python, FastAPI, Flask, MySQL, SQLite)", body_bold),
        Paragraph("<a href='https://nlpcrm-1.onrender.com/' color='#0284c7'>Live App</a> | <a href='https://github.com/Amanvarma2231/NLPCRM' color='#0284c7'>GitHub</a>", ParagraphStyle('RAlign2', parent=body_text, alignment=TA_RIGHT))
    ]], colWidths=[380, 160])
    proj1_table.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP')]))
    story.append(proj1_table)
    story.append(Paragraph("• Designed and developed <b>25+ RESTful API endpoints</b> across contacts, NLP, email, and webhook modules.", body_text))
    story.append(Paragraph("• Integrated MySQL and SQLite for structured data persistence and database-driven workflows.", body_text))
    story.append(Paragraph("• Implemented JWT-based access control, rate limiting, and strict input validation.", body_text))
    story.append(Spacer(1, 6))

    # ContentDesk
    proj2_table = Table([[
        Paragraph("<b>ContentDesk – AI Content & Data Processing Platform</b> (Python, Flask, SQLite)", body_bold),
        Paragraph("<a href='https://content-desk.onrender.com/' color='#0284c7'>Live App</a> | <a href='https://github.com/Amanvarma2231/Content-_Desk' color='#0284c7'>GitHub</a>", ParagraphStyle('RAlign3', parent=body_text, alignment=TA_RIGHT))
    ]], colWidths=[380, 160])
    proj2_table.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP')]))
    story.append(proj2_table)
    story.append(Paragraph("• Engineered shared Python/Flask backend serving web and desktop application channels.", body_text))
    story.append(Paragraph("• Developed an SEO-scoring crawler and <b>TF-IDF near-duplicate detection workflow</b>.", body_text))
    story.append(Paragraph("• Implemented <b>26 automated unit tests</b> in GitHub Actions CI pipeline.", body_text))
    story.append(Spacer(1, 8))

    # Education
    story.append(Paragraph("EDUCATION", section_heading))
    edu_table = Table([[
        Paragraph("<b>NITRA Technical Campus, AKTU</b> — <i>B.Tech, Computer Science & Engineering</i>", body_bold),
        Paragraph("Ghaziabad UP, India<br/>May 2022 – June 2026", ParagraphStyle('RAlign4', parent=body_text, alignment=TA_RIGHT))
    ]], colWidths=[380, 160])
    edu_table.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP')]))
    story.append(edu_table)
    story.append(Paragraph("• <b>CGPA:</b> 7.12 / 10", body_text))
    story.append(Spacer(1, 8))

    # Certifications & Activities
    story.append(Paragraph("CERTIFICATIONS & RESEARCH", section_heading))
    story.append(Paragraph("• <b>Python Programming Certification</b> – Infosys Springboard", body_text))
    story.append(Paragraph("• <b>Quantitative Research Job Simulation</b> – JPMorgan", body_text))
    story.append(Paragraph("• Presented <i>'Adaptive Residual-Energy Threshold LEACH for Performance & Energy Efficiency'</i> at NGAISL-2026, HRIT University (Apr 2026).", body_text))

    doc.build(story)
    print(f"PDF successfully generated at: {pdf_path}")

if __name__ == "__main__":
    build_pdf()
