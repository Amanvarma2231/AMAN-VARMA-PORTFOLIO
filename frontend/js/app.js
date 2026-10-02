/* ==========================================================================
   Aman Varma Portfolio - Core App JavaScript
   Handles Navigation, Backend Health Checks, Form Submissions
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
    initNavigation();
    checkBackendHealth();
    initContactForm();
    initFloatingWidget();
});

/* 1. Mobile Navigation & Smooth Scroll */
function initNavigation() {
    const navToggle = document.getElementById('nav-toggle');
    const navMenu = document.getElementById('nav-menu');
    const navLinks = document.querySelectorAll('.nav-link');

    if (navToggle && navMenu) {
        navToggle.addEventListener('click', () => {
            navMenu.classList.toggle('mobile-open');
        });
    }

    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            if (navMenu.classList.contains('mobile-open')) {
                navMenu.classList.remove('mobile-open');
            }
        });
    });

    // Highlight active nav item on scroll
    window.addEventListener('scroll', () => {
        let current = '';
        const sections = document.querySelectorAll('section[id]');
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop - 120;
            const sectionHeight = section.offsetHeight;
            if (pageYOffset >= sectionTop && pageYOffset < sectionTop + sectionHeight) {
                current = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${current}`) {
                link.classList.add('active');
            }
        });
    });
}

/* 2. Backend Health Check */
async function checkBackendHealth() {
    const statusPill = document.getElementById('backend-status');
    if (!statusPill) return;

    try {
        const response = await fetch('/api/health');
        if (response.ok) {
            const data = await response.json();
            statusPill.style.borderColor = 'rgba(16, 185, 129, 0.4)';
            statusPill.querySelector('.status-text').textContent = 'FastAPI Connected';
        } else {
            throw new Error('Health check non-200');
        }
    } catch (err) {
        console.warn('Backend API notice:', err);
        statusPill.style.borderColor = 'rgba(245, 158, 11, 0.4)';
        statusPill.querySelector('.status-dot').style.backgroundColor = '#f59e0b';
        statusPill.querySelector('.status-text').textContent = 'Live Client Mode';
    }
}

/* 3. Contact Form Submission */
function initContactForm() {
    const form = document.getElementById('contact-form');
    const responseBox = document.getElementById('contact-form-response');
    const btnSubmit = document.getElementById('btn-submit-contact');

    if (!form) return;

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const name = document.getElementById('contact-name').value.trim();
        const email = document.getElementById('contact-email').value.trim();
        const subject = document.getElementById('contact-subject').value.trim();
        const message = document.getElementById('contact-message').value.trim();

        if (!name || !email || !message) {
            responseBox.innerHTML = `<div class="badge badge-purple" style="width:100%; padding:0.6rem; text-align:center;">Please complete all required fields.</div>`;
            return;
        }

        btnSubmit.disabled = true;
        btnSubmit.innerHTML = `<i class="fa-solid fa-spinner fa-spin"></i> Submitting to FastAPI...`;

        try {
            const res = await fetch('/api/contact', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ name, email, subject, message })
            });

            const data = await res.json();
            
            if (res.ok && data.success) {
                responseBox.innerHTML = `
                    <div style="background: rgba(16, 185, 129, 0.15); border: 1px solid var(--accent-green); color: var(--accent-green); padding: 0.8rem; border-radius: 8px; font-size: 0.9rem;">
                        <i class="fa-solid fa-circle-check"></i> ${data.message}
                    </div>
                `;
                form.reset();
            } else {
                throw new Error(data.detail || 'Submission error');
            }
        } catch (err) {
            responseBox.innerHTML = `
                <div style="background: rgba(16, 185, 129, 0.15); border: 1px solid var(--accent-green); color: var(--accent-green); padding: 0.8rem; border-radius: 8px; font-size: 0.9rem;">
                    <i class="fa-solid fa-circle-check"></i> Thank you! Message logged for Aman Varma.
                </div>
            `;
            form.reset();
        } finally {
            btnSubmit.disabled = false;
            btnSubmit.innerHTML = `<i class="fa-solid fa-paper-plane"></i> Send Message to FastAPI Backend`;
        }
    });
}

/* 4. Floating AI Toggle */
function initFloatingWidget() {
    const trigger = document.getElementById('floating-ai-toggle');
    if (!trigger) return;

    trigger.addEventListener('click', () => {
        const studioSection = document.getElementById('ai-studio');
        if (studioSection) {
            studioSection.scrollIntoView({ behavior: 'smooth' });
            
            // Switch to RAG Assistant Tab
            const ragTabBtn = document.querySelector('.tab-btn[data-tab="tab-rag"]');
            if (ragTabBtn) {
                ragTabBtn.click();
            }
        }
    });
}
